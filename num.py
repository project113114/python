import random as rn
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
#play function

def play():
  t = 1
  while(True):
    x = int(input("enter num between 1 to 20 "))
    if (x < 1 or x > 20):
      print("enter the number between " + f"{Fore.BLUE} 1 to 20 ")
    elif( x < my_num ):
      print("your entered" f"{Fore.RED} lesser number ")
      t += 1
    elif(x > my_num ):
      print("you enterd" + f"{Fore.RED} greater number ")
      t += 1
    elif( x == my_num ):
      print(f"{Fore.BLUE} win the match " + f"{Fore.RED} completed in " + str(t) + f"{Fore.BLUE} gausses ")
      break
    else:
      t += 1
    if( t == 9 ):
      print(f"{Fore.RED} game over ")
      break

while(True):
  my_num = rn.randint(0,20)
  d = str(input("mode :- " + f"{Fore.BLUE} play " +f"{Fore.GREEN}or" + f"{Fore.RED} exit "))

  if(d == "play"):
      print(f"{Fore.BLUE} STARTING THE GAME ")
      print("  ")
      play()
  if(d == "exit"):
      break
      print(" ")
      print(f"{Fore.RED} GOOD TO SEE YOU AGAIN ")
