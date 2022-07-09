#!/usr/bin/python3

#####################################################
## Black Discord (BlackDC)                         ##
## A discord Selfbot.                              ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
from logging import exception
from urllib.parse import uses_fragment
import discord
from colorama import Fore
import time
import os
from datetime import datetime
from discord.ext import commands, tasks
import linecache
import asyncio
import requests
import numpy
from discord.ext.commands import Bot
from discord.utils import get
from discord import Permissions
from discord.ext import *
from discord.ext.commands import bot
from discord.ext.commands.errors import *
from discord.ext.commands.errors import DiscordException, ClientException
import discord.ext.commands.errors
from discord.ext.commands.errors import CommandError, CommandNotFound
import traceback
import sys
import json

# Useful Defines    
token_file_size = os.stat("./assets/token.txt").st_size
client = discord.Client()
activity = discord.Activity(type=discord.ActivityType.playing, name="BlackDC")
bot = commands.Bot (command_prefix="bdc ", self_bot=True,  help_command=None, activity=activity)


def checktoken():
    if token_file_size == 0:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} No local token found.")
        user_token = input(f"{Fore.YELLOW}[?] {Fore.LIGHTWHITE_EX}Enter a {Fore.GREEN}VALID{Fore.LIGHTWHITE_EX} token\n{Fore.RED}>") 
        with open("./assets/token.txt", "w+") as file:
            file.write("## DO NOT CHANGE ANY OF THIS OTHERWISE BlackDC WILL NOT WORK PROPERLY!!! If you want a new token then you should edit the token below!\n")
            file.write(user_token)
            file.close()
            print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Saved token in {Fore.YELLOW}./assets/token.txt{Fore.LIGHTWHITE_EX}")
            time.sleep(1.5)
            clearcmd()
            print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} New token found restart BlackDC to make change.")
            time.sleep(1)
            input(f"{Fore.YELLOW}Press enter to quit")
            clearcmd()
            quit()
    else:
        print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Token Found: {Fore.YELLOW}{TOKEN}{Fore.LIGHTWHITE_EX}")
        change_yn = input(f"Do you want to change the token? (y/n)\n{Fore.RED}>")
        if change_yn == "y":
            tokench = input(f"Desired token?\n{Fore.RED}>")
            with open("./assets/token.txt", "w+") as file:
                file.write("## DO NOT CHANGE ANY OF THIS OTHERWISE BlackDC WILL NOT WORK PROPERLY!!! If you want a new token then you should edit the token below!\n")
                file.write(tokench)
                file.close()
                clearcmd()
                print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Set token as: {Fore.YELLOW} {tokench}")
                time.sleep(1)
                clearcmd()
                print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} New token found restart BlackDC to make change.")
                time.sleep(1)
                input(f"{Fore.YELLOW}Press enter to quit")
                clearcmd()
                quit()
        elif change_yn == "n":
            clearcmd()
            pass
        else:
            print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not recognize your input. Continuing with the found token.")
            time.sleep(2)
            clearcmd()

TOKEN_VAR = linecache.getline('./assets/token.txt', 2)
TOKEN = TOKEN_VAR              



def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global Variables
# bot = discord.Client()
now = datetime.now()
curtime = now.strftime("%H:%M")

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
    print(f"{Fore.MAGENTA}BlackDC - V.0.6 - BETA")  
    time.sleep(0.5)
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}")
    print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Connected to {Fore.YELLOW}{bot.user}")
    print(f"{Fore.YELLOW}[!]{Fore.LIGHTWHITE_EX} Send {Fore.GREEN}bdc help{Fore.LIGHTWHITE_EX} In Discord to start!")
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------\n{Fore.LIGHTWHITE_EX}")
    

         

@bot.command()
async def help(ctx):
    if ctx.author != bot.user:
        return
    else:
        await ctx.message.delete()
        print(f"{Fore.GREEN}COMMANDS:")
        print(f"""
        {Fore.YELLOW}test{Fore.LIGHTWHITE_EX} - tests the bot -
        {Fore.YELLOW}spam{Fore.LIGHTWHITE_EX} - spams a certain message -{Fore.YELLOW} bdc spam <amount> <message> 
        {Fore.YELLOW}ghostping{Fore.LIGHTWHITE_EX} - Ghostspings people -{Fore.YELLOW} bdc ghostping <amount> <user>
        {Fore.YELLOW}delchn{Fore.LIGHTWHITE_EX} - deletes all channels in server -{Fore.YELLOW} bdc delchn
        {Fore.YELLOW}crechn{Fore.LIGHTWHITE_EX} - creates alot of channels -{Fore.YELLOW} bdc crechn <amount> <channelname>

        """)
@bot.command()
async def test(ctx):
    if ctx.author != bot.user:
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[!] {Fore.LIGHTWHITE_EX}Ignored command from{Fore.RED} {ctx.author} {Fore.LIGHTWHITE_EX}In {Fore.YELLOW}#{ctx.channel} ")
        return
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} BlackDC is working!", delete_after=1.5)
    print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}BlackDC is {Fore.RED}Working{Fore.LIGHTWHITE_EX} sent in {Fore.YELLOW}#{ctx.channel} ")


@bot.command()
async def clearpm(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()

@bot.command()
async def av(ctx, member : discord.Member = None):
  if member == None:
    member = ctx.author
  avatar = member.avatar_url
  await ctx.send(f"{ctx.member.mention}'s avatar", avatar)

@bot.command()
async def delchn(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    for chn in ctx.guild.channels:
        await chn.delete()
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.RED}Deleted Channel{Fore.LIGHTWHITE_EX}{Fore.YELLOW} {chn}{Fore.LIGHTWHITE_EX}")
    print(f"{Fore.BLUE}{curtime} {Fore.GREEN}[+] {Fore.RED}Deleted All Channels in{Fore.LIGHTWHITE_EX}{Fore.YELLOW} {ctx.guild}{Fore.LIGHTWHITE_EX}")

@bot.command()
async def crechn(ctx, amount:int, *, name):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    guild = ctx.message.guild
    for chn in range(amount):
        await guild.create_text_channel(f'{name}-{chn}')
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.RED}Created Channel{Fore.LIGHTWHITE_EX}{Fore.YELLOW} {name}-{chn}{Fore.LIGHTWHITE_EX} In {Fore.YELLOW}{guild}")
    print(f"{Fore.BLUE}{curtime} {Fore.GREEN}[+] {Fore.RED}Created {amount} Channels in{Fore.LIGHTWHITE_EX}{Fore.YELLOW} {guild}{Fore.LIGHTWHITE_EX}")


@bot.command()
async def spam(ctx, *, message):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    for i in range(100000):
        await ctx.send(message)
        if message == "stop":
            return
            

@bot.command()
async def ghostping(ctx, amount:int, *, message):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message, delete_after=0.1)
        await asyncio.sleep(5.0)

    

# Main Run
while __name__ == '__main__':
    try:
        bot.run(TOKEN, bot=False)
   
    except AttributeError:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Attribute error, try cheking for misspellings")

    except ModuleNotFoundError:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Got An import error try following the instructions in https://github.com/DrkTheDon/BlackDC/wiki/Installation-of-BlackDC")
        time.sleep(1)
        quit()

    except discord.errors.LoginFailure:
        print(f"{Fore.MAGENTA}TOKEN: {Fore.LIGHTWHITE_EX}{TOKEN}")
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Improper Token or disabled account.\n{Fore.YELLOW}NOTE:{Fore.LIGHTWHITE_EX} If you have any quotes like \" or \' then remove them from your token in ./assets/token.txt")
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

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound): 
            await ctx.send("Unknown command") 
        
