#!/usr/bin/python
# -*- coding: utf-8 -*-

print('show me your name now,please~')
name = input('please enter your name:')
print('hello,',name)
print('1024 * 768 = ',(1024*768))
error = ""
print(error,r" \\t\\\ can't print, slash will be dounle show then can't translate ")
s= r"aa\nnn"
print(s)
print(r'\\t\\\\')
print(r'\n')
print(r'''line1\\\n
line2
line3''')
print('print(3>2) result:',3>2)
print('print(True) result:',True)
print('print(False) result:',False)
print('print(3<2) result:',3<2)
sex = input('man or woman or boy or girl:')
age = input('show me your age:')
ageInt = int(age)
if ageInt > 0:
    if ageInt < 18 :
        print('hi little ',sex,name)
    else:
        print('hay old ',sex,name)
else:
    print('plz enter the correct age')
a = u'中文'
print(a)
