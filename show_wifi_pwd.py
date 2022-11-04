#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

print("")
print(f"{'SSID':^32} || {'PASSWORD':<}")
print("{:=<80}".format(''))

data = subprocess.check_output(['netsh.exe', 'wlan', 'show', 'profile']).decode('utf-8').splitlines()
profile = [i.split(": ")[1] for i in data if "Profil " in i]

for i in profile:
    results = subprocess.check_output(['netsh.exe', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').splitlines()
    passwd = [a.split(": ")[1] for a in results if "Contenu de la clé" in a]
    try:
        print (f"{i:^32} || {passwd[0]:<}")
    except IndexError:
        print ("{i:<32}|| {'':<}")
print("")
