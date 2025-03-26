#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Calculate the multiplication and sum of two numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum=a+b
pro=a*b
print("The Sum of two numbers are: ",sum)
print("The Product of two numbers are: ",pro)


# In[2]:


#2. Declare two variables and print that which variable is largest using ternary operators
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
lar= x if x>y else y
print("The Largest number is: ",lar)


# In[3]:


#3.Take input from the user (name, age, and city) and print it in a formatted string.
x=input("Enter your name: ")
y=int(input("Enter your age: "))
z=input("Enter your city: ")
print(f"My name is {x},I am {y} years old,I belong to {z} city")


# In[4]:


#4. Python program to find the area of a triangle whose sides are given
x=int(input("Enter the base of triangle: "))
y=int(input("Enter the height of triangle: "))
area=1/2*x*y
print("The Area of triangle is: ",area)


# In[5]:


#5.Write a Python program to check whether a number is even or odd
num=int(input("Enter any number: "))
if num%2==0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")


# In[6]:


#6.Find the square and cube of a given number.
num=int(input("Enter any number: "))
sq=num*num
cube=num*num*num
print("The Square root of the number is : ",sq)
print("The Cube root of the number is : ",cube)


# In[ ]:




