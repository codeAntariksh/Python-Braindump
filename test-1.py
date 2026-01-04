# a=10
# b="name"
# c,d,e='A',36,True
# print(a,b,c,d,e)
# print(type(a))
# print(type(c))
# f=[1,2,"abcd00",36.56,False]
# print(f)
# print(type(f))
# a=b=c=79
# print(a+b-c)
# print(a,',',b,',',c)
# print(a.__sizeof__())

## Python Data Types
#Integer Values
# a=15
# b=3646554568841
# print(type(a)," ",type(b))
# print(a.__sizeof__())
# print(b.__sizeof__())
#Float Values
# a=1.963e-4
# b=25.63E9
# print(a,b)
# print(type(a),b.__sizeof__())
# c=True
# d=bool(35)
# print(d)
# print(int(d))
# Complex Data Type
# a=complex(15,43e-6)
# b=336+45.29j
# c=bool("")
# print(a,b,c,b.__sizeof__(),type(a))
# print(a.real,b.imag)
# abc=163+45.36j
# print(abc.__sizeof__(),type(abc))

#Integer Literals
# a=15_36_4_26_78
# b=12_5.36_7
# print(a,type(a))
# print(b)
# A=12_.32 --> Invalid Decimal Literal

# Complex Literals
# a=complex(126_62,12_6_.3_4)
# print(a)

#LITERALS & NUMBER SYSTEM
# In terms of Complex Numbers only real part can be displayed like such
# A=0b11011101
# print(int(A))
# C1=int(0XABC15E)
# print(C1)

# a=complex(int(input("Enter Real Part:")),float(input("Enter Imag Part:")))
# print(a,a.__sizeof__())
# c=input("ENTER A:")
# d=input("ENTER B:")
# e=c+d
# print(e,type(c),type(d))
# a=26
# b=bool(":+LOVE")
# c=a+b
# print(c)
# a=0x15A+156j
# b=0b1101101+45.36j
# print(a+b)

# TypeCasting
# c="45+54.36j"
# print(complex(c))
# d=int(52.346_7)
# print(d)
# e=0o156
# print(int(e))

# Base Conversions
#bin(),oct(),hex() can only be derived from integers
# a=13564
# print(bin(a),oct(a),hex(a))
# b="0x135Ac"
# c=0b1101001
# d=0o10156
# print(int(c),int(b,16),int(d))
# f=0b110101
# g="0x12ACe"
# print(int(f),int(g,16))

# a=56
# b=2
# print(a**b)
# print(a//b)
# print(a%b)
# print(a/b)
# print(a*b)

# a=5+4j
# b=4+3j
# print(a/b)
# print(a*b)
# print(a**b)
# a="hello"
# b="hihihi"
# print(a+b*3)
#for Complex datatype //floor div and %mod operator doesn't carry any meaning

#Assignment Operators
# a=46
# b=3
# a+=b
# print(a)
# a-=b
# print(a)
# a//=b
# print(a)
# a%=b
# print(a)
# a**=b
# print(a)
# a/=b
# print(a)

# QuadratiC EQUATIONS
# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
# x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
# print("x1=",x1,"x2=",x2)

# # Conditional Logic
# year=int(input("Enter a year:"))
# if((year%4==0 and year%100!=0) or year%400==0):
#     print(year,"is a Leap year")
# else:
#     print(year,"is not a Leap Year")

# alphabet=input("Enter the Alphabet:")
# if(alphabet=='a' or alphabet=='A' or alphabet=='e' or alphabet=='E' or alphabet=='i' or alphabet=='I' or alphabet=='o' or alphabet=='O' or alphabet=='u' or alphabet=='U'):
#     print("Vowel")
# else:
#     print("Consonant")

# String Comparisions
# a1=input("Enter Str1=")
# a2=input("Enter Str2=")
# if(a1>a2):
#     print(a1,'>',a2)
# else:
#     print(a2,'>',a1)

# s1="true"
# s2="true"
# print(s1==s2)

# DataType Comparisions & Short-Circuit Conditions
# print("abc">"abcd")
# print(45+36j==45+424j)
# i=1
# j=2
# if(i<j or ++i==j):
#     print("")
# print(i,j)

# Chaining Comparisions
# a=10
# b=5
# c=12
# d=4
# print(a<b<c>d)

# a="hello"
# b="hello"
# print(a is b)
# print(a is not b)
# print(id(a),id(b))

# a=3
# b=9
# print(format(a,"b"))
# print(a,"|",b,"is=",a|b)
# print(a,"&",b,"is=",a&b)
# print(a,"^",b,"is=",a^b)

# Looping
# i=0
# while(True):
#     print(i)
#     i+=1
#     if(i==10):
#         break

