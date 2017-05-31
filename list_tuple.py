#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
classmates = ['a','v','c','s','w','1',2]
print(classmates)  # ['a', 'v', 'c', 's', 'w', '1', 2]
classmates.pop() 
print(classmates)  # ['a', 'v', 'c', 's', 'w', '1']
print(classmates.pop(2))  # c
print(classmates)  # ['a', 'v', 's', 'w', '1']
print(len(classmates)) # 5
print(classmates.insert(2,';'))  #  insert的 返回值  为None

print(classmates) # ['a', 'v', ';', 's', 'w', '1']

L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
]
print(L[0][0]) # Apple
print(L[1][1]) # Python
print(L[2][2]) # Lisa

t = ('a','b','c','d',['A','B'])
print(t) # ('a', 'b', 'c', 'd', ['A', 'B'])
t[len(t)-1][0] = 'Z'
print(t) # ('a', 'b', 'c', 'd', ['Z', 'B'])
