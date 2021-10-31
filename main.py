import pyfiglet
import os
from time import sleep
from pip._vendor.colorama import Fore

ascii_banner = pyfiglet.figlet_format("JCPS PASS GEN")
print(f'{Fore.GREEN} {ascii_banner}')
print('============================================')


print('FOLLOW INSTRUCTIONS BELLOW TO GENERATE ALL POSSIBLE JCPS PASSWORDS')
print('------------------------------------------------\n')
print('GENERATES ALL COMBINATIONS FOR BRUTE FORCE ATTACK')
print('-----------------------------------------------------')
print(f'{Fore.LIGHTRED_EX}**************************************************************************************')
print(f'{Fore.LIGHTRED_EX}FOR RESEARCH PURPOSES ONLY!!! NOT TO BE USED IN ANY WAY OTHER THAN FOR FUN/TESTING!!!!')
print(f'{Fore.LIGHTRED_EX}**************************************************************************************\n')

'''Get user initials and make them capital'''
initals = input(f'{Fore.GREEN}Enter first and last initials: ')
initals = initals.upper()

'''Set prefix and get beginning of password'''
prefix = 'jcps'
beginning = prefix + initals

'''Loading screen'''
print('============================================')
print(f'{Fore.MAGENTA}Generating all combinations for:  {initals}\n')

msg = f"{Fore.RED}Generating..\n"
for x in range(5):
  msg = msg + "."
  print(msg)
  sleep(1)
  os.system("cls")

print("%sDone!" % msg)

msg = f"{Fore.YELLOW} WRITING TO DATASET"
for x in range(3):
  msg = msg + "."
  print(msg)
  sleep(1)
  os.system("cls")

print("\n%sDone!" % msg)


msg = f"{Fore.BLUE} Finishing Up\n"
for x in range(4):
  msg = msg + "."
  print(msg)
  sleep(1)
  os.system("cls")

print("%sDone!" % msg)




'''Generate all possible number combinations and write to txt file'''
finalPassData = open('finalPasswordData', 'w')
for i in range(10000):
    number = f"{i:04d}\n"
    finalPass = beginning + number
    finalPassData.write(finalPass)

finalPassData.close()
