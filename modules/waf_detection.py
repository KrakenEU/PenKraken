#!/usr/bin/env python
import wafw00f
import subprocess
import sys
sys.path.append('../')
import penkraken

class wafw00f:
    
    def __init__(self, target):
        self.target = target
        self.waf_detected = []
        self.scan()
    
    def scan(self):
        op = ''
        try:
            options = input(f"{penkraken.colors['blue']}\n[>] Select Scann options:\n\n{penkraken.colors['green']}[1] Check for all available WAFs on the list\n[2] Just run\n\n{penkraken.colors['blue']}[>] Select your scan option (1-2): {penkraken.colors['reset']}")
            if int(options) > 0 and int(options) < 3:
                if int(options) == 1:
                    op = '-a '
            else:
                raise Exception("Invalid Options detected")

            print(f"{penkraken.colors['blue']}\n[+] Starting WAF scan...{penkraken.colors['reset']}")
            output = subprocess.check_output("wafw00f "+str(op)+self.target, shell=True)
            check = 0
            for o in output.decode().split('\n'):
                if 'behind' in o:
                    self.waf_detected.append(o)
                    print(o)
                    check += 1
            if check == 0:
                print(f"{penkraken.colors['red']}\n[~] No WAFs were detected{penkraken.colors['reset']}")
        
        except:
            print(f"{penkraken.colors['red']}\n[-] Error encountered while searching for wafs{penkraken.colors['reset']}")

def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to {penkraken.colors['red']}wafw00f{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_'
        check = 0
        while check == 0:
            target = input(f"{penkraken.colors['blue']}\n[>] Select your target to be scanned : {penkraken.colors['reset']}")
            for x in target:
                if str(x) in valid:
                    check = 1
                    continue
                else:
                    print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                    check = 0
                    break
    
        target = wafw00f(target)
        out = ''
        for x in target.waf_detected:
            out += x + '\n'
        return out

    except:
            print(f"{penkraken.colors['red']}\n[-] Exiting WAFs Scan{penkraken.colors['reset']}")
