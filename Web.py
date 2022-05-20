# Modules
import time
import socket
import sys


# Art
print("""
 _     _       ___   _____         _____   _____   _____        _   _____  
| |   / /     /   | |  _  \       /  ___| | ____| |_   _|      | | |  _  \ 
| |  / /     / /| | | |_| |       | |     | |__     | |        | | | |_| | 
| | / /     / / | | |  _  /       | |  _  |  __|    | |        | | |  ___/ 
| |/ /     / /  | | | | \ \       | |_| | | |___    | |        | | | |     
|___/     /_/   |_| |_|  \_\      \_____/ |_____|   |_|        |_| |_|
""")
print("=========================================================================")

# User Input
host_name = input("Enter The Website Address: ")
print("--------------------")

print("Waiting...")
time.sleep(1)
print("--------------------")

# Variable
ip = socket.gethostbyname(host_name)

# Output Function
try:
	print("Website Is: " +host_name)
	print("====================")
	print("IP Address Is: " ,ip)
	time.sleep(15)
	
except socket.gaierror:
	print("Enter Valid Website Address...!")
	time.sleep(5)
	exit()
	
	
# Output In File
output_file = open("Result.txt","w+")
output_file.write(f"\nWebsite : {host_name}")
output_file.write(f"\nIp Address : {ip}")