#!/usr/bin/env python

import subprocess
import penkraken

class httpx:
    def __init__(self):
        self.results = []
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] Single Target Scan\n[2] Multiple Target Scan\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
        if x == '1':
            self.single_target()
        else:
            self.file_scan()
        try:
            # write Output to a file
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open('Httpx-results.txt', 'w')
                content = ''.join(str(x)+'\n' for x in self.results)
                file.write(content)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to {penkraken.colors['magenta']}'Httpx-results.txt'\n{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Error while saving output to file{penkraken.colors['reset']}")
            
    def single_target(self):
        try:
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            check = 0
            while check == 0:
                t = input(f"{penkraken.colors['blue']}\n[>] Select target URL : {penkraken.colors['reset']}")
                for x in t:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                        check = 0
                        break

            # run command
            print(f"{penkraken.colors['blue']}\n[+] Starting httpx scan against {penkraken.colors['magenta']}{t} {penkraken.colors['reset']}")
            output = subprocess.check_output(f"httpx -status-code -title -tech-detect -u {t}", shell=True)
            # print and save results
            for x in str(output.decode()).split('\n'):
                print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                self.results.append(x)

        except:
            print(f"{penkraken.colors['red']} Error encountered in httpx Single Scan {penkraken.colors['reset']}")

    def file_scan(self):
        try:
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            check = 0
            while check == 0:
                t = input(f"{penkraken.colors['blue']}\n[>] Select targets file : {penkraken.colors['reset']}")
                for x in t:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                        check = 0
                        break

            # run command
            print(f"{penkraken.colors['blue']}\n[+] Starting httpx scan against {penkraken.colors['magenta']}{t} {penkraken.colors['reset']}")
            output = subprocess.check_output(f"httpx -status-code -title -tech-detect -list {t}", shell=True)
            # print and save results
            for x in str(output.decode()).split('\n'):
                print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                self.results.append(x)


        except:
            print(f"{penkraken.colors['red']} Error encountered in httpx Multi Scan {penkraken.colors['reset']}")
        



class subfinder:
    def __init__(self):
        self.results = [] 
        self.sub_scan()
        try:
            # write Output to a file
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open('Subfinder-results.txt', 'w')
                content = ''.join(str(x)+'\n' for x in self.results)
                file.write(content)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to {penkraken.colors['magenta']}'Subfinder-results.txt'\n{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Error while saving output to file{penkraken.colors['reset']}")
            
    def sub_scan(self):
        try:
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            check = 0
            while check == 0:
                t = input(f"{penkraken.colors['blue']}\n[>] Select target domain (example.com) : {penkraken.colors['reset']}")
                for x in t:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                        check = 0
                        break

            # run command
            print(f"{penkraken.colors['blue']}\n[+] Starting subfinder scan against {penkraken.colors['magenta']}{t} {penkraken.colors['reset']}")
            output = subprocess.check_output(f"subfinder -d {t}", shell=True)
            # print and save results
            for x in str(output.decode()).split('\n'):
                print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                self.results.append(x)

        except:
            print(f"{penkraken.colors['red']} Error encountered in Subfinder Scan {penkraken.colors['reset']}")

        
class nuclei:
    def __init__(self):
        self.results = []
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] Custom Template Scan\n[2] Default Scan (Single Target - Time Consuming)\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
        if x == '1':
            self.template_scan()
        else:
            self.nuclei_scan()
        
        try:
            # write Output to a file
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open('Nuclei-results.txt', 'w')
                content = ''.join(str(x)+'\n' for x in self.results)
                file.write(content)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to {penkraken.colors['magenta']}'Nuclei-results.txt'\n{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Error while saving output to file{penkraken.colors['reset']}")

    # Custom Template       
    def template_scan(self):
        try:
            print(f"{penkraken.colors['blue']}[+] Nuclei templates can be found on: {penkraken.colors['magenta']} https://cloud.projectdiscovery.io/templates {penkraken.colors['reset']}")
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            while True:
                x = input(f"{penkraken.colors['green']}\n[1] Single Target Scan\n[2] Multiple Target Scan\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
                if str(x) != '1' and str(x) != '2':
                    print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
                else:
                    break
            if x == '1':
                # take target
                check = 0
                while check == 0:
                    targ = input(f"{penkraken.colors['blue']}\n[>] Select target URL (example.com) : {penkraken.colors['reset']}")
                    for x in targ:
                        if str(x) in valid:
                            check = 1
                            continue
                        else:
                            print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                            check = 0
                            break
                # take templates folder
                check2 = 0
                while check2 == 0:
                    temp = input(f"{penkraken.colors['blue']}\n[>] Select template folder: {penkraken.colors['reset']}")
                    for x in temp:
                        if str(x) in valid:
                            check2 = 1
                            continue
                        else:
                            print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                            check2 = 0
                            break
                            
                # run command
                print(f"{penkraken.colors['blue']}\n[+] Starting Nuclei scan against {penkraken.colors['magenta']}{targ} {penkraken.colors['blue']}with templates in {penkraken.colors['magenta']}{temp}/ {penkraken.colors['reset']}")
                command = f"nuclei -u {targ} -t {temp}/"
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                while True:
                    salida = process.stdout.readline()
                    if salida == '' and process.poll() is not None:
                        break
                    if salida:
                        print(salida.strip())
                        self.results.append(salida.strip())
            else:
                # take filename
                check = 0
                while check == 0:
                    f = input(f"{penkraken.colors['blue']}\n[>] Select targets file : {penkraken.colors['reset']}")
                    for x in f:
                        if str(x) in valid:
                            check = 1
                            continue
                        else:
                            print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                            check = 0
                            break
                # take templates folder
                check = 0
                while check == 0:
                    temp = input(f"{penkraken.colors['blue']}\n[>] Select template folder: {penkraken.colors['reset']}")
                    for x in temp:
                        if str(x) in valid:
                            check = 1
                            continue
                        else:
                            print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                            check = 0
                            break 
                # run command
                print(f"{penkraken.colors['blue']}\n[+] Starting Nuclei scan against {penkraken.colors['magenta']}{f} {penkraken.colors['blue']}with templates in {penkraken.colors['magenta']}{temp}/ {penkraken.colors['reset']}")
                command = f"nuclei -list {f} -t {temp}/"
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                while True:
                    salida = process.stdout.readline()
                    if salida == '' and process.poll() is not None:
                        break
                    if salida:
                        print(salida.strip())
                        self.results.append(salida.strip())

        except:
            print(f"{penkraken.colors['red']} Error encountered in Subfinder Scan {penkraken.colors['reset']}")
            
    #Default Scan

    def nuclei_scan(self):
        try:
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            check = 0
            while check == 0:
                t = input(f"{penkraken.colors['blue']}\n[>] Select target URL (example.com) : {penkraken.colors['reset']}")
                for x in t:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                        check = 0
                        break
            command = f"nuclei -u {t}"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
            while True:
                salida = process.stdout.readline()
                if salida == '' and process.poll() is not None:
                    break
                if salida:
                    print(salida.strip())
                    self.results.append(salida.strip())
            

        except:
            print(f"{penkraken.colors['red']} Error encountered in Nuclei Scan {penkraken.colors['reset']}")

class autoscan:
    def __init__(self):
        self.results = []
        self.auto_scan()
        try:
            # write Output to a file
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open('Autoscan-results.txt', 'w')
                content = ''.join(str(x)+'\n' for x in self.results)
                file.write(content)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to {penkraken.colors['magenta']}'Autoscan-results.txt'\n{penkraken.colors['reset']}")
        except:
            print(f"\n{penkraken.colors['red']}[-] Error while saving output to file{penkraken.colors['reset']}")
            
    def auto_scan(self):
        try:
            valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_#?'
            check = 0
            while check == 0:
                t = input(f"{penkraken.colors['blue']}\n[>] Select target domain (example.com) : {penkraken.colors['reset']}")
                for x in t:
                    if str(x) in valid:
                        check = 1
                        continue
                    else:
                        print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                        check = 0
                        break

            # run command
            print(f"{penkraken.colors['blue']}\n[+] Triggering auto scan against {penkraken.colors['magenta']}{t}{penkraken.colors['reset']}")
            output = subprocess.check_output(f"subfinder -d {t} -o {t}-urls.txt | httpx -status-code -title -tech-detect", shell=True)
            print(f"{penkraken.colors['blue']}\n[+] Results were saved into {penkraken.colors['magenta']}{t}-urls.txt{penkraken.colors['blue']}{penkraken.colors['reset']}")
            for x in str(output.decode()).split('\n'):
                print(f"{penkraken.colors['magenta']} {x} {penkraken.colors['reset']}")
                self.results.append(x)
            print(f"{penkraken.colors['blue']}\n[+] Running nuclei http scan on {penkraken.colors['magenta']}{t}-urls.txt{penkraken.colors['blue']} (This could take A LOT of time...){penkraken.colors['reset']}")
            # print and save results
            command = f"nuclei -list {t}-urls.txt"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
            while True:
                salida = process.stdout.readline()
                if salida == '' and process.poll() is not None:
                    break
                if salida:
                    print(salida.strip())
                    self.results.append(salida.strip())

        except:
            print(f"{penkraken.colors['red']} Error encountered in AutoScan {penkraken.colors['reset']}")


def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to {penkraken.colors['red']}ProjectDiscovery{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] Run httpx against single/multiple targets\n[2] Run Subfinder against a single target\n[3] Run nuclei agains single/multiple targets\n[4] AutoScan single target(Every Tool)\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2' and str(x) != '3' and str(x) != '4':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
        if str(x) == '1':
            target = httpx()
        elif str(x) == '2':
            target = subfinder()
        elif str(x) == '3':
            target = nuclei()
        elif str(x) == '4':
            target = autoscan()

        try:
            # Display Results:
            out = ''
            for x in target.results:
                out += x + '\n'
            return out

        except:
            print(f"{penkraken.colors['red']}\n[-] Could not save results {penkraken.colors['red']}{target.os_name}{penkraken.colors['reset']}")

    except:
        print(f"{penkraken.colors['red']}\n[-] Exiting ProjectDiscovery Module!{penkraken.colors['reset']}")\

