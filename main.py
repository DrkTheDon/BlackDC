#!/usr/bin/python3

#####################################################
## Black Discord (BlackDC)                         ##
## A discord Selfbot.                              ##
## https://drkbro.ml/                              ##
## Coded by: drk                                   ##
#####################################################

# Imports
from logging import exception
from urllib.parse import uses_fragment
import discord
from colorama import Fore # OLD LIB 
from pystyle import Colorate, Colors # NEW LIB
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
    if token_file_size == 1:
        print(f"{Colors.red}[-]{Colors.white} No local token found.")
        user_token = input(f"{Colors.yellow}[?] {Colors.white}Enter a {Colors.green}VALID{Colors.white} token\n{Colors.red}>") 
        with open("./assets/token.txt", "w+") as file:
            file.write("## DO NOT CHANGE ANY OF THIS OTHERWISE BlackDC WILL NOT WORK PROPERLY!!! If you want a new token then you should edit the token below!\n")
            file.write(user_token)
            file.close()
            print(f"{Colors.green}[+]{Colors.white} Saved token in {Colors.yellow}./assets/token.txt{Colors.white}")
            time.sleep(1.5)
            clearcmd()
            print(f"{Colors.yellow}[*]{Colors.white} New token found restart BlackDC to make change.")
            time.sleep(1)
            input(f"{Colors.yellow}Press enter to quit")
            clearcmd()
            quit()
    else:
        print(f"{Colors.green}[+]{Colors.white} Token Found: {Colors.yellow}{TOKEN}{Colors.white}")
        change_yn = input(f"{Colors.yellow}[?]{Colors.white} Is this the correct token? (y/n)\n{Colors.red}>")
        if change_yn == "n":
            tokench = input(f"Desired new token?\n{Colors.red}>")
            with open("./assets/token.txt", "w+") as file:
                file.write("## DO NOT CHANGE ANY OF THIS OTHERWISE BlackDC WILL NOT WORK PROPERLY!!! If you want a new token then you should edit the token below!\n")
                file.write(tokench)
                file.close()
                clearcmd()
                print(f"{Colors.green}[+]{Colors.white} Set token as: {Colors.yellow} {tokench}")
                time.sleep(1)
                clearcmd()
                print(f"{Colors.yellow}[*]{Colors.white} New token found restart BlackDC to make change.")
                time.sleep(1)
                input(f"{Colors.yellow}Press enter to quit")
                clearcmd()
                quit()
        elif change_yn == "y":
            clearcmd()
            pass
        else:
            print(f"{Colors.red}[-]{Colors.white} Did not recognize your input. Continuing with the found token.")
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

print(f"{Colors.yellow}[*] Starting BDC...")
time.sleep(1.5)
clearcmd()
checktoken()
print(f"""
                        {Colors.red}LICENSE AGREEMNT\n{Colors.white}
                    GNU GENERAL PUBLIC LICENSE
                    Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it and removing credits is not allowed.

{Colors.yellow}https://github.com/DrkTheDon/BlackDC/blob/main/LICENSE
""")
time.sleep(3.3)
clearcmd()

@bot.event
async def on_ready():
    print(f"{Colors.purple}BlackDC - V.0.7 - BETA ACCESS")  
    time.sleep(0.5)
    print(f"{Colors.yellow}----------------------------------------------------------------------------------{Colors.white}")
    print(f"{Colors.green}[+]{Colors.white} Loaded {Colors.red}BlackDC V.0.7{Colors.white} by {Colors.green}drk#1337")
    time.sleep(0.5)
    print(f"{Colors.yellow}----------------------------------------------------------------------------------{Colors.white}")
    print(f"{Colors.green}[+]{Colors.white} Connected to {Colors.yellow}{bot.user}")
    print(f"{Colors.yellow}[!]{Colors.white} Send {Colors.green}bdc help{Colors.white} In Discord to start!")
    print(f"{Colors.yellow}----------------------------------------------------------------------------------\n{Colors.white}")
    

         

@bot.command()
async def help(ctx):
    if ctx.author != bot.user:
        return
    else:
        await ctx.message.delete()
        print(f"{Colors.green}COMMANDS:")
        print(f"""
        {Colors.yellow}test{Colors.white} - tests the bot -{Colors.yellow} bdc test 
        {Colors.yellow}spam{Colors.white} - spams a certain message -{Colors.yellow} bdc spam <amount> <message> {Colors.red} UNDER DEVELOPMENT!
        {Colors.yellow}ghostping{Colors.white} - Ghostspings people -{Colors.yellow} bdc ghostping <amount> <user>
        {Colors.yellow}delchn{Colors.white} - deletes all channels in server -{Colors.yellow} bdc delchn
        {Colors.yellow}crechn{Colors.white} - creates alot of channels -{Colors.yellow} bdc crechn <amount> <channelname>
        {Colors.yellow}serverinfo{Colors.white} - displays info about the server-{Colors.yellow} bdc serverinfo {Colors.red} UNDER DEVELOPMENT!
        {Colors.yellow}clearcmd{Colors.white} - clears the cmd/terminal -{Colors.yellow} bdc clearcmd {Colors.red} UNDER DEVELOPMENT!

        """)
    
