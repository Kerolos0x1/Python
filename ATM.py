import time
import os

print("""
 _____  __    __           ___   _____       ___  ___  
|  _  \ \ \  / /          /   | |_   _|     /   |/   | 
| |_| |  \ \/ /          / /| |   | |      / /|   /| | 
|  ___/   \  /          / / | |   | |     / / |__/ | | 
| |       / /          / /  | |   | |    / /       | | 
|_|      /_/          /_/   |_|   |_|   /_/        |_| """)

print("=======================================================")

user1 = input("Enter Your Account Name: ")
print("=====================================")
pass1 = input("Enter Your Account PassWord: ")

if user1 == "" or pass1 == "":
	print("=================================")
	print("Please Try Agian")
	time.sleep(3)
	exit()
	
l = 4500
os.system("cls")
time.sleep(2)
################################################################
def Allfunction():
	print("""
 _   _   _            ___   _____       ___  ___        _____  __    __ 
| | | | | |          /   | |_   _|     /   |/   |      |  _  \ \ \  / / 
| |_| | | |         / /| |   | |      / /|   /| |      | |_| |  \ \/ /  
|  _  | | |        / / | |   | |     / / |__/ | |      |  ___/   \  /   
| | | | | |       / /  | |   | |    / /       | |      | |       / /    
|_| |_| |_|      /_/   |_|   |_|   /_/        |_|      |_|      /_/     """)
	
	print("=======================================================================")
################################################################
	print("(1) Know Your Balance? \n")
	print("(2) Know Your Name And Pass? \n")
	print("(3) Transfer Money? \n")
	print("(4) Add Money? \n")
################################################################
	all1 = input("Choose : ")
	if all1 == "1":
		print("=======================")
		print("Your Balance Is : 4500$")
		print("====================================")
		
		print("Would You Like To Return To Main Menu...? \n")
		print("1.Yes")
		print("2.No")
		print("==========")
		no_or_yes = input("Choose : ")
		
		if no_or_yes == "1":
			return Allfunction()
		elif no_or_yes == "2":
			print("==========================")
			print("Thank You For Visiting....")
			time.sleep(3)
			exit()
################################################################	
	elif all1 == "2":
		print("=============================")
		print("Your Name Is : "+user1)
		print("=============================")
		print("Your Password Is : "+pass1)
		print("====================================")
		
		print("Would You Like To Return To Main Menu...? \n")
		print("1.Yes")
		print("2.No")
		print("==========")
		no_or_yes1 = input("Choose : ")
		
		if no_or_yes1 == "1":
			return Allfunction()
		elif no_or_yes1 == "2":
			print("==========================")
			print("Thank You For Visiting....")
			time.sleep(3)
			exit()
#################################################################
	elif all1 == "4":
		print("===================================")
		p = int(input("Enter Balance To Add It : "))
		print("==============================")
		print("Your Balance Now Is: ",l+p,"$")
		print("==============================")
		
		print("Would You Like To Return To Main Menu...? \n")
		print("1.Yes")
		print("2.No")
		print("==========")
		no_or_yes2 = input("Choose : ")
		
		if no_or_yes2 == "1":
			return Allfunction()
		elif no_or_yes2 == "2":
			print("==========================")
			print("Thank You For Visiting....")
			time.sleep(3)
			exit()
#################################################################		
	if all1 == "3":
		print("===============================================")
		tra = input("Enter Username To Transfer Money To It : ")
		print("===============================================")
#################################################################		
	bal = int(input("Enter Balance : "))
	if bal > l:
		print("===========================================")
		print("Not Enough Money..Please Check Your Balance")
		print("===========================================")
		
		print("Would You Like To Return To Main Menu...? \n")
		print("1.Yes")
		print("2.No")
		print("==========")
		no_or_yes3 = input("Choose : ")
		
		if no_or_yes3 == "1":
			return Allfunction()
		elif no_or_yes3 == "2":
			print("==========================")
			print("Thank You For Visiting....")
			time.sleep(3)
			exit()
################################################################		
	elif bal < l:
		print("======================")
		print("Successful Proccess..!")
		print("======================")
		print("Money Tranfer To " +tra.capitalize(),"@PYATM.com")
		print("====================================")
		
		print("Would You Like To Return To Main Menu...? \n")
		print("1.Yes")
		print("2.No")
		print("==========")
		no_or_yes = input("Choose : ")
		
		if no_or_yes == "1":
			return Allfunction()
		elif no_or_yes == "2":
			print("==========================")
			print("Thank You For Visiting....")
			time.sleep(3)
			exit()
Allfunction()