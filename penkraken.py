#!/usr/bin/env python
import re
import sys
import subprocess
import ipaddress
import nmap
import signal
import wafw00f

# Import modules
import modules.os_identification as os_identify
import modules.port_scanning as port_scanning
import modules.waf_detection as waf_detection
import modules.load_balancers as load_balancers
import modules.discovery_tools as discoverytools
import modules.Fuzzing as fuzzing
import modules.exploit_searcher as exp_searcher
import modules.shell_craft as Shellcraft
import modules.OSINT_tools as Osint
import modules.pass_crack as Cracker

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
        self.balancers = ''
        self.discovery = ''
        self.fuzzer = ''
        self.exploits = ''
        self.shells = ''
        self.osint = ''
        self.cracked = ''

        try:
            print(f"{colors['blue']}\n[+] What would you like to use:{colors['reset']}")
            option = input(f"{colors['bright_green']}\n[1] OS Identification\n[2] Port Scanning\n[3] WAF Detectionn\n[4] Load Balancers Scan\n[5] Project Discovery Tools\n[6] Fuzzing Module\n[7] Exploit Searcher\n[8] Shell Crafter\n[9] OSINT CLI Auto Tool\n[10] Password Cracking\n\n{colors['blue']}[>] Choose an option: {colors['reset']}")

            # Os Identification
            if option == '1':
                if os_name != '':
                    print(f"{colors['red']}\n[+] Last OS Identified was: {os_name}")
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
                    print(f"{colors['red']}\n[+] Last scanned ports were: {ports_discovered}")
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
                    print(f"{colors['red']}\n[+] Last WAF scan output was:\n{str(wafs)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to scan for exiting WAFs again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.waf_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting WAF Detection...{colors['reset']}") 
                else:
                    self.waf_scan()

            # Load Balancers
            elif option == '4':
                if balancers != '':
                    print(f"{colors['red']}\n[+] Last Halberd scan output was:\n{str(balancers)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to scan for Load Balancers again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.halberd_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting Halberd Module...{colors['reset']}") 
                else:
                    self.halberd_scan()
            
            # Project Discovery
            elif option == '5':
                if discovery != '':
                    print(f"{colors['red']}\n[+] Last ProjectDiscovery scan output was:\n{str(discovery)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to run scans again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.PDiscovery_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting ProjectDiscovery Module...{colors['reset']}") 
                else:
                    self.PDiscovery_scan()
            
            # Fuzzing module
            elif option == '6':
                if fuzzer != '':
                    print(f"{colors['red']}\n[+] Last FUZZING scan output was:\n{str(fuzzer)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to FUZZ again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.fuzzing_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting FUZZING Module...{colors['reset']}") 
                else:
                    self.fuzzing_scan()
            
            # Exploit Searcher
            elif option == '7':
                if exploits != '' and exploits!=None:
                    print(f"{colors['red']}\n[+] Last Exploit Searcher scan output was:\n{str(exploits)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to search for exploits again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.exploit_search()
                    else:
                        print(f"{colors['red']}\n[+] Exiting Exploit Searcher Module...{colors['reset']}") 
                else:
                    self.exploit_search()

            # Shell Crafter
            elif option == '8':
                if shells != '':
                    print(f"{colors['red']}\n[+] Last Shell Crafted was:\n{str(shells)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to craft a shell again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.shell_crafter()
                    else:
                        print(f"{colors['red']}\n[+] Exiting ShellCrafter Module...{colors['reset']}") 
                else:
                    self.shell_crafter()
            
            # Osint CLI
            elif option == '9':
                if osint != '':
                    print(f"{colors['red']}\n[+] Last OSINT Scan was:\n{str(osint)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to use the OSINT tool again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.osint_scan()
                    else:
                        print(f"{colors['red']}\n[+] Exiting OSINT Module...{colors['reset']}") 
                else:
                    self.osint_scan()
            
            # Password Cracking
            elif option == '10':
                if cracked != '':
                    print(f"{colors['red']}\n[+] Last Password Cracking was:\n{str(cracked)}")
                    again = input(f"{colors['blue']}\n[>] Would you like to use the Password Cracking tool again? (y/n): {colors['reset']}")
                    if 'y' in str(again).lower():
                        self.cracking()
                    else:
                        print(f"{colors['red']}\n[+] Exiting Password Cracking Module...{colors['reset']}") 
                else:
                    self.cracking()

        except:
            print("Invalid option")

# Calling Independent Modules
    def os_identification(self):  
        self.os = os_identify.Init()
        
    def ports_scan(self):
        self.ports = port_scanning.Init()
    
    def waf_scan(self):
        self.wafs = waf_detection.Init()
    
    def halberd_scan(self):
        self.balancers = load_balancers.Init()

    def PDiscovery_scan(self):
        self.discovery = discoverytools.Init()
    
    def fuzzing_scan(self):
        self.fuzzer = fuzzing.Init()

    def exploit_search(self):
        self.exploits = exp_searcher.Init()
    
    def shell_crafter(self):
        self.shells = Shellcraft.Init()
    
    def osint_scan(self):
        self.osint = Osint.Init()

    def cracking(self):
        self.cracked = Cracker.Init()

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
    balancers = ''
    discovery = ''
    fuzzer = ''
    exploits = ''
    shells = ''
    osint = ''
    cracked = ''
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
            if penkraken_menu.balancers != '':
                balancers = penkraken_menu.balancers
            if penkraken_menu.discovery != '':
                discovery = penkraken_menu.discovery
            if penkraken_menu.fuzzer != '':
                fuzzer = penkraken_menu.fuzzer
            if penkraken_menu.exploits != '':
                exploits = penkraken_menu.exploits
            if penkraken_menu.shells != '':
                shells = penkraken_menu.shells
            if penkraken_menu.osint != '':
                osint = penkraken_menu.osint
            if penkraken_menu.cracked != '':
                cracked = penkraken_menu.cracked

        except:
            pass

        # Perform more actions
        
        while True:
            cont = input(f"{colors['blue']}\n[>] Would you like to perform more actions? (y/n): {colors['reset']}")
            if 'y' in str(cont).lower():
                break
            elif 'n' in str(cont).lower():
                print(f"{colors['red']}\n[+] Exiting Now...\n[+] Thanks for Using PenKraken!!{colors['reset']}")
                exit()
            else:
                print(f"{colors['red']}\n[-] That's not an option, try again{colors['reset']}")

  

 
