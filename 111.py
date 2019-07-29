# -*- coding: utf-8 -*-

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-19))
# print('毒啊圣诞快乐')
import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x,y=move(100,100,60,math.pi/6)

# print(x,y)

# def fact1(n):
#     if n==1:
#         return 1
#     return n*(fact1(n-1))

# t= fact1(500)
# print(t)

# def fact(n):
#     return fact_iter(n,1)

# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)

# tt=fact_iter(20,1)
# print(tt)

# pp=fact(500)
# print(pp)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r=[]
# # n=3
# # for i in range(3):
# #     r.append(L[i])

# print(L[0:3:2])

# t= range(100)

# print(list(t))

# from collections import Iterable

# print(isinstance('abc',Iterable))

# def findMinAndMax(L):
#     if L == []:
#         return None, None
#     else:
#         min=max=L[0]
#         for a in L:
#             if a>max:
#                 max=a
#             if a<min:
#                 min=a
#         return min, max



# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败1!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败2!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败3!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败4!')
# else:
#     print('测试成功5!')

# import os 
# for d in os.listdir('c:/'):
#      print(d)


# # -*- coding: utf-8 -*-
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2=[]
# for l in L1:
#     if(isinstance(l,str)):
#         l=l.lower()
#         L2.append(l)

# print(L1)
# print(L2)

# g = (x * x for x in range(10))
# print(next(g)) 
# print(next(g)) 
# print(next(g)) 
# print(next(g)) 
# print(next(g)) 

# def fib(tt):
#     n,a,b=0,0,1
#     while n<tt:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# for t in fib(6):
#     print(t)




# def moveList(L,outL,num):
#     T=[]
#     n=0
#     for em in L:
#         if n<int(num):

#             if(em not in T):
#                 if(n==0 and outL[-1]==em):
#                     print('重复')
#                 else:
#                     T.append(em)
#                     n=n+1
#     return T
       
# L=['aa','aa','aa','bb','bb','bb','cc','dd','dd']

# outL=['aa']
# outL=moveList(L,outL,3)
# print(outL)      

# outL=moveList(L,outL,3)
# print(outL)      

# outL=moveList(L,outL,3)
# print(outL)      



# def moveList(L,outL,num):
#     T=[]
#     n=0
#     k=0
#     while n<num:
#         em=random.sample(L, 1)[0]
#         k=k+1
#         if(em not in T):
#             if(n==0 and outL[-1]==em):
#                   'aa'  
#             else:
#                 T.append(em)
#                 L.remove(em)
#                 n=n+1
#         if k>1000:
#             return T
#     return T

# import random
# L = ['aa','aa','aa','bb','bb','cc']
# outL=['e']
# outL=moveList(L,outL,6)
# print(outL)
