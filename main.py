#!usr/bin/env python3

# Date: 02-09-19, Feb ~ 9nd 2010 | Synchronocy
# Project: Discord Token Checker
# work around from discord.py
# IDLE Python 3.6 64-bit
import requests
headers={
    'Authorization': 'tokenhere' # I'll soon be adding support for bulk checking.
}
src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
try:
    if src.status_code == 200:
        print('Token Works!')
    else:
        print('Invalid Token.')
except Exception:
    print("Yeah we can't contact discordapp.com")    
