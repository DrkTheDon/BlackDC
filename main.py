#!/usr/bin/python3

#####################################################
## Black Discord (BlackDC)                         ##
## A discord Selfbot.                              ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
from urllib.parse import uses_fragment
import discord
from colorama import Fore
import time
import os
from datetime import datetime
from discord.ext import commands
import linecache

# Useful Defines
token_file_size = os.path.getsize("assets/token.txt")

def checktoken():
    if token_file_size == 0:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} No local token found.")
        user_token = input(f"{Fore.YELLOW}[?] {Fore.LIGHTWHITE_EX}Enter a {Fore.GREEN}VALID{Fore.LIGHTWHITE_EX} token\n{Fore.RED}>") 
        with open("./assets/token.txt", "w+") as file:
            file.write(user_token)
            file.close()
            print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Saved token in {Fore.YELLOW}./assets/token.txt{Fore.LIGHTWHITE_EX}")
    else:
        print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Token Found using that one.")
        clearcmd()

TOKEN_VAR = linecache.getline('./assets/token.txt', 2)
TOKEN = TOKEN_VAR # This is for Debugging (DEVS)

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global Variables
bot = discord.Client()
now = datetime.now()
curtime = now.strftime("%H:%M")
PREFIX = "bdc"
COMMANDS = { # In development
    "help", 
}
# Main 
clearcmd()

print(f"{Fore.YELLOW}[*] Starting BDC...")
time.sleep(1.5)
clearcmd()
checktoken()
print(f"""
                        {Fore.RED}LICENSE AGREEMNT\n{Fore.LIGHTWHITE_EX}
                    GNU GENERAL PUBLIC LICENSE
                    Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it and removing credits is not allowed.

{Fore.YELLOW}https://github.com/DrkTheDon/BlackDC/blob/main/LICENSE
""")
time.sleep(3.3)
clearcmd()

@bot.event
async def on_ready():
    print(f"{Fore.MAGENTA}BlackDC - V.0.3 - BETA")  
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}")
    print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Conntected to {Fore.YELLOW}{bot.user}")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}[!]{Fore.LIGHTWHITE_EX} Send {Fore.GREEN}bdc help{Fore.LIGHTWHITE_EX} to start!")
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------\n{Fore.LIGHTWHITE_EX}")

    

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
    if message.content == f"{PREFIX} help":
        await message.channel.send(f"{message.author.mention} This bot is under development!") 
        
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}Sent {Fore.RED}This bot is under development!{Fore.LIGHTWHITE_EX} in {Fore.YELLOW}#{message.channel} ")
    elif message.content == f"{PREFIX}":
        await message.channel.send(f"{message.author.mention} This bot is under development!") 

    

# Main Run
try:
    bot.run(TOKEN, bot=False)
except ModuleNotFoundError:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Got An import errror try following the instructions in https://github.com/DrkTheDon/BlackDC")
    time.sleep(1)
    quit()
except discord.errors.LoginFailure:
    print(f"{Fore.MAGENTA}TOKEN: {Fore.LIGHTWHITE_EX}{TOKEN}")
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Inproper Token or disabled account.\n{Fore.YELLOW}NOTE:{Fore.LIGHTWHITE_EX} If you have any quotes like \" or \' then remove them from your token in ./assets/token.txt")
    time.sleep(1.5)
    quit()
except KeyboardInterrupt:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Quitting.")
    time.sleep(0.5)
    clearcmd()
    quit()