# n=int(input("Enter the number:"))
# original=n
# sum=0
# while(n>0):
#     sum=sum*10+(n%10)
#     n//=10
# if(sum==original):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# n=1
# while(n<4):
#     print(n)
#     n+=1
# else:
#     print("Loop End")
# print("Termination of Programme")

# For Loop
# for i in range(1,6,1): #for(i=1;i<6;i++)
#     print(i)
# s1="python"
# for x in s1:
#     print(x)

# Fibonacci Series
# 0 1 1 2 3 5 8
# n=int(input("No of terms:"))
# a=0
# b=1
# for i in range(1,n+1,1):
#     if(i==1):
#         print(a)
#     elif(i==2):
#         print(b)
#     else:
#         print(a+b)
#         b=a+b
#         a=b-a

# n=3
# for i in range(1,n+1,1):
#     print(i)
# else:
#     print(i)

# day=int(input("Day no:"))
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid Day Number")

# Python Essentials
# A = 'z';
# print(ord(A))
# print(chr(122))
# print("\u0905") #Unicode

# print("Hello\nWorld")
# print("Alex\'s")
# print("Hello","World",sep=' ',end=" ")
# print("Python")
# item="Doll"
# price=36.75
# print("The price of %s is %d"%(item,price),end=" ")
# buyer="Ratan"
# print("and %s bought this"%(buyer),end=" ")
# print("Again re-affirming")
# print("The price of {} is {}".format(item,price),end=" ")
# print("The buyer is {}".format(buyer))

#Regular Expressions
# import re
# print(re.findall("abcdefc c","c"))

#List
# L1 = [1,2,3,"abcd"]
# for i in range(0,4):
#     print(L1[i],end=" ")
# print("")
# L1.append("IIT")
# L1.remove(2)
# for i in range(0,4):
#     print(L1[i],end=" ")
# print("")
# L1.append([4,5])
# print(L1[::-1])
# print(L1[0::2])

# L = [1,2,3,4,'Hii']
# print(L+[5])
# B = [5,6,7,8]
# print(L+B)
# L.extend(B)
# print(L)

# list1=[1,2]
# list2=list1*3
# print(list2)
# print(list1>list2)

# list1=["red","blue","green"]
# for x in list1:
#     print(x,end=" ")
# for i in range(0,3):
#     print(list1[i],end=" ")

#Nested Lists
# l1=[[1,2,3,4],[5,6,7,8],[9,10,11,12,13],[14,15,16]]
# for i in range(0,4,1):
#     for x in range(0,3,1):
#         print(l1[i][x],end=" ")
#     print("\n")

# Adding and Removing ELements from a List
# l1 = [1,2,3,4,5]
# l1.append(7) # 1 2 3 4 5 7
# l1.extend('python')
# l1.extend(["snake"])
# l1.insert(0,"abcd0")
# print(l1)
# l2 = l1.copy()
# print(l2)

# Deleting ELements from a List
# l1 = [1,2,3]
# l1.pop(2)
# print(l1)
# l1.extend([4,5,6,7])
# l1.pop()
# print(l1)
# l1.remove(4)
# print(l1)
# del l1[3]
# print(l1)

# l1 = [1,2,3,4,5,6,7,8,9]
# l1.sort(reverse="True")
# print(l1)
# print(l1.index(7,0,10))

# l2 = ["apple","banana","grape","cat"]
# l2.sort(key=len,reverse="True")
# print(l2)
# l2.sort(key=str.lower,reverse="False")
# print(l2)

# l1 = [x.capitalize() for x in "Python"]
# l2 = [x for x in '12a3Bh4Y&' if x.isalpha()]
# l3 = [x+1 for x in range(0,5)]
# print(l2)
# print(l3)
# print(l1)

# Tuple
# t1 = (1,2,3,5)
# t2 = (*(x for x in range(0,3)),)
# print(type(t2),type(t1),end=" ")
# print(t1,t2)
# t3 = (1)
# t4 = (1,)
# print(type(t3),type(t4))

# t1 = tuple(x.capitalize() for x in 'python')
# print(t1)
# t2 = (*(x for x in range(1,6) if x%2==0),)
# print(t2)
# t3 = tuple(range(1,6))
# print(t3)
# print(t3[0::2])

# Packing & Unpacking in Tuple
# t1 = tuple(range(1,5))
#UnPacking
# a,b,c,d = t1
# print(a,b,c,d)

#Packing 
# T1 = 1,2,3,'a',True
# print(T1)
# print(3 in T1)

# T2 = tuple(range(4,9))
# a,*v,d = T2
# print(a,v,d)

