#!/bin/sh

#####################################################
## drkSelfBot (DSM)                                ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
## NOTE: This will install all the dependicies     ##
#####################################################

# Imports
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
echo ${BLUE}"   _____       _    _____ _______ _____ "
echo ${BLUE}"  |  __ \     | |  |  __ \__   __|_   _|"
echo ${BLUE}"  | |  | |_ __| | _| |__) | | |    | |  "
echo ${BLUE}"  | |  | | '__| |/ /  ___/  | |    | |  "
echo ${BLUE}"  | |__| | |  |   <| |      | |   _| |_ "
echo ${BLUE}"  |_____/|_|  |_|\_\_|      |_|  |_____|"
echo ${RED}"                 Drk's Selfbot           "                                    
sleep 1.5
echo "\n"
echo "${YELLOW}[*] UPDATING SYSTEM."
sleep 1 
apt-get -y -qq update 
