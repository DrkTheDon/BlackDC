#!/usr/bin/python3

#####################################################
## Black Discord (BlackDC)                         ##
## A discord Selfbot.                              ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
from turtle import clear
from urllib.parse import uses_fragment
import discord
from colorama import Fore
import time
import os
import itertools
from datetime import datetime
from discord.ext import commands

# Useful Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global Variables
bot = discord.Client()
TOKEN = "YOUR_TOKEN_HERE" # This is for Debugging (DEVS)
now = datetime.now()
curtime = now.strftime("%H:%M")
PREFIX = "drk"
COMMANDS = {
    "help", 
}
# Main 
clearcmd()

print(f"{Fore.YELLOW}[*] Starting DSB...")
time.sleep(3.5)
clearcmd()

@bot.event
async def on_ready():
    print(f"{Fore.YELLOW}BlackDC - V.0.3 - BETA")  
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}")
    print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Conntected to {Fore.YELLOW}{bot.user}")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}[!]{Fore.LIGHTWHITE_EX} Send {Fore.GREEN}drk help{Fore.LIGHTWHITE_EX} to start!")
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------\n{Fore.LIGHTWHITE_EX}")

    

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
    if message.content == f"{PREFIX} help":
        await message.channel.send(f"{message.author.mention} This bot is under development!") 
        
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}Sent {Fore.RED}This bot is under development!{Fore.LIGHTWHITE_EX} in {Fore.YELLOW}#{message.channel} ")

    

# Main Run
try:
    bot.run(TOKEN, bot=False)
except discord.errors.LoginFailure:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Inproper Token or disabled account.")
    time.sleep(0.5)
    quit()
except KeyboardInterrupt:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Quitting.")
    time.sleep(0.5)
    clearcmd()
    quit()
