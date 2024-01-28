#!/usr/bin/env python
import re
import sys
import subprocess
import ipaddress
import nmap
import signal
import os_identification as os_identify
import port_scanning as port_scanning
import waf_detection as waf_detection

colors = {
  'reset': '\x1b[0m',
  'bold': '\x1b[1m',
  'italic': '\x1b[3m',
  'underline': '\x1b[4m',
  'inverse': '\x1b[7m',

  'black': '\x1b[30m',
  'red': '\x1b[31m',
  'green': '\x1b[32m',
  'yellow': '\x1b[33m',
  'blue': '\x1b[34m',
  'magenta': '\x1b[35m',
  'cyan': '\x1b[36m',
  'white': '\x1b[37m',
  'gray': '\x1b[90m',
  'bright_red': '\x1b[91m',
  'bright_green': '\x1b[92m',
  'bright_yellow': '\x1b[93m',
  'bright_blue': '\x1b[94m',
  'bright_magenta': '\x1b[95m',
  'bright_cyan': '\x1b[96m',
  'bright_white': '\x1b[97m',

  'bg_black': '\x1b[40m',
  'bg_red': '\x1b[41m',
  'bg_green': '\x1b[42m',
  'bg_yellow': '\x1b[43m',
  'bg_blue': '\x1b[44m',
  'bg_magenta': '\x1b[45m',
  'bg_cyan': '\x1b[46m',
  'bg_white': '\x1b[47m',
  'bg_gray': '\x1b[100m',
  'bg_bright_red': '\x1b[101m',
  'bg_bright_green': '\x1b[102m',
  'bg_bright_yellow': '\x1b[103m',
  'bg_bright_blue': '\x1b[104m',
  'bg_bright_magenta': '\x1b[105m',
  'bg_bright_cyan': '\x1b[106m',
  'bg_bright_white': '\x1b[107m'
}

# Ctr-C function
def def_handler(sig,frame):
    print(f"{colors['red']}\n\n[+] Exiting...\n\n{colors['reset']}")
    sys.exit(1)
#Ctr-C
signal.signal(signal.SIGINT, def_handler)

class Welcome:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def display_welcome_message(self):
        welcome_message = f"{colors['blue']}\n========================= Welcome to ============================={colors['bright_green']}{self.tool_name}{colors['reset']}"
        print(welcome_message)

class Menu:
    def __init__(self):
        self.os = ''
        self.ports = ''
        self.wafs = ''
        try:
            print(f"{colors['blue']}\n[+] What would you like to use:{colors['reset']}")
            option = input(f"{colors['bright_green']}\n[1] OS Identification\n[2] Port Scanning\n[3] WAF Detection\n\n{colors['blue']}[>] Choose an option: {colors['reset']}")

            # Os Identification
            if option == '1':
                if os_name != '':
                    print(f"{colors['red']}\n[+] Last OS Identified was: {os_name}{colors['reset']}")
                    again = input(f"{colors['blue']}[>] Would you like to identify the OS again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.os_identification()
                    else:
                        print(f"{colors['bright_red']}\n[+] Exiting OS Identification...{colors['reset']}") 
                else:
                    self.os_identification()

            # Port Scanning
            elif option == '2':
                if ports_discovered != '':
                    print(f"{colors['red']}\n[+] Last scanned ports were: {ports_discovered} {colors['reset']}")
                    again = input(f"{colors['blue']}\n[>] Would you like to scan ports again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.ports_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting Port Scanning...{colors['reset']}") 
                else:
                    self.ports_scan()
            
            # WAF Detection
            elif option == '3':
                if wafs != '':
                    print(f"{colors['red']}\n[+] Last WAF scan output was:\n{str(wafs)}{colors['reset']}")
                    again = input(f"{colors['blue']}\n[>] Would you like to scan for exiting WAFs again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.waf_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting WAF Detection...{colors['reset']}") 
                else:
                    self.waf_scan()
    
        except:
            print("Invalid option")
# Calling Independent Modules
    def os_identification(self):  
        self.os = os_identify.Init()
        
    def ports_scan(self):
        self.ports = port_scanning.Init()
    
    def waf_scan(self):
        self.wafs = waf_detection.Init()


if __name__ == "__main__":
    penkraken_welcome = Welcome(f"""
==================================================================                      
                      ____  __.              __ 
______   ____   ____ |    |/ _|___________  |  | __ ____   ____  
\____ \_/ __ \ /    \|      < \_  __ \__  \ |  |/ // __ \ /    \ 
|  |_> >  ___/|   |  \    |  \ |  | \// __ \|    <\  ___/|   |  \\
|   __/ \___  >___|  /____|__ \|__|  (____  /__|_ \\___  >___|  /
|__|        \/     \/        \/           \/     \/    \/     \/  \n
==================================================================
{colors['blue']}=================================================================={colors['reset']}"""
    )
    # Display Welcome message
    penkraken_welcome.display_welcome_message()

    # General Variables
    os_name = ''
    ports_discovered = ''
    wafs = ''

    # Choose an Option:
    while True:
        penkraken_menu = Menu()

        # Update Variables
        try:
            if penkraken_menu.os != '':
                os_name = penkraken_menu.os
            if penkraken_menu.ports != '': 
                ports_discovered = penkraken_menu.ports
            if penkraken_menu.wafs != '':
                wafs = penkraken_menu.wafs
        
        except:
            pass

        # Perform more actions
        cont = input(f"{colors['blue']}\n[>] Would you like to perform more actions? (y/n): {colors['reset']}")
        while True:
            if 'y' in str(cont).lower():
                break
            elif 'n' in str(cont).lower():
                print(f"{colors['red']}\n[+] Exiting Now...\n[+] Thanks for Using PenKraken!!{colors['reset']}")
                exit()
            else:
                print(f"{colors['red']}\n[-] That's not an option, try again{colors['reset']}")



    

 