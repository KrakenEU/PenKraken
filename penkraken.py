#!/usr/bin/env python
import re
import sys
import subprocess
import ipaddress
import nmap
import signal
import wafw00f
import time

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
        

class Enumeration:
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
            print(f"{colors['red']}[-] Invalid option{colors['reset']}")

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



def RecoverFile(name):
    dic = {}
    with open(name, 'r') as file:
            file_content = file.read()
    # Patterns
    host_pattern = re.compile(r'Host: ([\d.]+)')
    osint_pattern = re.compile(r'OSINT')
    metadata_pattern = re.compile(r'Metadata:((?:(?!\n\n).)*)', re.DOTALL)
    mails_pattern = re.compile(r'Mails:((?:(?!\n\n\n\n).)*)', re.DOTALL)
    domains_pattern = re.compile(r'Domains:((?:(?!\n\n).)*)', re.DOTALL)
    usernames_pattern = re.compile(r'Usernames:((?:(?!\n\n).)*)', re.DOTALL)
    hash_cracking_pattern = re.compile(r'Hash Cracking((?:(?!\n\n).)*)', re.DOTALL)
    os_pattern = re.compile(r'OS: (.+)')
    ports_pattern = re.compile(r'Oppened Ports:((?:(?!\n\n).)*)', re.DOTALL)
    nmap_pattern = re.compile(r'Nmap Scan:((?:(?!\n\n).)*)', re.DOTALL)
    fuzzing_pattern = re.compile(r'Fuzzing:((?:(?!\n\n).)*)', re.DOTALL)
    wafs_pattern = re.compile(r'WAFS: (.+)')
    balancers_pattern = re.compile(r'Load Balancers:((?:(?!\n\n\n\n).)*)', re.DOTALL)

    
    entries = re.split(r'(?=Host:)', file_content)
    # Process each entry
    for entry in entries: 

        # OSINT part
        osint_match = osint_pattern.search(entry)
        
        if osint_match:
            osint_key = osint_match.group(0).strip()
            metadata_match = metadata_pattern.search(entry)
            mails_match = mails_pattern.search(entry)
            usernames_match = usernames_pattern.search(entry)
            domains_match = domains_pattern.search(entry)
            entry_dict = {}

            if metadata_match:
                entry_dict['Metadata'] = metadata_match.group(1).strip() + '\n'

            if mails_match:
                entry_dict['Mails'] = mails_match.group(1).strip() + '\n'

            if usernames_match:
                entry_dict['Usernames'] = usernames_match.group(1).strip() + '\n'

            if domains_match:
                entry_dict['Domains'] = domains_match.group(1).strip() + '\n'

            dic[osint_key] = entry_dict

        entry_dict = {}

        # Pass Cracking Part

        hash_match = hash_cracking_pattern.search(entry)

        if hash_match:
            hash_key = hash_match.group(1).strip()
            hash_val, password = hash_key.split(': ', 1)
            sub_dict = {hash_val: password+ '\n'}
            dic['Hash Cracking'] = sub_dict


        # Hosts Part

        host_match = host_pattern.search(entry)

        if host_match:

            host_key = host_match.group(0).strip()
            
            os_match = os_pattern.search(entry)
            if os_match:
                entry_dict['OS'] = os_match.group(1).strip() + '\n'

            ports_match = ports_pattern.search(entry)
            if ports_match:
                entry_dict['Oppened Ports'] = ports_match.group(1) + '\n'
            
            nmap_match = nmap_pattern.search(entry)
            if nmap_match:
                entry_dict['Nmap Scan'] = nmap_match.group(1) + '\n'

            wafs_match = wafs_pattern.search(entry)
            if wafs_match:
                entry_dict['WAFS'] = wafs_match.group(1).strip() +'\n'
            
            fuzzing_match = fuzzing_pattern.search(entry)
            if fuzzing_match:
                entry_dict['Fuzzing'] = fuzzing_match.group(1).strip()
            
            balancers_match = balancers_pattern.search(entry)
            if balancers_match:
                entry_dict['Load Balancers'] = balancers_match.group(1).strip()

            dic[host_key] = entry_dict
    

    return dic   


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

    while True:
        print(f"{colors['green']}\n[+] OPENING PENKRAKEN PANEL! {colors['reset']}")
        option = input(f"{colors['bright_green']}\n[1] Recover file from other session to continue\n[2] Jump to modules\n\n{colors['blue']}[>] Choose an option: {colors['reset']}")
        if option != '1' and option != '2':
            print(f"{colors['green']}\n[-] Invalid Option! {colors['reset']}")
        else:
            break

    # Enumeration Variables
    Results_dic = {}
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

    # Recover File
    if option == '1':
        name = input(f"{colors['blue']}\n[>] Name of the Recoverable File: {colors['reset']}")

        # Read content from the file and update variables
        Results_dic = RecoverFile(name)
              
        print(f"{colors['green']}\n[+] Document Loaded to {colors['red']}PenKraken {colors['green']}!\n[+] Loading Contents...{colors['reset']}")
        time.sleep(1)
        process = subprocess.Popen(f'cat {name}',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
        while True:
            out = process.stdout.readline()
            time.sleep(0.025)
            if out == '' and process.poll() is not None:
                break
            else:
                if out:
                    print(out.strip())
        print(f"{colors['green']}\n[+] Done! ")
    
    # Choose an Option:
    while True:
        penkraken_enum = Enumeration()

        # Update Enumeration Variables
        try:
            if penkraken_enum.os != '':
                os_name = penkraken_enum.os[1]
                if f'Host: {penkraken_enum.os[0]}' in Results_dic:
                    Results_dic[f'Host: {penkraken_enum.os[0]}'].update({'OS' : penkraken_enum.os[1]+'\n'})
                else:
                    Results_dic[f'Host: {penkraken_enum.os[0]}'] = {}
                    Results_dic[f'Host: {penkraken_enum.os[0]}']['OS'] = penkraken_enum.os[1]+'\n'

            if penkraken_enum.ports != '': 
                ports_discovered = penkraken_enum.ports[1]
                if f'Host: {penkraken_enum.ports[0]}' in Results_dic:
                    Results_dic[f'Host: {penkraken_enum.ports[0]}'].update({'Oppened Ports' : penkraken_enum.ports[1]+'\n'})
                    Results_dic[f'Host: {penkraken_enum.ports[0]}'].update({'Nmap Scan' : penkraken_enum.ports[2]+'\n'})

                else:
                    Results_dic[f'Host: {penkraken_enum.ports[0]}'] = {}
                    Results_dic[f'Host: {penkraken_enum.ports[0]}']['Oppened Ports'] = penkraken_enum.ports[1]+'\n'
                    Results_dic[f'Host: {penkraken_enum.ports[0]}']['Nmap Scan'] = penkraken_enum.ports[2]+'\n'


            if penkraken_enum.wafs != '':
                wafs = penkraken_enum.wafs
                if f'Host: {penkraken_enum.wafs[0]}' in Results_dic:
                    Results_dic[f'Host: {penkraken_enum.wafs[0]}'].update({'WAFS' : penkraken_enum.wafs[1].strip()+'\n'})
                else:
                    Results_dic[f'Host: {penkraken_enum.wafs[0]}'] = {}
                    Results_dic[f'Host: {penkraken_enum.wafs[0]}']['WAFS'] = penkraken_enum.wafs[1].strip()+'\n'

            if penkraken_enum.balancers != '':
                balancers = penkraken_enum.balancers[1]
                if f'Host: {penkraken_enum.balancers[0]}' in Results_dic:
                    Results_dic[f'Host: {penkraken_enum.balancers[0]}'].update({'Load Balancers' : penkraken_enum.balancers[1].strip()+'\n\n'})
                else:
                    Results_dic[f'Host: {penkraken_enum.balancers[0]}'] = {}
                    Results_dic[f'Host: {penkraken_enum.balancers[0]}']['Load Balancers'] = penkraken_enum.balancers[1].strip()+'\n\n'

            if penkraken_enum.discovery != '':
                try:
                    discovery = penkraken_enum.discovery[1]
                    if f'Host: {penkraken_enum.discovery[0]}' in Results_dic:
                        Results_dic[f'Host: {penkraken_enum.balancers[0]}'].update({'Nuclei' : penkraken_enum.balancers[1].strip()+'\n'})
                    else:
                        Results_dic[f'Host: {penkraken_enum.discovery[0]}'] = {}
                        Results_dic[f'Host: {penkraken_enum.balancers[0]}']['Nuclei'] = penkraken_enum.balancers[1].strip()+'\n'
                except:
                    discovery = penkraken_enum.discovery

            if penkraken_enum.fuzzer != '':
                fuzzer = penkraken_enum.fuzzer[1]
                if f'Host: {penkraken_enum.fuzzer[0]}' in Results_dic:
                    Results_dic[f'Host: {penkraken_enum.fuzzer[0]}'].update({f'Fuzzing-{penkraken_enum.fuzzer[2]}' :penkraken_enum.fuzzer[1].strip()+'\n'})
                else:
                    Results_dic[f'Host: {penkraken_enum.fuzzer[0]}'] = {}
                    Results_dic[f'Host: {penkraken_enum.fuzzer[0]}'][f'Fuzzing'] = penkraken_enum.fuzzer[1].strip()+'\n'

            if penkraken_enum.exploits != '':
                exploits = penkraken_enum.exploits

            if penkraken_enum.shells != '':
                shells = penkraken_enum.shells

            if penkraken_enum.osint != '':
                osint = penkraken_enum.osint[1]
                if f'OSINT' in Results_dic:
                    Results_dic[f'OSINT'].update({penkraken_enum.osint[0] : penkraken_enum.osint[1]})
                else:
                    Results_dic[f'OSINT'] = {}
                    Results_dic[f'OSINT'][penkraken_enum.osint[0]] = penkraken_enum.osint[1]

            if penkraken_enum.cracked != '':
                cracked = penkraken_enum.cracked
                hash_val = penkraken_enum.cracked.split(':')[-2].replace(' ','')
                pattern = re.compile(r'\x1b\[[0-9;]*m')
                hash_val = re.sub(pattern, '', hash_val)
                if 'Hash Cracking' in Results_dic:
                    Results_dic['Hash Cracking'].update({hash_val : penkraken_enum.cracked.split(':')[1].split('\n')[0]+'\n'})
                else:
                    Results_dic['Hash Cracking'] = {}
                    Results_dic['Hash Cracking'][hash_val] = penkraken_enum.cracked.split(':')[-1].split('\n')[0]+'\n'



        except:
            pass

        # Export Results to a recoverable file
        #try:
        # Write New Data
        
        #except:
        #    print('Could Not write')
                    

        print(Results_dic)

        # Perform more actions

        while True:
            cont = input(f"{colors['blue']}\n[>] Would you like to perform more actions? (y/n): {colors['reset']}")
            if 'y' in str(cont).lower():
                break
            elif 'n' in str(cont).lower():
                input_name = input(f"{colors['blue']}\n[>] Name of the Resulting report file (Default = PenKraken-Report.txt): {colors['reset']}")
                if input_name != '':
                    name = input_name
                else:
                    name = 'PenKraken-Report.txt'
                file = open(name, 'w')
                write = ''
                for k,v in Results_dic.items():
                    if k.split()[-1] not in write:
                        write+=f"{colors['red']}"+k+f"\n{colors['reset']}"
                    for s,i in v.items():
                        write+=f"{colors['green']}"+s+f": {colors['magenta']}"+i+f"\n{colors['reset']}"

                file.write(write)

                print(f"{colors['red']}\n[+] Exiting Now...\n[+] Thanks for Using PenKraken!!{colors['reset']}")
                exit()
            else:
                print(f"{colors['red']}\n[-] That's not an option, try again{colors['reset']}")


