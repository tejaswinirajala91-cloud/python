     #Display Personal Details Using Variables
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
print(name)
print(age)
print(height)

#Personalized Greeting
name = input("Enter your name:")
print(F"Hello,{name}!")

#add two numbers read as string
a = input("Enter the first number:")
b = input("Enter the second number:")
a = int(a)
b = int(b)
total = a+b
print(total)

#float to integer conversion
n = float(input("Enter the number: "))
print(n)
new = int(n)
print(new)

#sum using arithmetic operator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(a+b)

#area of rectangle
length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
area = length*breadth
print(area)

#Quotient and Remainder
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
q = a/b
r = a%b
print(q)
print(r)

#power calculation
base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))
print(base**exponent)

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))
total = n1+n2+n3
avg = total/3
print(avg)

#greater than comparison
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a>b
print(c)

#equality check
#same-true
#different-false
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
print(n1==n2)

#both numbers positive check
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
print(n1>0 and n2>0)

#atleast one even number
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
print(n1%2==0 or n2%2==0)
     
#logical NOT on a condition
num = int(input("Enter the num:"))
print(not(num>0))

#augmented assignment operators
a = int(input("Enter a:"))
a = a+5
a = a*2
a = a-3
print(a)

#exchange values of two variables
a = int(input("Enter a:"))
b = int(input("Enter b:"))
  
temp = a
a=b
b = temp
print(a)
print(b)

a = a+b
b = a-b
a = a-b
print(a)
print(b)

a = a^b
b = a^b
a = a^b
print(a)
print(b)

a = a*b 
b = a/b
a = a/b
print(a)
print(b)

a,b = b,a
print(a)
print(b)

#calculate simple interest
principle = float(input("Enter loan amount:"))
rate = float(input("Enter rate:"))
time = float(input("Enter time:"))
si = (principle*rate*time)/100
print(si)

#temperature conversion
c = float(input("Enter celsius:"))
f = (c*9/5)
print(f)

#check divisibility by 3 and 5
n = int(input("Enter n:"))
print(n%3==0 and n%5==0)

#sum of digits of a two-digit number
num = int(input("Enter num:"))
tens = num//10
units = num % 10
total = tens + units
print(total)




