import matplotlib.pyplot as mp
import random as rn
import colorama
from colorama import Fore, Back, Style
# init colorama
colorama.init(autoreset = True )

# Set the Range of number
z =int(input("Range:- "))
# Set Total Repetation Event
x = int(input("Event:- "))
# Creating Empty List
ls = list()
plotls = list()
# Defining t for Condition True When List is Completed For Rest Process
t = 0
# ti for breaking while loop when ti == z or complete event
ti = 0

#function for percentage
def per():
  f = (ls.count(ti)/x)*100
  return f
# For Loop for Event
print(f"{Fore.RED} excuting process ")
for i in range(0,x):
  t += 1
  # Genrating random number in range upto event completed
  r = rn.randint(1,z)
  # Adding random number in empty list
  ls.append(r)
  # printing number of repetation of all elements of list
  if(t == x):
    while(True):
      ti += 1
      # using count()
      print(ti," :- ", ls.count(ti)," ", per(),"%")
      # putting value in plotls
      plotls.append(ls.count(ti))
      # breaking loop after completing printing 
      if(ti == z):
        print(f"{Fore.RED} completed")
        mp.plot(plotls)
        mp.show()
        break
