#dictionary
import random as rn

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
#welcome statement
print(f"{Fore.RED} WELCOME TO OUR DICTINOARY ")
print(f"{Fore.BLUE} Enter the Word Present in array  :- \" set , relation , function , domain \" ")

#input
x = str(input("Enter the Word "))

dic = { "set":"A Well Define Collection of Element is Called SET " , "relation":"Relation is Define Between to Set" , "function": "Function is a Special Type of Relation Between Sets" , "domain":"All the Possiable Input of a Function or Relation is Called Domain" }

#random
rnum = rn.randint(0,3)

#list key
ky = ("set" , "relation" , "function" , "domain")

#condition to print meaning



if(x == ""):
  print(f"{Fore.RED} TRY to type " + f"{Fore.BLUE}" +  ky[rnum] )

elif(x == "set"):
  print( f"{Fore.BLACK} {Back.RED}" +  dic["set"])

elif(x == "relation"):
  print(f"{Fore.BLACK} {Back.RED}" + dic["relation"])

elif(x == "function"):
  print(f"{Fore.BLACK} {Back.RED}" + dic["function"])

elif(x == "domain"):
  print(f"{Fore.BLACK} {Back.RED}" + dic["domain"])

else:
  print(f"{Fore.RED} TRY to type" + f"{Fore.BLUE}" +  ky[rnum])
