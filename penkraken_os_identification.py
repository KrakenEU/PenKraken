#!/usr/bin/env python

import re
import sys
import subprocess
import ipaddress
import nmap

# First Option
# Using python-nmap

class Nmap_os:
    def __init__(self,ip_address):
        self.ip_address = str(ip_address)
        self.nm = nmap.PortScanner()
        print("\n[+] Checking if target is up...")
        self.nm.scan(str(self.ip_address), '0')        
        state = self.nm[str(self.ip_address)].state()
        print("\n[+] Target is " + str(state))
        if str(state) == 'up':
            self.os_name = self.osdiscovery()
        else:
            print("\n[-] Target seems down")

    def osdiscovery(self):
        try:
            print('\n[+] Searching for OS match (This could take some time...)')
            dump = self.nm.scan(self.ip_address, arguments="-O")
            print('\n[+] OS Found!')
            print('\n[+] OS info:\n')
            print(dump['scan'][str(self.ip_address)]['osmatch'][0]['osclass'])
            return str(dump['scan'][str(self.ip_address)]['osmatch'][0]['osclass'][0]['osfamily'])
        except:
            print("[-] Could not scan OS, are you root?")



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
            print("\n%s (ttl -> %s): %s" % (self.ip_address, ttl_value, os_name))
            print("\n[+] Os Found!")
            return os_name    
        except:
           print("\n[-] Error while sending ping command, Target could be blocking ICMP traces \n- Please try Again -\n")

class Init:
    try:
        ip = input("\n[+] Target IP: ")
        ip_address = ipaddress.ip_address(ip)
        while True:
            x = input("\n[1] Nmap OS discovery (Requires Root Privileges)\n[2] TTL OS discovery\n\n[+] Choose option: ")
            if str(x) != '1' and str(x) != '2':
                print("\n[-] Invalid Option")
            else:
                break
        if str(x) == '1':
            target = Nmap_os(ip_address)
            os_name = target.os_name
        elif str(x) == '2':
            #Second Option  
            target = TTL(ip_address)

        # Display OS:
        print('\n[+] OS = ' + target.os_name)

    except ValueError:
        print('[-] Invalid address: %s' % sys.argv[1])
        sys.exit(1)
    except:
        print("\n[-] Exiting Program")


    

    

