# Họ và tên:Huỳnh Thanh Hải
# MSSV:20064981
# Lớp học phần - Nhóm TH: 420300207402
# 1. Hello world!
# 2. Program to Add Two Numbers## Add Two Numbers
import math
num1 = 1.5
num2 = 6.3

### START CODE HERE ### 
# Add two numbers

sum = num1 + num2

# Display the sum
print(sum)##  Add Two Numbers With User Input# Store input numbers

num1 = float(input("Enter num1: "));
num2 = float(input("Enter num2: "));

### START CODE HERE ### 

# Add two numbers

sum = num1 + num2

### END CODE HERE ###

# Display the sum
print(sum);
# 3. Program to Find the Square Root# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
num = float(input('Enter a number: '))

# calculate the square root 

squareRoot = math.sqrt(num)

# print the value of the square root
print(squareRoot)
# 4. Program to Calculate the Area of a Triangle
#s = (a+b+c)/2

#area = √(s(s-a)*(s-b)*(s-c))
### START CODE HERE ### 

# take inputs from the user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


# calculate the semi-perimeter
s = (a + b + c)/2

# calculate the area
area = math.sqrt(s*(s - a)*(s - b)*(s - c))

### END CODE HERE ###

print('The area of the triangle is %0.2f' %area)
# 5. Program to Solve Quadratic Equation ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0import cmath

### START CODE HERE ### 
import cmath
# take inputs from the user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate the discriminant
d = pow(b, 2) - 4*a*c

# find two solutions using square root for real/complex number
sol1 = (-b + math.sqrt(d))/(2*a)
sol2 = (-b - math.sqrt(d))/(2*a)
### END CODE HERE ###

print('The solution are {0} and {1}'.format(sol1,sol2))
# 6. Program to Swap Two Variables
# To take inputs from the user

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

# create a temporary variable and swap the values

temp = num1
num1 = num2
num2 = temp

# Print the c=value of x, y after swapping
print("value of num1, num2 after swapping: %0.2f, %0.2f", num1, num2)

### START CODE HERE ### 
# writing code to get the address (in RAM) of x, y, temp through the built-in function id()

print(id(num1))
print(id(num2))
print(id(temp))

### END CODE HERE ###
# 7. Program to Generate a Random Number https://docs.python.org/3/library/random.html
# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,9))

# Uncomment to try different function in random module
print(random.randrange(9))
# print(random.randrange(3,9))
# print(random.random())
# print(random.uniform(a,b))
# 8. Program to Convert Kilometers to Miles 1 km = (1/1.609344) mi = 0.62137119 mi
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
### START CODE HERE ### 
# writing code to convert miles to kilometers
kilometers = miles/conv_fac
print('%.2f miles is equal to %.2f kilometers' %(miles, kilometers))
### END CODE HERE #### 
#9. Program to Convert Celsius To Fahrenheit
#T(°F) = T(°C) × 1.8 + 32
### START CODE HERE ### 
# Taking celsius input from the user

celsius = float(input('Enter celsius: '))

# conversion factor

conv_fac = 1.8

# calculate Fahrenheit

fah = (celsius - 32)/conv_fac

# print result
print('Fahrenheit' + fah)
### END CODE HERE ###