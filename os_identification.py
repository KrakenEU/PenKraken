#!/usr/bin/env python

import re
import sys
import subprocess
import ipaddress
import nmap
import penkraken

# First Option
# Using python-nmap

class Nmap_os:
    def __init__(self,ip_address):
        self.ip_address = str(ip_address)
        self.nm = nmap.PortScanner()
        print(f"{penkraken.colors['green']}\n[+] Checking if target is up...{penkraken.colors['reset']}")
        self.nm.scan(str(self.ip_address), '0')        
        state = self.nm[str(self.ip_address)].state()
        print(f"{penkraken.colors['magenta']}\n[+] Target is {str(state)}{penkraken.colors['reset']}")
        if str(state) == 'up':
            self.os_name = self.osdiscovery()
        else:
            print(f"{penkraken.colors['red']}\n[-] Target seems down{penkraken.colors['reset']}")

    def osdiscovery(self):
        try:
            print(f"\n{penkraken.colors['green']}[+] Searching for OS match (This could take some time...){penkraken.colors['reset']}")
            dump = self.nm.scan(self.ip_address, arguments="-O")
            print(f"{penkraken.colors['magenta']}\n[+] OS Found!{penkraken.colors['reset']}")
            print(f"{penkraken.colors['green']}\n[+] OS info:\n{penkraken.colors['green']}")
            print(dump['scan'][str(self.ip_address)]['osmatch'][0]['osclass'])
            return str(dump['scan'][str(self.ip_address)]['osmatch'][0]['osclass'][0]['osfamily'])

        except:
            print(f"{penkraken.colors['red']}[-] Could not scan OS, are you root?{penkraken.colors['reset']}")



# Second Option:
# Use TTL reference
class TTL:
    def __init__(self,ip_address):
        self.ip_address = ip_address
        self.os_name = self.get_ttl()

    def get_ttl(self):
        try:
            proc = subprocess.Popen(["/bin/ping -c 1 %s" % self.ip_address, ""], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            out = out.split()
            for x in out:
                if 'ttl' in x.decode():
                    ttl = x.decode().split('=')[1]
            ttl_value = int(ttl)
            if ttl_value >= 0 and ttl_value <= 64:
                os_name = "Linux"
            elif ttl_value >= 64 and ttl_value <= 128:
                os_name = "Windows"
            else:
                os_name = "Not found"
            print(f"{penkraken.colors['magenta']}\n%s ({penkraken.colors['red']}ttl{penkraken.colors['magenta']} -> {penkraken.colors['red']}%s{penkraken.colors['magenta']}): {penkraken.colors['red']}%s{penkraken.colors['reset']}" % (self.ip_address, ttl_value, os_name))
            print(f"{penkraken.colors['magenta']}\n[+] Os Found!{penkraken.colors['reset']}")
            return os_name    
        except:
           print(f"{penkraken.colors['red']}\n[-] Error while sending ping command, Target could be blocking ICMP traces \n- Please try Again -\n{penkraken.colors['reset']}")


def Init():
    try:
        ip = input(f"{penkraken.colors['blue']}\n[+] Target IP: {penkraken.colors['reset']}")
        ip_address = ipaddress.ip_address(ip)
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] Nmap OS discovery (Requires Root Privileges)\n[2] TTL OS discovery\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
        if str(x) == '1':
            target = Nmap_os(ip_address)
        elif str(x) == '2':
            target = TTL(ip_address)

        # Display OS:
        print(f"{penkraken.colors['magenta']}\n[+] OS = {penkraken.colors['red']}{target.os_name}{penkraken.colors['reset']}")
        return target.os_name

    except ValueError:
        print(f"{penkraken.colors['red']}[-] Invalid address: %s{penkraken.colors['reset']}")
        sys.exit(1)
    except:
           print(f"{penkraken.colors['red']}\n[-] Exiting OS Scan{penkraken.colors['reset']}")


    

    

