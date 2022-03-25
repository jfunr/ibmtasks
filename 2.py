# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:53:53 2018

@author: Mary Paccha
"""
# 2.1 Values and types
print('2.1 Values and types\n')

print(4)

print(type(40))

print(type("Hello"))
print(type(3.21))

print(type('12'))
print(type('23.65'))

print('\n2.2 Variables')

message='and now for something completely different'
n=17
pi=3.14

print("\n",message,n,pi)

#no escribir con 0 al principio
#print(01)
print(10)

print('\n2.3 VARIABLE NAMES AND KEYWORDS')

#to begin variable names with a lowercase letter, not number

v1=12
print('\nv1=',v1)

my_name='doni'

#review keywords

print('\n2.4 STATEMENTS\n')

#A statement is a unit of code that the Python interpreter can execute

print("ne")

x=2
print("x=",x)


print('\n2.5 OPERATORS AND OPERANDS\n')

print(20+32)

hour=10
print(hour-1)

print(50**2)

print((5+9)*(15-7))

minute=59
print(minute/60)

print('\n2.6 EXPRESSIONS\n')

#An expression is a combination of values, variables, and operators

x2=12
print(x2+3)


# 2.7 order of operations' PEMDAS
print("\n2.7 order of operations PEMDAS\n")
#P parentesis E exponential M multiplication D division A addition S substraction

print("2*(3-45)=",2*(3-45))
print('(2-1)*(10-7)=',(2-1)*(10-7))

print("2**2=",2**2)

print('2*3-1=',2*3-1)

print('2/2*pi=',2/2*pi)

#2.8
print('\n2.8 String Operations\n')
# + means concatenation

first='nuevo'
second='film'
print('first+second=',first+second)

print('3*second=',3*second)

# 2.9
print('\n2.9 Comments')
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60
print("percentage=",percentage)


print('\n2.10 Debugging')

print('1/(2pi)=',1/(2*pi))

print('\n2.12 Exercises')
print('Ex 2.3')

width=17
height=12.0
delimeter='.'

# 1
print('width/2=',width/2)
print('type(width/2)=',type(width/2))

# 2
print('width/2.0=',width/2.0)
print('type(width/2)=',type(width/2.0))

# 3
print('height/2=',height/3)
print('type(height/2)=',type(height/3))

# 4
print('1+2*5=',1+2*5)
print('type(1+2*5)=',type(1+2*5))

# 5
print('delimeter*5=',delimeter*5)
print('type(delimeter*5)',type(delimeter*5)) 

print('Ex 2.4')

# 1

r=5
print('volume=',(4*pi*r**3)/3)

# 2
p1=24.95
print("p final 60 copies=",24.95*.4+3+59*(24.95*.4+3+.75))

# 3












