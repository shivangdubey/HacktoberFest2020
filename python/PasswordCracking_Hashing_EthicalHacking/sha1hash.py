
#!/usr/bin/python

import hashlib
#hash library
from urllib.request import urlopen
#using url from website
from termcolor import colored


sha1hash = input("[+] Enter sha1 Hash value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#importing file from web

for password in passlist.split('\n'):
	hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
	if hashguess == sha1hash:
		print(colored("[+]The password is: " + str(password),'green'))
		quit()
	else:
		print(colored("[-]Password guess " + str(password) + "doesnot match, trying next...",'yellow'))
#checking if the password matches the hash

print(colored("Password not in passwordlist",'red'))
