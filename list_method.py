
#NOTE :- Index Start From 0
#NOTE :- Length Start From 1

# List Methods

# Method extend()
print("extend() Method")
x = [1,2,3,4,5]
y = [6,6,6,7,8,9,10]
'''
extend() Method is Used to Add an exsiting 
List at the End of Current List
'''
x.extend(y)
print(x)



# append Method
print(" append() Method ")

x.append(6)
'''
append() Method is Used to Add an Element at
the End of Current List 
'''
print(x)


# clear() Method
print("clear() Method ")
x.clear()
'''
clear() Method is Used to Empty the Current
List

'''
print(x)

# copy() Method
print(" copy() Method ")
z = y.copy()
'''
copy() Method Create a copy of Current List
and If  we Change in copied List it Does not 
Effect Original One
'''
print(z)


# count() Method

print(" count() Method ")
z = y.count(6)
'''
count() Method is Used for Counting the
Number of Repetation of an Element in the
List it Take a Element as Argument and
Return the Number of Repetation
'''
print(z)

# index() Method
print("index() Method")
z = y.index(7)
'''
index() Method is Used for Know the Index
of Element of the List and if the Element is
Repeted then Show Index of the First
Element and it ELement as argument
'''
print(z)
z = y.index(6)
print(z)

#insert() Method
print("insert() Method")
'''
insert() Method is Used for Inserting Element
in a List at Specified Index 
Example List.index( <position> , <value> )

'''
y.insert(1,5)
print(y)

#pop() Method
print(" pop() Method ")
print(y)

'''
the pop() Method is Used for Removing Element
at the specified Index in Current List
it Take position of Element as Argument
'''

y.pop(0)
print(y)

# remove() Method
print("remove() Method")
y.remove(10)
'''
remove() Method is Used for Removing The 
Element from List and it Take Element as
Argument
'''
print(y)

# reverse() Method
print("reverse() Method")
'''
reverse() Method is Used for Reversed the 
Order of the List
'''
y.reverse()
print(y)

# sort() Method
print("sort() Method")
print(y)

'''
sort() Method is Used for Sorting the list 
Default asscending 
'''

y.sort()
print(y)

