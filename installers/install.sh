#!/bin/sh

#####################################################
## drkSelfBot (DSM)                                ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
## NOTE: This will install all the dependicies     ##
#####################################################

# Global Variables
RED="\033[0;31m"
YELLOW="\033[0;33m"
GREEN="\033[0;32m"
BLUE="\033[0;36m"

# Main Code
if [ "$(id -u)" -ne 0 ]; then

        echo "${RED}Permission Denied! Try running this with sudo." >&2
        sleep 1.5
        exit 1

fi
clear
echo ${BLUE}"  ____  _____   _____ "
echo ${BLUE}" |  _ \|  __ \ / ____|"
echo ${BLUE}" | |_) | |  | | |     "
echo ${BLUE}" |  _ <| |  | | |     "
echo ${BLUE}" | |_) | |__| | |____ "
echo ${BLUE}" |____/|_____/ \_____|"
echo ${RED}"     Black Discord     "      
sleep 1   
echo ${YELLOW}"\nDependicies Installer for Black Discord. Coded by drk"                                  
sleep 1.5
echo "\n"
echo "${YELLOW}[*] UPDATING SYSTEM."
apt-get -y -qq update 
echo "${RED}\n[*] Installing Packages\n"
pip install discord -qq
echo "${RED}Installed${GREEN} discord ${YELLOW}[1/6]"
pip install colorama -qq
echo "${RED}Installed${GREEN} colorama ${YELLOW}[2/6]"
pip install datetime -qq
echo "${RED}Installed${GREEN} datetime  ${YELLOW}[3/6]"
pip install numpy -qq
echo "${RED}Installed${GREEN} numpy  ${YELLOW}[4/6]"
pip install requests -qq
echo "${RED}Installed${GREEN} requests  ${YELLOW}[5/6]"
pip install discord.py -qq
echo "${RED}Installed${GREEN} discord.py  ${YELLOW}[6/6]\n"

echo "${GREEN}\nInstalled all the dependicies!"
