import os
from time import sleep
import requests
import random
import string
import pyfiglet
from colorama import Fore
import webbrowser

os.system("mode con cols=80 lines=20")
os.system('cls')

text = pyfiglet.figlet_format("proxy scrapper" , font = "big")

info = '''
███╗   ██████████████████████████████╗██████╗ ██████╗███╗   █████████╗
████╗ ██████╔════██╔════██╔════██╔══████╔══████╔═══██████╗  ████╔════╝
██╔████╔███████╗ █████╗ █████╗ ██║  ████████╔██║   ████╔██╗ ███████╗  
██║╚██╔╝████╔══╝ ██╔══╝ ██╔══╝ ██║  ████╔══████║   ████║╚██╗████╔══╝  
██║ ╚═╝ ███████████║    █████████████╔██║  ██╚██████╔██║ ╚███████████╗
╚═╝     ╚═╚══════╚═╝    ╚══════╚═════╝╚═╝  ╚═╝╚═════╝╚═╝  ╚═══╚══════╝
'''

print(info)
print(f'{Fore.CYAN}Program made by ARTIX_')
print()

ready = input(f'{Fore.MAGENTA}Press [ENTER] to scrap proxies ! (Socks4,Socks5,HTTP)')

url = 'https://api.openproxylist.xyz/http.txt'
r = requests.get(url)
results = r.text
with open ("http.txt", "w") as file:
 file.write(results)
 
url = 'https://api.openproxylist.xyz/socks4.txt'
r = requests.get(url)
results = r.text
with open ("socks4.txt", "w") as file:
 file.write(results)

url = 'https://api.openproxylist.xyz/socks5.txt'
r = requests.get(url)
results = r.text
with open ("socks5.txt", "w") as file:
 file.write(results)

 