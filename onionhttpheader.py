import os
import sys
import socks
import socket
import requests

os.system("clear")

print (chr(27)+"[37m")

os.system("sudo service tor restart")

print ("                    +=======================================+")
print ("                    |           ONION HTTP HEADER           |")
print ("                    +=======================================+")
print ("                    |   Author : Rahat Khan Tusar(rkt)      |")
print ("                    |   Github : https://github.com/r3k4t   |")
print ("                    +=======================================+")

print

onionsite = raw_input('Enter a onionsite :')
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
response = session.get(onionsite)
print(response.headers)
