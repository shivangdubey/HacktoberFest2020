#!/usr/bin/python

from termcolor import colored
import hashlib


def tryOpen(wordlist):
        global pass_file
        try:
                pass_file = open(wordlist, "r")
        except:
                print("[!!]No such file at that path: ")
                quit()
#function trying  to open the file from which password will be read




pass_hash = input("[+] Enter SHA512 hash value: ")
wordlist = input("[+] Enter the path to the password file: ")

tryOpen(wordlist)


for word in pass_file:
        print(colored("[-] Trying: " + word.strip("\n"),'yellow'))
        enc_wrd = word.encode('utf-8')
        sha512digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
#from the word file every word is picked and converted into md5hash
        if sha512digest == pass_hash:
                print(colored("[+] Password Found: " + word, 'green'))
                exit(0)
#checks if the password matches from the wordlist

print(colored("[!!] Password Not in List",'red'))
