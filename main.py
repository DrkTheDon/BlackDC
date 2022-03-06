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
import asyncio
import requests
import numpy
from discord.ext.commands import Bot
from discord.utils import get
from discord import Permissions

# Useful Defines    
token_file_size = os.path.getsize("assets/token.txt")


def checktoken():
    if token_file_size == 0:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} No local token found.")
        user_token = input(f"{Fore.YELLOW}[?] {Fore.LIGHTWHITE_EX}Enter a {Fore.GREEN}VALID{Fore.LIGHTWHITE_EX} token\n{Fore.RED}>") 
        with open("./assets/token.txt", "w+") as file:
            file.write("## DO NOT CHANGE ANY OF THIS OTHERWISE BlackDC WILL NOT WORK PROPERLY!!!\n")
            file.write(user_token)
            file.close()
            print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Saved token in {Fore.YELLOW}./assets/token.txt{Fore.LIGHTWHITE_EX}")
            time.sleep(1.5)
            clearcmd()
            print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} New token found restart BlackDC to make change.")
            time.sleep(1)
            entet_t_q = input(f"{Fore.YELLOW}Press enter to quit")
            clearcmd()
            quit()
    else:
        print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Token Found using that one.")
        clearcmd()

TOKEN_VAR = linecache.getline('./assets/token.txt', 2)
TOKEN = TOKEN_VAR 


def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global Variables
# bot = discord.Client()
bot = commands.Bot (command_prefix="bdc ", self_bot=True, help_command=None)
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

    

@bot.command()
async def help(ctx):
    if ctx.author != bot.user:
        return
    else:
        await ctx.message.delete()
        print(f"{Fore.GREEN}COMMANDS:")
        print(f"""
        {Fore.YELLOW}test{Fore.LIGHTWHITE_EX} - tests the bot
        {Fore.YELLOW}spam{Fore.LIGHTWHITE_EX} - spams a certain message
        {Fore.YELLOW}clearpm{Fore.LIGHTWHITE_EX} - clears all of your messages
        {Fore.YELLOW}delchn{Fore.LIGHTWHITE_EX} - deletes all channels in server
        {Fore.YELLOW}crechn{Fore.LIGHTWHITE_EX} - creates alot of channels

        """)

        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}Sent {Fore.RED}BlackDC Commands{Fore.LIGHTWHITE_EX} in {Fore.YELLOW}#{ctx.channel} ")

@bot.command()
async def test(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} BlackDC is working!", delete_after=1.5)
    print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}BlackDC is {Fore.RED}Working{Fore.LIGHTWHITE_EX} sent in {Fore.YELLOW}#{ctx.channel} ")


@bot.command()
async def clearpm(ctx):
    if ctx.author != bot.user:
        return

@bot.command()
async def delchn(ctx):
    if ctx.author != bot.user:
        return

@bot.command()
async def crechn(ctx):
    if ctx.author != bot.user:
        return

@bot.command()
async def spam(ctx):
    if ctx.author != bot.user:
        return


# Main Run
while __name__ == '__main__':
    try:
        bot.run(TOKEN, bot=False)
    except ModuleNotFoundError:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Got An import errror try following the instructions in https://github.com/DrkTheDon/BlackDC/wiki/Installation-of-BlackDC")
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
    except RuntimeError:
        clearcmd()
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} CTRL + C detected, quitting...")
        time.sleep(0.5)
        clearcmd()
        quit()
