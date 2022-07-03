#!/usr/bin/python3
# <-- Mr Shell -->
import hashlib
import requests
import threading
import time
import sys
import os

os.system('clear' if os.name == 'posix' else 'cls')
print('''\x1b[1;35m
 _   _           _      ____                _             
| | | | __ _ ___| |__  / ___|_ __ __ _  ___| | _____ _ __ 
| |_| |/ _` / __| '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
|  _  | (_| \__ \ | | | |___| | | (_| | (__|   <  __/ |   
|_| |_|\__,_|___/_| |_|\____|_|  \__,_|\___|_|\_\___|_|\x1b[00m

     \x1b[33m[+] Creator:  \x1b[36m [ Mr-shell              ]
     \x1b[33m[+] Github:   \x1b[36m [ Github.com/Linux-Zone ]
     \x1b[33m[+] Telegram: \x1b[36m [ T.me/Linux_Zone_Org   ]

\x1b[1;92m1) \x1b[00mOnline Hash Cracking \x1b[91m(\x1b[00mMD5\x1b[91m)
\x1b[1;92m2) \x1b[00mOffline Hash Cracking
\x1b[1;92m3) \x1b[00mExit
''')

def crack():
	start = time.time()
	for word in wordlist:
		if hash_function(word.encode()).hexdigest() == hash_value:
			print("\n\x1b[92mPassword Found: \x1b[00m{}".format(word))
			end = time.time()
			print("\x1b[92mSpeed: \x1b[00m{}ms\n".format(str(end - start)[:4]))
			time.sleep(1)
			sys.exit()
	
	print('\n\x1b[91mPassword not found!\x1b[00m\n')
	time.sleep(1)
	sys.exit()

method = input('\x1b[91m>> \x1b[94mChoose attack method: \x1b[00m')

if method == '1':
	hash_value = input('\x1b[91m>> \x1b[94mEnter hash value: \x1b[00m')
	start = time.time()
	try:
		password = requests.get("http://nitrxgen.net/md5db/" + hash_value, verify=False).text
		if password:
			print("\n\x1b[92mPassword Found: \x1b[00m{}".format(password))
			end = time.time()
			t = str(end - start)[:4]
			print("\x1b[92mTime: \x1b[00m{}ms\n".format(t))
			time.sleep(1)
			sys.exit()
		else:
			print('\n\x1b[91mPassword not found!\x1b[00m\n')
			time.sleep(1)
			sys.exit()
	except KeyboardInterrupt:
		print('\n\x1b[91mHave good time :)\x1b[00m\n')
		time.sleep(1)
		sys.exit()

elif method == '2':
	print('\n\x1b[1;92m1) \x1b[00mMD5\n\x1b[1;92m2) \x1b[00mSHA1\n\x1b[1;92m3) \x1b[00mSHA224\n\x1b[1;92m4) \x1b[00mSHA256\n\x1b[1;92m5) \x1b[00mSHA384\n\x1b[1;92m6) \x1b[00mSHA512\n\x1b[1;92m7) \x1b[00mExit\n')
	hash_type = input('\x1b[91m>> \x1b[94mChoose hash type: \x1b[00m')
	hash_value = input('\x1b[91m>> \x1b[94mEnter hash value: \x1b[00m')
	wordlist = open(input('\x1b[91m>> \x1b[94mEnter password list file path: \x1b[00m'), "r").read().splitlines()

	if hash_type == '1':
		hash_function = hashlib.md5
	elif hash_type == '2':
		hash_function = hashlib.sha1
	elif hash_type == '3':
		hash_function = hashlib.sha224
	elif hash_type == '4':
		hash_function = hashlib.sha256
	elif hash_type == '5':
		hash_function = hashlib.sha384
	elif hash_type == '6':
		hash_function = hashlib.sha512
	else:
		print('\n\x1b[91mInvalid hash type!\x1b[00m\n')
		time.sleep(1)
		sys.exit(1)
	
	thread = threading.Thread(target=crack)
	thread.start()

else:
	print('\n\x1b[91mHave good time :)\x1b[00m\n')
	time.sleep(1)
	sys.exit()
