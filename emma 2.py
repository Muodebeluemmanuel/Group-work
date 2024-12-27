x=str(3)
y=int(3)
z=float(3)
print(x,y,z)

a=5
b="john"
print(type(a))
print(type(b))

#x="john"
#is the same as
#x='john'

v=4
V= "sal"
#V will not over write v

#x,y,z="orange", "banana", "cherry"
print(x)
print(y)
print(z)

#x=y=z="orange"
print(x)
print(y)
print(z)

fruits=["apple","banana","cherry"]
j, k, l=fruits
print(j)
print(k)
print(l)

s="python"
w="is"
r="awesome"
print(s,w,r)
print(s+w+r)

t=4
p=3
print(t+p)

m=5
n="gabriel"
print(m,n)

u="awesome"
def myfunc():
    print("python is"+ u)

myfunc()

def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is" + x)

x="fantastic"
def myfunc():
    global x
    x= "fanta"
myfunc()
print("python is" + x)

x= 1
y=24445551
z=-73536
print(type(x))
print(type(y))
print(type(z))
# float is used in decimal and also be scienific numbers with an "e" to indicate the power of 10
#complex numbers are written with a "j" as the imaginary part
x=3+5j
print(type(x))
# we can also convert from one type yo another with the int(),float(), and complex() methods
x=1
y=2.7
z=1j
#convert from int to float:
a=float(x)
#convert from float to int:
b=int(y)
#convert from int to complex:
c=complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,10))

print("it's alright")
print("he is called'johnny'")

for x in "banana":
    print(x)

a="hello, world!"
print(len(a))

txt="the best things in life are free!"
print("free"in txt)

print(10>9)
print(10==10)
print(10<9)

a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("hello"))
print(bool(15))
#x+y
#x-y
#x*y
#x/y
#x%y
#x**y
#x//y

#== equal
#!= not equal
#>   greater than
#<   less than
#>=  greater than or equal to
#<=  less than or equal to

thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist)
print(thislist[1])
print(thislist[-3])
print(thislist[-3:-1])
mylist=["apple","banana","cherry","kiwi"]
if "kiwi" in mylist:
    print("yes,'kiwi'is in the fruits list")
else:
    print("there is no kiwi")
# to change list 
mylist[1]="pineapple"
print(mylist)

#using for loop in list
for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

i=0
me=["faith","goodness","love"]
while i<len(me):
    print(me[i])
    i=i+1
for x in range(500,-1,-1):
    if x%2!=0:
        print(x)