@bot.command()
async def test(ctx):
    if ctx.author != bot.user:
        print(f"{Colors.blue}{curtime} {Colors.yellow}[!] {Colors.white}Ignored command from{Colors.red} {ctx.author} {Colors.white}In {Colors.yellow}#{ctx.channel} ")
        return
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} BlackDC is working!", delete_after=1.5)
    print(f"{Colors.blue}{curtime} {Colors.yellow}[*] {Colors.white}BlackDC is {Colors.red}Working{Colors.white} sent in {Colors.yellow}#{ctx.channel} ")


@bot.command()
async def clearpm(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()

@bot.command()
async def clearcmd(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} Making the terminal clean!", delete_after=0.5)
    clearcmd()
    print(f"{Colors.purple}BlackDC - V.0.7 - BETA ACCESS")  
    print(f"{Colors.yellow}----------------------------------------------------------------------------------{Colors.white}")
    print(f"{Colors.green}[+]{Colors.white} Loaded {Colors.red}BlackDC V.0.7{Colors.white} by {Colors.green}drk#1337")
    print(f"{Colors.yellow}----------------------------------------------------------------------------------{Colors.white}")
    print(f"{Colors.green}[+]{Colors.white} Connected to {Colors.yellow}{bot.user}")
    print(f"{Colors.yellow}[!]{Colors.white} Send {Colors.green}bdc help{Colors.white} In Discord to start!")
    print(f"{Colors.yellow}----------------------------------------------------------------------------------\n{Colors.white}")
    
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
        print(f"{Colors.blue}{curtime} {Colors.yellow}[*] {Colors.red}Deleted Channel{Colors.white}{Colors.yellow} {chn}{Colors.white}")
    print(f"{Colors.blue}{curtime} {Colors.green}[+] {Colors.red}Deleted All Channels in{Colors.white}{Colors.yellow} {ctx.guild}{Colors.white}")

@bot.command()
async def crechn(ctx, amount:int, *, name):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    guild = ctx.message.guild
    for chn in range(amount):
        await guild.create_text_channel(f'{name}-{chn}')
        print(f"{Colors.blue}{curtime} {Colors.yellow}[*] {Colors.red}Created Channel{Colors.white}{Colors.yellow} {name}-{chn}{Colors.white} In {Colors.yellow}{guild}")
    print(f"{Colors.blue}{curtime} {Colors.green}[+] {Colors.red}Created {amount} Channels in{Colors.white}{Colors.yellow} {guild}{Colors.white}")


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
async def serverinfo(ctx):
    if ctx.author != bot.user:
        return
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in guild.members:
        print(member)


@bot.command()
async def massban(ctx):
    guild = ctx.message.guild
    if ctx.author != bot.user:
        return
    for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{Colors.blue}{curtime} {Colors.green}[+] {Colors.green}Succsessfully {Colors.red}Banned {user}{Colors.white}in{Colors.yellow} {guild}{Colors.white}")
        except:
            pass

@bot.command()
async def ghostping(ctx, amount:int, *, message):
    if ctx.author != bot.user:
        return
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message, delete_after=0.1)
        await asyncio.sleep(5.0)
    print(f"{Colors.blue}{curtime} {Colors.green}[+] {Colors.green}Succsessfully {Colors.red}Ghostpinged {message} {Colors.yellow}{amount} times {Colors.white}in{Colors.yellow} {guild}{Colors.white}")

    

# Main Run
while __name__ == '__main__':
    try:
        bot.run(TOKEN, bot=False)
   
    except AttributeError:
        print(f"{Colors.red}[-]{Colors.white} Attribute error, try cheking for misspellings")

    except ModuleNotFoundError:
        print(f"{Colors.red}[-]{Colors.white} Got An import error try following the instructions in https://github.com/DrkTheDon/BlackDC/wiki/Installation-of-BlackDC")
        time.sleep(1)
        quit()

    except discord.errors.LoginFailure:
        print(f"{Colors.purple}TOKEN: {Colors.white}{TOKEN}")
        print(f"{Colors.red}[-]{Colors.white} Improper Token or disabled account.\n{Colors.yellow}NOTE:{Colors.white} If you have any quotes like \" or \' then remove them from your token in ./assets/token.txt")
        time.sleep(1.5)
        quit()

    except KeyboardInterrupt:
        print(f"{Colors.red}[-]{Colors.white} Quitting.")
        time.sleep(0.5)
        clearcmd()
        quit()

    except RuntimeError:
        clearcmd()
        print(f"{Colors.red}[-]{Colors.white} CTRL + C detected, quitting...")
        time.sleep(0.5)
        clearcmd()
        quit()

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound): 
            await ctx.send("Unknown command") 
        
