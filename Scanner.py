# Made By kerolos osama
# First Download Modules python-nmap
# sudo apt-get install pip
# pip install python-nmap
# If Not Worked Download This File
# sudo apt-get install git -y
# git clone https://bitbucket.org/xael/python-nmap
# If You Use Windows Visit Website To Get More Inforamtion


# Modules
import nmap
import platform
import time
import os


# Variables
scanner = nmap.PortScanner()
line = "============================================="
my_system_1 = platform.uname()
my_system_2 = my_system_1.system
name_art = """
 _____   _____       ___   __   _  
/  ___/ /  ___|     /   | |  \ | | 
| |___  | |        / /| | |   \| | 
\___  \ | |       / / | | | |\   | 
 ___| | | |___   / /  | | | | \  | 
/_____/ \_____| /_/   |_| |_|  \_|
"""


# OS Condition
# Windows
if my_system_2 == "Windows":
	time.sleep(1)
	os.system('cls')
	print(name_art)
	print(line)
	print("1.Port Scanner")
	print("2.Host Discovery")
	print(line)
	user_input_1 = int(input("Choose : "))
	
	# User Condition
	# Port Scan
	if user_input_1 == 1:
		time.sleep(1)
		os.system('cls')
		print(name_art)
		print(line)
		
		# Input For Scan
		Port_Num_Begin = int(input("Port Range Begin : "))
		print(line)
		Port_Num_End = int(input("Port Range End : "))
		print(line)
		Target_Ip_Address = input("Ip Address : ")
		print(line)
		print("Scan Start Now")
		print(line)
		
		# Scan Result
		for i in range(Port_Num_Begin , Port_Num_End):
			i = i+1
			result = scanner.scan(Target_Ip_Address,str(i))
			
			try:
				result = result['scan'][Target_Ip_Address]['tcp'][i]['state']
			except KeyError:
				print("Please Type An Correct IP...!")
				time.sleep(1)
				exit()
				
			time.sleep(2)
			print("Port", i ,"Is", result)
		
		
	# Host Discovery	
	elif user_input_1 == 2:
		time.sleep(1)
		os.system('cls')
		print(name_art)
		print(line)
		print("Coming Soon...!")
		time.sleep(1)
		
		

# Linux
elif my_system_2 == "Linux":
	time.sleep(1)
	os.system('clear')
	print(name_art)
	print(line)
	print("1.Port Scanner")
	print("2.Host Discovery")
	print(line)
	user_input_1 = int(input("Choose : "))
	
	# User Condition
	# Port Scan
	if user_input_1 == 1:
		time.sleep(1)
		os.system('clear')
		print(name_art)
		print(line)
		
		# Input For Scan
		Port_Num_Begin = int(input("Port Range Begin : "))
		print(line)
		Port_Num_End = int(input("Port Range End : "))
		print(line)
		Target_Ip_Address = input("Ip Address : ")
		print(line)
		print("Scan Start Now")
		print(line)
		
		# Scan Result
		for i in range(Port_Num_Begin , Port_Num_End):
			i = i+1
			result = Scanner.scan(Target_Ip_Address,str(i))
			
			try:
				result = result['scan'][Target_Ip_Address]['tcp'][i]['state']
			except KeyError:
				print("Please Type An Correct IP...!")
				time.sleep(1)
				exit()
				
			time.sleep(2)
			print("Port", i ,"Is", result)
		
		
	# Host Discovery	
	elif user_input_1 == 2:
		time.sleep(1)
		os.system('clear')
		print(name_art)
		print(line)
		print("Coming Soon...!")
		time.sleep(1)
		
# This Tool Made By Kerolos