#!/bin/bash

echo '[+] Installing Required Packages...'
sudo pacman -S wafw00f halberd go python-python-nmap nmap
echo '[+] Installing Project Discovery tools...'
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
echo '[+] Making links to Go Tools...'
sudo ln -sf /home/$USER/go/bin/subfinder /usr/local/bin/subfinder
sudo ln -sf /home/$USER/go/bin/httpx /usr/local/bin/httpx
sudo ln -sf /home/$USER/go/bin/nuclei /usr/local/bin/nuclei

echo "[+] DONE! DON'T FORGET TO ADD TO YOUR PATH /home/$USER/.local/bin"
