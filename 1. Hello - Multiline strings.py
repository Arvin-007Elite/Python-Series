# print Statement 

# print("Hello World")

# Using Variables 

# a = 25
# b = 25
# c =a + b 
# print(c)

# Finding the datatype 

# print(type(c))

# finding memory location of variables 

# print(id(a))  
# print(id(b))
# print(id(c))

 # for a and b , memory location will be same , because both have same values, thats why python is memory efficient !!

# a = 50

# print(id(a))

# now C and new A having same memory location !!

#-------------------------------------------------------------

# to display all keyword in python !

# import keyword
# print(keyword.kwlist)

# to get input
# default all will print as String  , we should use type converting 
# Name = input("Enter ur number: ")
# print(type(Name))

# it takes number also string !

# ----------------  Adding 2 inputs

# a = input("enter the value of a :")
# b = input("en ter the value of b : ")
# c = a+b
# print(c)
# now answer will not ne added , just link and prints it !
# because it is in string !
# 20

# to make it add the numbers
# also converted the numbers as int , float !!!!

# a = int(input("enter a number: "))
# b = float(input("Enter a number: "))
# c = a + b
# print(type(c),c)


# Multiple inputs in single line
# Using .split()
# we can use symbols to split the words when giving the input

# Name1,Name2,Name3 = input("Enter the 3 names: ").split(',')
# print(Name1,Name2,Name3)

# to print multi line strings 
# para = """lorem ipsum dolor sit amet, consectetur adipiscing jhgyug"""
# print(para)

# to get multi line strings is only through while loop !!

# para=[]
# print("Enter the para : ")

# while True:
#     line= input()

#     if line:
#         para.append(line)
#     else:
#         break
#     print(para)
# # till here it in list 

#     output = '\n'.join(para)
#     print(output)

    # this is to make the final output as  a para !!

# ---------------------------

# comments 
# Single line comments   - # this is tomato
# Multi line comments - """ this is tomato , this is potato , this is apple """"


#---------------------------------------------------------------------


# generating a random number

# import random
# print(random.randrange(2, 8))


# assigning many variables to many values

# x , y , z =["apple","orange","grape"];
# print(x)


# assigning many vars to a single string

# x = y = z ="apple";
# print(x);

# unpacking a list or a tuple

# fruits = ["apple","orange","grape"];
# x , y , z = fruits;
# print(x);