
# DAY-2
# Lab-1

# Variables
w=True
x=12
y="Hello"
z=1.1



# Inputs
var1 = input("\nEnter a value")
var1 = int(input("Enter a value"))

#Checking data type
var1 = 2
print(type(var1))


#Basic Operations
a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# String Op
greeting = "Hello"
audience = "world"
full_greeting = greeting +", "+ audience

len(greeting)
greeting.upper()
greeting.lower()


# Loops and conditions
x=5

if x==5:
  print("Yes")
else:
  print("No")

# elif
if x>5:
  print("greater")
elif x<5:
  print("lesser")
else:
  print("equal")

# nested if
a = 5
b = 8

if a>10:
  if b>15:
    print("Both greater")

# different loops structure
fruits = ["Apple","Orange","Potato"]

for fruit in fruits:
  print(fruit)



for i in range(1,6):
  print(i)


# TASK 1
num = int(input("Enter Number:"))

if num%3 == 0 and num%5==0:
  print("Divisble by 3 and 5 both")
else:
  print("Not Divisible by both")

# Task 2
for i in range(1,21):
  if i%2 == 0:

    print(i)

#Functions

# No Arg

# def greeting():
#   print("Hello world!")

# greeting()

# With Arg

def greet_person(name):
  print(f"Hello Mr. {name}")

greet_person("Younis")

# With Default Arg

def greet_person(name, message = ", How are you?"):
  print(f"Hello Mr. {name}")

greet_person("Younis","Hey")


# List [] Ordered and changeable, duplicates are OK
fruits = ["Apple","Orange","Banana"]

# print(dir(fruits)) # to check methods available
# print(help(fruits)) # for help of this collection
# print(len(fruits)) # check out the length of the collection
# print("Apple" in fruits) # check whether this exist in out collection
# fruits[0] = pineaple # re asign value in our collection

# fruits.append("Pineaple") # Appends the pineapple to the end of list
# fruits.remove("Apple") # removes that element from list
# fruits.insert(0,"Coconut") # inserts the element at given index
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("Apple"))
# print(fruits.count("Apple"))

# Tuples = {} Ordered and unchangeable,Duplicates ok, Faster

fruits = ("Apple","Orange","Banana")

# print(dir(fruits)) # to check methods available
# print(help(fruits)) # for help of this collection
# print(len(fruits)) # check out the length of the collection
# print("Apple" in fruits) # check whether this exist in out collection


# set = {} Random/Unordered & immutable, but add/remove ok, no duplicate

fruits = {"Apple","Orange","Banana"}

# print(dir(fruits)) # to check methods available
# print(help(fruits)) # for help of this collection
# print(len(fruits)) # check out the length of the collection
# print("Apple" in fruits) # check whether this exist in out collection

# fruits.add()
# fruits.remove("")
# fruits.pop()
# fruits.clear()

# Dictionaries

Std_Grades = {
    "Alice":99,
    "Bob":99,
    "Charlie":99
}

print(Std_Grades["Alice"])

num1 = int(input("\nEnter Number 1 :"))
num2 = int(input("\nEnter Number 2 :"))

print("\n1-Addition")
print("\n2-Subtraction")
print("\n3-Multiplication")
print("\n4-Division")

choice = int(input("\nEnter the choice : "))

if choice == 1:
  print(f"\nAddition = {num1+num2}")
elif choice == 2:
  print(f"\nSubtraction = {num1-num2}")
elif choice ==3:
  print(f"\nMultiplication = {num1*num2}")
elif choice ==4:
  print(f"\nDivision = {num1/num2}")


# Using List
number = ["","","","",""]
number[0] = int(input("\nEnter Number 1 :"))
number[1] = int(input("\nEnter Number 2 :"))
number[2] = int(input("\nEnter Number 3 :"))
number[3] = int(input("\nEnter Number 4 :"))
number[4] = int(input("\nEnter Number 5 :"))

print("\n1-Addition")
print("\n2-Subtraction")
print("\n3-Multiplication")
print("\n4-Division")

choice = int(input("\nEnter the choice : "))

if choice == 1:
  print(f"\nAddition = {number[0]+number[1]+number[2]+number[3]+number[4]}")
elif choice == 2:
  print(f"\nSubtraction = {number[0]-number[1]-number[2]-number[3]-number[4]}")
elif choice ==3:
  print(f"\nMultiplication = {number[0]*number[1]*number[2]*number[3]*number[4]}")
elif choice ==4:
  print(f"\nDivision = {number[0]+number[1]/number[2]/number[3]/number[4]}")


# Using List
num1 = int(input("\nEnter Number 1 :"))
num2 = int(input("\nEnter Number 2 :"))
number = (num1,num2)

print("\n1-Addition")
print("\n2-Subtraction")
print("\n3-Multiplication")
print("\n4-Division")

choice = int(input("\nEnter the choice : "))

if choice == 1:
  print(f"\nAddition = {number[0]+number[1]}")
elif choice == 2:
  print(f"\nSubtraction = {number[0]-number[1]}")
elif choice ==3:
  print(f"\nMultiplication = {number[0]*number[1]}")
elif choice ==4:
  print(f"\nDivision = {number[0]+number[1]}")

# Using DIct
var_dict = {
    "num1":int(input("\nEnter Number 1 :")),
    "num2":int(input("\nEnter Number 1 :"))
}


print("\n1-Addition")
print("\n2-Subtraction")
print("\n3-Multiplication")
print("\n4-Division")

choice = int(input("\nEnter the choice : "))

if choice == 1:
  result = {"result":var_dict["num1"]+var_dict["num2"]}
  print(f"\nAddition = {result}")
elif choice == 2:
  result = {"result":var_dict["num1"]-var_dict["num2"]}
  print(f"\nSubtraction = {result}")
elif choice ==3:
  result = {"result":var_dict["num1"]*var_dict["num2"]}
  print(f"\nMultiplication = {result}")
elif choice ==4:
  result = {"result":var_dict["num1"]/var_dict["num2"]}
  print(f"\nDivision = {result}")


# Getting Started with numpy
# Experiment on tabuler data
# Fast Compilation

import numpy as np
# 2. Basic Numpy array op

list_data = [1,2,3,4,5]

array_data = np.array(list_data)

# Now we can perform the operation on array

print(type(list_data))
print(type(array_data))
print("",array_data)
print("How many rows and col ",array_data.shape)
print("Size ",array_data.size)
print("Data type ",array_data.dtype)
print("MEan : ", array_data.mean())
print("Max : ", array_data.max())
print("Min : ", array_data.min())
print("Sum : ", array_data.sum())
print("Standard Deviation : ", array_data.std())
