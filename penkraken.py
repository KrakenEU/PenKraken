#!/usr/bin/env python
import re
import sys
import subprocess
import ipaddress
import nmap
import signal
import penkraken_os_identification as os_identify
import penkraken_port_scanning as port_scanning

# Ctr-C function
def def_handler(sig,frame):
    print("\n\n[+] Saliendo...\n\n")
    sys.exit(1)
#Ctr-C
signal.signal(signal.SIGINT, def_handler)

class Welcome:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def display_welcome_message(self):
        welcome_message = f"\n========================= Welcome to ============================= {self.tool_name}"
        print(welcome_message)

class Menu:
    def __init__(self):
        self.os = ''
        self.ports = ''
        try:
            print("\n[+] What would you like to use:")
            option = input("\n[1] OS Identification\n[2] Port Scanning\n\n[>] Choose an option: ")

            # Os Identification
            if option == '1':
                if os_name != '':
                    print("\n[+] Last OS Identified was " + os_name)
                    again = input("[>] Would you like to identify the OS again? (y/n): ")
                    if 'y' in str(again).lower():
                        self.os_identification()
                    else:
                        print("\n[+] Exiting OS Identification...") 
                else:
                    self.os_identification()

            # Port Scanning
            elif option == '2':
                if ports_discovered != '':
                    print("\n[+] Last scanned ports were: " + ports_discovered)
                    again = input("\n[>] Would you like to scan ports again? (y/n): ")
                    if 'y' in str(again).lower():
                        self.ports_scan()
                    else:
                        print("\n[+] Exiting Port Scanning...") 
                else:
                    self.ports_scan()
    
        except:
            pass

    def os_identification(self):  
        self.os = os_identify.Init()
        
    
    def ports_scan(self):
        self.ports = port_scanning.Init()


if __name__ == "__main__":
    penkraken_welcome = Welcome("""
==================================================================                      
                      ____  __.              __ 
______   ____   ____ |    |/ _|___________  |  | __ ____   ____  
\____ \_/ __ \ /    \|      < \_  __ \__  \ |  |/ // __ \ /    \ 
|  |_> >  ___/|   |  \    |  \ |  | \// __ \|    <\  ___/|   |  \\
|   __/ \___  >___|  /____|__ \|__|  (____  /__|_ \\___  >___|  /
|__|        \/     \/        \/           \/     \/    \/     \/  \n
==================================================================
=================================================================="""
    )
    # Display Welcome message
    penkraken_welcome.display_welcome_message()

    # General Variables
    os_name = ''
    ports_discovered = ''

    # Choose an Option:
    while True:
        penkraken_menu = Menu()

        # Update Variables
        try:
            if penkraken_menu.os != '':
                os_name = penkraken_menu.os
            if penkraken_menu.ports != '': 
                ports_discovered = penkraken_menu.ports
        
        except:
            pass

        cont = input("\n[>] Would you like to perform more actions? (y/n): ")
        while True:
            if 'y' in str(cont).lower():
                break
            elif 'n' in str(cont).lower():
                print("\n[+] Exiting Now...\n[+] Thanks for Using PenKraken!!")
                exit()
            else:
                print("\n[-] That's not an option, try again")



    

 