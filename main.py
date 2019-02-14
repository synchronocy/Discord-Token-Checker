#!usr/bin/env python3

# Date: 02-09-19, Feb ~ 9nd 2010 | Synchronocy
# Project: Discord Token Checker
# Simple token checker
# IDLE Python 3.6 64-bit
import requests

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
            try:
                if src.status_code == 200:
                    print('Token Works!')
                else:
                    print('Invalid Token.')
            except Exception:
                print("Yeah we can't contact discordapp.com")
