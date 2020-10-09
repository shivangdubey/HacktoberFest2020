PasswordCracking_Hashing_EthicalHacking

This folder contains password hashers which help you and your organisation to check if the password is strong enough to be cracked by others...


CAUTION:Check for the your passwords not others which you have permissions to, otherwise it is an act of cybercrime..


RECCOMENDATION: Use linux terminals to execute the codes for better result


1)hasher.py(this programs hashes your password into md5, sha1, sha224, sha256 and sha512)


command : python3 hasher.py
Enter a string to hash:<enter your password>


2)md5brute.py(this program takes the md5 hash value and text file to guess your pasword)


command : python3 md5brute.py
Enter MD5 hash value: <md5 hash>
Enter the path to the password file: <enter the text file containing possible passwords...I have added 10000.txt for your help>


3)sha256brute.py(this program takes the sha256 hash value and text file to guess your pasword)


command : python3 sha256brute.py
Enter sha256 hash value: <sha256 hash>
Enter the path to the password file: <enter the text file containing possible passwords...I have added 10000.txt for your help>

	 
4)sha512brute.py(this program takes the sha512 hash value and text file to guess your pasword)


command : python3 sha512brute.py
Enter sha512 hash value: <sha512 hash>
Enter the path to the password file: <enter the text file containing possible passwords...I have added 10000.txt for your help>


5)sha1hash.py(this program takes sha1 hash and uses online library to crack the password...
here url used: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt )


command: python3 sha1hash.py
Enter the Hash value: <enter sha1 hash to be cracked >



HAPPY HACKING AND STAY SAFE BY KNOWING YOUR WEAKNESSES
