#!/usr/bin/env python
import re
import sys
import subprocess
import ipaddress
import nmap

class Welcome:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def display_welcome_message(self):
        welcome_message = f"\n========================= Welcome to ============================= {self.tool_name}"
        print(welcome_message)

class Options:
    def __init__(self):
        print("\nWhat would you like to use:")
        option = input("\n[1] Os Identification: ")

        # Os Identification
        if option == '1':
            self.os_identification()

    def os_identification(self):
        import penkraken_os_identification as os_identify
        os_identify.Init()

    


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

    # Choose an Option:
    penkraken_options = Options()



    

