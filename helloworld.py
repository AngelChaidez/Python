#!/usr/bin/env python3.11
print("Hello world")
 
def square(x):
    return x * x

def power(x, y):
    return x ** y

x = input("Enter a number for x: ")
y = input("Enter a number for y: ")

print("X squared is", square(float(x)))
print("Y squared is", square(float(y)))

print("X to the power of Y = ", power(float(x), float(y)))
