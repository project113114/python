# input
x = int(input("Enter the first num"))
y = int(input("Enter the second num"))
o = int(input("Enter the o num"))
l = int(input("Enter the l num"))
ls = [[i,j,d,g] for i in range(x) for j in range(y) for d in range(o) for g in range(l) if(x>0 and y>0 and o>0 and l>0) ]
print("cartisine product of " , x , "and" , y) 
#for loop for printing each element of list line by line
z = 0

#opening file
f = open("aman.txt" , "a")
#for k in ls:
#  print(ls[z])
#  z += 1 
print("number of element are")
print(len(ls))
f.write(str(ls))
f.close()
print("completed")
