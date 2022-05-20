# To Generat A Strong Password
# The Library
import random
import time

print("""
 _____       ___   _____   _____        _____   _____   __   _  
|  _  \     /   | /  ___/ /  ___/      /  ___| | ____| |  \ | | 
| |_| |    / /| | | |___  | |___       | |     | |__   |   \| | 
|  ___/   / / | | \___  \ \___  \      | |  _  |  __|  | |\   | 
| |      / /  | |  ___| |  ___| |      | |_| | | |___  | | \  | 
|_|     /_/   |_| /_____/ /_____/      \_____/ |_____| |_|  \_|

""")
print("===============================================================")

# The Variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]#@$+/."
# The Misson Of Code
all = lower + upper + number + symbol
length = 16
password = "".join(random.sample(all, length))
print("Password is : \n")
print(password)
# The Time Will code Run To Stop
time.sleep(1000)
