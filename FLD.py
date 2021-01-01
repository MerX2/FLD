import pyautogui
import time
from colorama import Fore, Back, Style

print(Fore.RED+'''
███████╗██╗     ██████╗ 
██╔════╝██║     ██╔══██╗
█████╗  ██║     ██║  ██║
██╔══╝  ██║     ██║  ██║
██║     ███████╗██████╔╝  By MerX
╚═╝     ╚══════╝╚═════╝ ''')



msg = input(Fore.WHITE+"[" + Fore.BLUE +"FLD" + Fore.WHITE+"]" + " Enter the message: ")
n = input(Fore.WHITE+"[" + Fore.BLUE +"FLD" + Fore.WHITE+"]" + " How many times?: ")


count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Attack!! uwu")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
    


