# problem 2 faulty calculator

x= int(input("first num"))
y= int(input("secnd num"))
op= input("+ , - , / , * :- ")
print(op)
if(x == 0 and y == 0 ):
  print("non")
elif(x == 45 and y == 3 and op == "*"):
  print(555)
elif(x == 56 and y == 9 and op == "+"):
  print(77)
elif(x == 56 and y == 6 and op == "/"):
  print(4)
elif(op == "+"):
  print(x + y)
elif(op == "*"):
  print(x * y)
elif(op == "-"):
  print(x - y)
elif(op == "/"):
  print(x / y)
else:
  print("enter correct")
