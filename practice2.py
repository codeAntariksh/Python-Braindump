## Python Basics
# price=complex(float(input("Enter Real Part=")),float(input("Enter Imaginary Part=")))
# print(price)

# a = int(input("Enter a = "))
# b = bool(input("Enter b = "))
# c = a + b
# print(a,'+',b,"=",c)

# a = complex(int(input("Enter Real Part")),int(input("Enter Imag Part")))
# b = complex(int(input("Enter Real:"),int(input("Enter Imag Part:"))))
# print(a+b)
# a = 25
# b = "25"
# print(id(a))
# print(id(b))
# print(a is b)

# a,b,c,d = 25,36,78,96
# print(a>b==c<d)

# s1 = "hard"
# s2 = "hardware"
# print(s1>s2)

# age = int(input("Enter Your Age:"))
# if(age>18):
#     print("Can Vote")
#     print("Proceed")
# elif(age==18):
#     print("Just Passed age limit")
#     print("Proceed")
# else:
#     print("Not eligible to Vote")

# for i in range(15):
#     print(i)

# i = 0
# while(i<15):
#     print(i)
#     i+=1
# s1 = "Hello"
# for x in s1:
#     print(x.capitalize())

# a = 0
# b = 1
# n = int(input("Enter No of Terms:")) 
# for i in range(0,n+1,1):
#     if(i<=1):
#         print(i,end=" ")
#     else:
#         b = a + b
#         print(b,end=" ")
#         a = b - a

# for i in range(1,5):
#     pass
# else:
#     print(2)

# n = int(input("ENTER DAY NO:"))
# match n:
#     case 0: print("Monday")
#     case 1: print("Tuesday")
#     case _:
#         print("Invalid")

# print(ord('A'))
# print(chr(122))

# print("Hii","Antarikshya",sep=" ",end=" ")
# print("Hello Jee")

# C Style Printing
# name = str(input("Enter Name:"))
# age = int(input("Enter Age:"))
# print("My Name is {} and age is {}".format(name,age))
# print("My Name is %s and age is %d"%(name,age))

# g = 5.51
# print("Outside is:",g)

# def fun():
#     g = 10
#     print("Local-",g)
#     print("Global-",globals()['g'])

# fun()

# def volume_of_cuboid(length,breadth,height):
#     vol = length*breadth*height
#     return vol
# v = volume_of_cuboid(10,15,20)
# print("Volume is=",v)

# def square_func(len=10,b=20):
#     return len*b
# a = square_func(5)
# print(a)

# def volume(len,bre,hei):
#     print(len,hei,bre,sep=",",end="\n")

# print(volume(bre=10,hei=25,len=12))

# Positional and Keyword Only Arguments
# def fun(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)
#     pass
# fun(12,13,c=25,d=36,e=14,f=23)


# def marks(a,b,c):
#     total = a + b + c
#     avg = total/3
#     return total,avg

# s = marks(10,15,30)
# for i in s:
#     print(i)


# Iterators
# list1 = [10,20,30,41]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))

# d1 = {'a':"abc",'b':"bcd"}
# it = iter(d1)
# for i in range(len(d1)):
#     key = next(it)
#     print(key,':',d1[key])

# r = range(4)
# print(r)

# r = range(4)
# it = iter(r)
# for i in r:
#     print(next(it))

# def myrange(n):
#     i = 0
#     while(i<n):
#         yield i
#         i+=1

# m = myrange(5)
# print(type(m))



list1 = ["p","y","p"]
list1.remove("p")
print(list1)