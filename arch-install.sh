#!/bin/bash

echo '[+] Installing Required Packages...'
sudo pacman -S wafw00f halberd go python-python-nmap nmap exploitdb python-requests wget git sherlock whois holehe infoga h8mail theharvester maigret cloudfail perl-image-exiftool hash-identifier hashcat
echo '[+] Installing Project Discovery tools...'
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
echo '[+] Installing our favorite FUZZING tool ffuf'
go install github.com/ffuf/ffuf/v2@latest
echo '[+] Making links to Go Tools...'
sudo ln -sf /home/$USER/go/bin/subfinder /usr/local/bin/subfinder
sudo ln -sf /home/$USER/go/bin/httpx /usr/local/bin/httpx
sudo ln -sf /home/$USER/go/bin/nuclei /usr/local/bin/nuclei
sudo ln -sf /home/$USER/go/bin/ffuf /usr/local/bin/ffuf
