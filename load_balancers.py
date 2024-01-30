#!/usr/bin/env python
import wafw00f
import subprocess
import penkraken
import time

class Halberd:

    def __init__(self, target='', filename=''):
        self.target = target
        self.filename = filename
        self.load_balancer_info = []
        self.scan()

    def scan(self):
        try:
            p = 10 # Threads
            if self.target != '':
                try:
                    print(f"{penkraken.colors['green']}\n[+] Starting Halberd scan towards a single target...{penkraken.colors['reset']}")
                    # run the command
                    output = subprocess.check_output(f"halberd -p {str(p)} {str(self.target)}", shell=True)
                    print(f"{penkraken.colors['green']}\n[+] Halberd output:\n{penkraken.colors['reset']}")
                    # Print and save
                    for x in str(output.decode()).split('\n'):
                        print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                        self.load_balancer_info.append(x)
                except:
                    print(f"{penkraken.colors['red']}[-] Invalid target '{self.target}' {penkraken.colors['reset']}")

            elif self.filename != '':
                try:
                    print(f"{penkraken.colors['green']}\n[+] Starting Halberd scan given a targets file...{penkraken.colors['reset']}")
                    # run the command
                    output = subprocess.check_output(f"halberd -p {str(p)} -u {str(self.filename)} -t 5", shell=True)
                    print(f"{penkraken.colors['green']}\n[+] Halberd output:\n{penkraken.colors['reset']}")
                    # Print and save
                    for x in str(output.decode()).split('\n'):
                        print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                        self.load_balancer_info.append(x)
                except:
                    print(f"{penkraken.colors['red']}[-] file '{self.filename}' was not found{penkraken.colors['reset']}")
            else:
                print(f"{penkraken.colors['red']}[-] No action was done, specify a valid target or filename with a list of targets{penkraken.colors['reset']}")
                exit()
            
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open('Halberd-results.txt', 'w')
                file.write(str(output.decode()))
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to 'Halberd-results.txt'\n{penkraken.colors['reset']}")
        
        except:
            print(f"{penkraken.colors['red']}\n[-] Error encountered while searching for load balancers using halberd{penkraken.colors['reset']}")



def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to {penkraken.colors['red']}Halberd{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-/:_'
        
        multiple = input(f"{penkraken.colors['green']}[1] Scan file with targets\n[2] Scan single target\n\n{penkraken.colors['blue']}[>] Choose option (1-2): {penkraken.colors['reset']}")
        if int(multiple) == 1:
            check = 0
            while check == 0:
                filename = input(f"{penkraken.colors['blue']}\n[>] Name of the file with targets (file content: line1 = https://target1.com ; line2 = https://target2.com ...) : {penkraken.colors['reset']}")
                for x in filename:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid filename{penkraken.colors['reset']}")
                        check = 0
            target = Halberd(filename = filename)

        else:
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

            target = Halberd(target=target)

        out = ''
        for x in target.load_balancer_info:
            out += x + '\n'
        return out

    except:
            print(f"{penkraken.colors['red']}\n[-] Exiting Halberd Scan{penkraken.colors['reset']}")

