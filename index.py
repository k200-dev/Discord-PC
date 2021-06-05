# Imports
import ctypes
import discord
import yaml
import os
from discord.ext import commands 
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import webbrowser
from pythonping import ping

# Read the yaml config file, contains hidden variables
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
    # Confirm read worked
    print("Read successful")

# Define the hidden variables in a cleaner way
banned_words = config['BANNEDWORDS']
banned_processes = config['BANNEDPROCESSES']
token = config['TOKEN']
username = config['USERNAME']
guild_ids = config['GUILDIDS']
server_ip = config['SERVERIP']


# Initalise the bot client
bot = commands.Bot(command_prefix="$")

# Initalise slash commands
slash = SlashCommand(bot, sync_commands=True)

# Events that happen when the bot becomes online
@bot.event
async def on_ready():
  # Change the bots status to "Listening to the flames of a PC"
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the flames of a PC"))
  # Confirm the bot is online
  print("Online")

# Create the lock PC command
@slash.slash(name="lock", description="Lock the PC")
async def _lock(ctx):
  # Saves a list of all the running processes on the PC
    output = os.popen('wmic process get description, processid').read()
    # Check if a banned process is running and stop the command if true
    for x in banned_processes:
      if x in output:
       await ctx.send(f"⚠️ **{username}** is currently running a banned process. **({x})**")
       return
    # Lock the PC and send the confirmation message to the channel
    ctypes.windll.user32.LockWorkStation()
    await ctx.send(f"🔒 Locked **{username}s** PC")

# Create the message box command
@slash.slash(name="message",
             description="Send a message box to the PC",
             options=[
               create_option(
                 name="message_to_send",
                 description="The message to send",
                 option_type=3,
                 required=True
               )
             ])
async def message(ctx, message_to_send: str):
    # Sends a popup message box with the input message to the PC
    await ctx.send(content=f"💬 Sending dialogue box with **{message_to_send}** to **{username}s** PC.")
    MessageBox = ctypes.windll.user32.MessageBoxW 
    MessageBox(None, message_to_send, "Message from discord bot", 0)
    
# Create the search browser command
@slash.slash(name="search",
             description="Searches the web for something on the PC",
             options=[
               create_option(
                 name="thing_to_search",
                 description="The thing to search the web for",
                 option_type=3,
                 required=True
               )
             ])
async def search(ctx, thing_to_search: str):
    # Checks for banned search terms in the input and stops the command if it does
    for x in banned_words:
        if x in thing_to_search:
            await ctx.send("⚠️ This search term is not allowed")
            return
    await ctx.send(content=f"🔍 Searching for **{thing_to_search}** on **{username}s** PC.")
    # Opens the default web browser and inputs the search URL
    webbrowser.open_new_tab(f"https://duckduckgo.com/?t=ffab&q={thing_to_search}" )

# Create the add quote to book command
@slash.slash(name="quote",
             description="Adds things to the quote book",
             options=[
               create_option(
                 name="quote",
                 description="The quote to add",
                 option_type=3,
                 required=True
               )
             ])
async def quote(ctx, quote: str):
    await ctx.send(content=f"🖊️ Added quote **{quote}** to the book")
    # Opens the quotes file
    f = open("quotes.txt", "a")
    # Writes the quote to a newline in the file
    f.write(f"\n\"{quote}\"")
    # Closes the quotes file
    f.close()

# Create the add quote to book command
@slash.slash(name="serverping", description="Checks the ping and online status of a server")
async def serverping(ctx):
    response = ping(server_ip)
    if response.rtt_avg_ms >= 2000:
      await ctx.send(content="🔴 The server is offline")
    else:
      await ctx.send(content=f"🟢 The server is online")

# Run the bot with the provided token
bot.run(token)