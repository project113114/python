import numpy as np
import math
import matplotlib.pyplot as plt
# x^2 function graph
siz = int(input("enter size"))
ls = list()
t = 1


for i in range(siz):
  rad = i*(np.pi/180)
  # rad convert degree into radian
  ls.append(rad)
  t += 1
print(ls)
plt.plot(ls,(np.sin(ls))**3)

op = input("do you want to save")
if(op.upper() == "Y"):
  gn = str(input("Enter name of file to save"))
  try:
    fo = str(input("Enter format"))
    dp = int(input("Enter the dpi"))
  except Exception as e:
    print(e)
  fname = "graph/" + gn + "." + fo
  try:
    print(fname)
    print(type(fname))
    plt.savefig(fname,dpi=dp , bbox_inches='tight')
  except Exception as er:
   print(er)
plt.show()
plt.close()
