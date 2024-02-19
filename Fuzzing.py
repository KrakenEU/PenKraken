#!/usr/bin/env python

import penkraken
import subprocess

class fuzzer:
    def __init__(self,target):
        self.target = target
        self.results = []
        while True:
            x = input(f"{penkraken.colors['green']}\n[1] Subdirectories discovery\n[2] Subdomains discovery\n[3] Post data Fuzzing\n\n{penkraken.colors['blue']}[>] Choose option: {penkraken.colors['reset']}")
            if str(x) != '1' and str(x) != '2' and str(x) != '3':
                print(f"{penkraken.colors['red']}\n[-] Invalid Option{penkraken.colors['reset']}")
            else:
                break
        
        flag = ''

        if x == '2':
            self.subdomains_fuzz()
            flag = 'subdomains'
        elif x == '3':
            self.post_fuzzing()
            flag = 'post-data'
        else:
            self.subdirectories_fuzz()
            flag = 'subdirectories'
        
        try:
            # write Output to a file
            write = input(f"{penkraken.colors['green']}\n[>] Would you like to write the output to a file? (y/n): {penkraken.colors['reset']}")
            if 'y' in str(write).lower():
                file = open(f'Fuzzing-{flag}-results.txt', 'w')
                content = ''.join(str(x)+'\n' for x in self.results)
                file.write(content)
                file.close()
                print(f"{penkraken.colors['green']}\n[+] Output was correctly saved to {penkraken.colors['magenta']}'Fuzzing-{flag}-results.txt'\n{penkraken.colors['reset']}")
              
        except:
            print(f"\n{penkraken.colors['red']}[-] Error while saving output to file{penkraken.colors['reset']}")


    def subdirectories_fuzz(self):
        wordlist = input(f"{penkraken.colors['blue']}[+] Select wordlist location (ex: /usr/share/wordlist/mywordlist.txt): {penkraken.colors['reset']}")
        print(f"{penkraken.colors['blue']}\n[+] Starting subdirectory scan...\n[+] Wordlist = {penkraken.colors['magenta']}{wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['blue']}{penkraken.colors['reset']}")
        extensions =  input(f"{penkraken.colors['blue']}[+] Do you want to add any extensions to the fuzz? (ex: .php,.txt,.html) (Leave blank otherwise): {penkraken.colors['reset']}")
        filter_words = input(f"{penkraken.colors['blue']}[+] Do you want to apply a filter to avoid showing certain word (ex: 9128,532) (Leave blank otherwise): {penkraken.colors['reset']}")
        if extensions != '':
            print(f"{penkraken.colors['blue']}\n[+] Extensions = {penkraken.colors['magenta']}{extensions}{penkraken.colors['reset']}\n")
            if filter_words != '':
                command = f"ffuf -c -r -w {wordlist} -e {extensions} -u {self.target}/FUZZ -fw {filter_words}"
            else:
                command = f"ffuf -c -r -w {wordlist} -e {extensions} -u {self.target}/FUZZ"
        else:
            if filter_words != '':
                command = f"ffuf -c -r -w {wordlist} -u {self.target}/FUZZ -fw {filter_words}"
            else:
                command = f"ffuf -c -r -w {wordlist} -u {self.target}/FUZZ"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        while True:
            salida = process.stdout.readline()
            if salida == '' and process.poll() is not None:
                break
            if len(salida) > 10:
                if 'Progress' not in salida and '#' not in salida:
                    print(salida.strip())
                    self.results.append(salida.strip())

    def subdomains_fuzz(self):
        wordlist = input(f"{penkraken.colors['blue']}[+] Select wordlist location (ex: /usr/share/wordlist/mywordlist.txt): {penkraken.colors['reset']}")
        print(f"{penkraken.colors['blue']}\n[+] Starting subdomain scan...\n[+] Wordlist = {penkraken.colors['magenta']}{wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['blue']}{penkraken.colors['reset']}")
        filter_words = input(f"{penkraken.colors['blue']}[+] Do you want to apply a filter to avoid showing certain word (ex: 9128,532) (Leave blank otherwise): {penkraken.colors['reset']}")
        if filter_words != '':
            command = f"ffuf -c -w {wordlist} -H 'Host: FUZZ.{self.target.replace('http://','').replace('https://', '')}' -u {self.target} -fw {filter_words}"
        else:
            command = f"ffuf -c -w {wordlist} -H 'Host: FUZZ.{self.target.replace('http://','').replace('https://', '')}' -u {self.target}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
        while True:
            salida = process.stdout.readline()
            if salida == '' and process.poll() is not None:
                break
            if len(salida) > 10:
                if 'Progress' not in salida and '#' not in salida:
                    print(salida.strip())
                    self.results.append(salida.strip())

    def post_fuzzing(self):

        login=input(f"{penkraken.colors['green']}\n[1] Fuzz username and password\n[2] Fuzz just one parameter\n\n{penkraken.colors['blue']}[>] Select an option (1-2): {penkraken.colors['reset']}")

        if login == '1':
            json = input(f"{penkraken.colors['blue']}\n[>] Are the post parameters in JSON format? (y/n): {penkraken.colors['reset']}")
            if 'y' in json:
                try:
                    user_wordlist = input(f"{penkraken.colors['blue']}[>] Select username wordlist location (ex: /usr/share/wordlist/usernames.txt): {penkraken.colors['reset']}")
                    pass_wordlist = input(f"{penkraken.colors['blue']}[>] Select password wordlist location (ex: /usr/share/wordlist/passwords.txt): {penkraken.colors['reset']}")
                    user_payload = input(f"{penkraken.colors['blue']}[>] Select your username parameter name (ex: user): {penkraken.colors['reset']}")
                    pass_payload = input(f"{penkraken.colors['blue']}[>] Select your password parameter name (ex: pass): {penkraken.colors['reset']}")
                    print(f"{penkraken.colors['blue']}\n[+] Fuzzing POST data...\n[+] Username Wordlist = {penkraken.colors['magenta']}{user_wordlist}{penkraken.colors['blue']}\n[+] Password Wordlist = {penkraken.colors['magenta']}{pass_wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['blue']}{penkraken.colors['reset']}")
                    filter_ex = input(f"{penkraken.colors['blue']}[+] Apply a filter to avoid showing certain error message (ex: Incorrect username or password) (Leave blank otherwise): {penkraken.colors['reset']}")
                    # define prior JSON syntax
                    json_payload = '{"'+user_payload+'":"USERFUZZ","'+pass_payload+'":"PASSFUZZ"}'
                    command = f"ffuf -c -w {user_wordlist}:USERFUZZ -w {pass_wordlist}:PASSFUZZ -u {self.target} -X POST -H 'Content-Type: application/json' -d '{json_payload}' -fr {filter_ex}"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                    while True:
                        salida = process.stdout.readline()
                        if salida == '' and process.poll() is not None:
                            break
                        if len(salida) > 10:
                            if 'Progress' not in salida and '#' not in salida:
                                print(salida.strip())
                                self.results.append(salida.strip())
                except:
                    print(f"{penkraken.colors['red']}\n[-] Login FUZZ failed!{penkraken.colors['reset']}")
            else:
                try:
                    user_wordlist = input(f"{penkraken.colors['blue']}[>] Select username wordlist location (ex: /usr/share/wordlist/usernames.txt): {penkraken.colors['reset']}")
                    pass_wordlist = input(f"{penkraken.colors['blue']}[>] Select password wordlist location (ex: /usr/share/wordlist/passwords.txt): {penkraken.colors['reset']}")
                    user_payload = input(f"{penkraken.colors['blue']}[>] Select your username parameter name (ex: user): {penkraken.colors['reset']}")
                    pass_payload = input(f"{penkraken.colors['blue']}[>] Select your password parameter name (ex: pass): {penkraken.colors['reset']}")
                    print(f"{penkraken.colors['blue']}\n[+] Fuzzing POST data...\n[+] Username Wordlist = {penkraken.colors['magenta']}{user_wordlist}{penkraken.colors['blue']}\n[+] Password Wordlist = {penkraken.colors['magenta']}{pass_wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['blue']}{penkraken.colors['reset']}")
                    filter_ex = input(f"{penkraken.colors['blue']}[+] Apply a filter to avoid showing certain error message (ex: Incorrect username or password) (Leave blank otherwise): {penkraken.colors['reset']}")
                    # fuzz user and password
                    command = f"ffuf -c -w {user_wordlist}:USERFUZZ -w {pass_wordlist}:PASSFUZZ -u {self.target} -X POST -d '{user_payload}=USERFUZZ&{pass_payload}=PASSFUZZ' -fr {filter_ex}"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                    while True:
                        salida = process.stdout.readline()
                        if salida == '' and process.poll() is not None:
                            break
                        if len(salida) > 10:
                            if 'Progress' not in salida and '#' not in salida:
                                print(salida.strip())
                                self.results.append(salida.strip())
                except:
                    print(f"{penkraken.colors['red']}\n[-] Login FUZZ failed!{penkraken.colors['reset']}")


        elif login == '2':
            json = input(f"{penkraken.colors['blue']}\n[>] Are the post parameters in JSON format? (y/n): {penkraken.colors['reset']}")
            if 'y' in json:
                try:
                    pass_wordlist = input(f"{penkraken.colors['blue']}[>] Select FUZZING wordlist location (ex: /usr/share/wordlist/passwords.txt): {penkraken.colors['reset']}")
                    example = '{"user":"admin","password":"FUZZ"}'
                    payload = input(f"{penkraken.colors['blue']}[>] Select a valid JSON payload including FUZZ word (ex: {example}): {penkraken.colors['reset']}")
                    print(f"{penkraken.colors['blue']}\n[+] Fuzzing POST data...\n[+] Wordlist = {penkraken.colors['magenta']}{pass_wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['reset']}")
                    filter_ex = input(f"{penkraken.colors['blue']}[+] Apply a filter to avoid showing certain error message (ex: Incorrect username or password) (Leave blank otherwise): {penkraken.colors['reset']}")
                    # Include payload in command
                    command = f"ffuf -c -w {pass_wordlist} -u {self.target} -X POST -H 'Content-Type: application/json' -d '{payload}' -fr {filter_ex}"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                    while True:
                        salida = process.stdout.readline()
                        if salida == '' and process.poll() is not None:
                            break
                        if len(salida) > 10:
                            if 'Progress' not in salida and '#' not in salida:
                                print(salida.strip())
                                self.results.append(salida.strip())
                except:
                    print(f"{penkraken.colors['red']}\n[-] Login FUZZ failed!{penkraken.colors['reset']}")
            else:
                try:
                    pass_wordlist = input(f"{penkraken.colors['blue']}[>] Select FUZZING wordlist location (ex: /usr/share/wordlist/passwords.txt): {penkraken.colors['reset']}")
                    example = 'user=admin&pass=FUZZ'
                    payload = input(f"{penkraken.colors['blue']}[>] Select a valid payload including FUZZ word (ex: {example}): {penkraken.colors['reset']}")
                    print(f"{penkraken.colors['blue']}\n[+] Fuzzing POST data...\n[+] Wordlist = {penkraken.colors['magenta']}{pass_wordlist}{penkraken.colors['blue']}\n[+] Target = {penkraken.colors['magenta']}{self.target}\n{penkraken.colors['reset']}")
                    filter_ex = input(f"{penkraken.colors['blue']}[+] Apply a filter to avoid showing certain error message (ex: Incorrect username or password) (Leave blank otherwise): {penkraken.colors['reset']}")
                    # Include payload in command
                    command = f"ffuf -c -w {pass_wordlist} -u {self.target} -X POST -d '{payload}' -fr {filter_ex}"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True, shell=True)
                    while True:
                        salida = process.stdout.readline()
                        if salida == '' and process.poll() is not None:
                            break
                        if len(salida) > 10:
                            if 'Progress' not in salida and '#' not in salida:
                                print(salida.strip())
                                self.results.append(salida.strip())
                except:
                    print(f"{penkraken.colors['red']}\n[-] Login FUZZ failed!{penkraken.colors['reset']}")
        else:
            print(f"{penkraken.colors['red']}\n[-] Invalid Option!{penkraken.colors['reset']}")





def Init():
    try:
        print(f"{penkraken.colors['blue']}\n[+] Welcome to the {penkraken.colors['red']}Fuzzing{penkraken.colors['blue']} module!\n{penkraken.colors['reset']}")
        valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/.-_'
        check = 0
        while check == 0:
            target = input(f"{penkraken.colors['blue']}\n[>] Select your target to be scanned (ex: https://example.com): {penkraken.colors['reset']}")
            for x in target:
                if str(x) in valid:
                    check = 1
                    continue
                else:
                    print(f"{penkraken.colors['red']}\n[-] Invalid Target{penkraken.colors['reset']}")
                    check = 0
                    break

        target = fuzzer(target)
        out = ''
        for x in target.results:
            out += x + '\n'
        return out

    except:
        print(f"{penkraken.colors['red']}\n[-] Exiting Fuzzing Module{penkraken.colors['reset']}")

