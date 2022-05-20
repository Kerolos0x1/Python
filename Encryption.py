import hashlib
import time
import os

def Fun_1():
	print("""
 _____   _____   __    __  _____   _____   _____  
/  ___| |  _  \  \ \  / / |  _  \ |_   _| /  _  \ 
| |     | |_| |   \ \/ /  | |_| |   | |   | | | | 
| |     |  _  /    \  /   |  ___/   | |   | | | | 
| |___  | | \ \    / /    | |       | |   | |_| | 
\_____| |_|  \_\  /_/     |_|       |_|   \_____/ 
	""")
	print("==================================================")

	hashs = hashlib.algorithms_available
	print(hashs,"\n")

	user_input = input("Enter The Type Of Encryption : ")
	print("==============================")

	if user_input not in hashs:
		print("Error Please Try Again...!")
		time.sleep(2)
		sys = os.system("cls")		
		return Fun_1()
	
	text = input("Enter The Words : ")
	print("==============================")
	text = text.encode("utf-8")
	hash_hash = hashlib.new(user_input)
	hash_hash.update(text)

	encry = hash_hash.hexdigest()
	print("The Encryption Is : "+encry)
	print("==============================")
	time.sleep(5)
	exit()
	
Fun_1()