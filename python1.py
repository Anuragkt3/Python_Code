# Sum of two numbers

num1 = float(input("First number:"))
num2 = float(input("Second number:"))

sum = num1 + num2
print("the sum is",sum)

# Square root of a number

num = int(input("Enter the number: "))
sr = num**(1/2)
print("the square root is",sr)

# Method 2

import math
num = int(input("Enter the number"))
sr = math.sqrt(num)
print("the square root is",sr)  

# How to Calculate Area of Triangle
height = float(input("the height is:"))
base = float(input("The base is:"))

area = 0.5*height*base
print("the area is",area) 

# Swap Two Variables in Python

x = 13
y = 12
temp = 14
x = y
print("The value of x is :",x)
y = temp
print("The value of y is :",y)

# Method2
x = 12
y = 13
x,y = y,x
print("the value of x is",x) 

#km to miles
km = float(input("Enter the value in km:"))
miles = 0.621371*km
print("km is",miles ) 

# check wether a number is positive or negative
num = float(input("Enter a number:"))
if num > 0:
    print("the number is positive")
elif num==0:
    print("it is 0")
else:
    print("it is negative")        

# check wether a number is odd or even
num = float(input("Enter the number"))
if num % 2 == 0:
    print("it is even")
else:
    print("it is odd")    

# Cleck for leap year

year = int(input("Enter the year: "))
if (year%400==0) and (year%100==0):
    print("The year is Leap year")
elif (year%4==0) and (year%100!=0):
    print("The year is leap year")
else:
    print("The year is not leap")        




























