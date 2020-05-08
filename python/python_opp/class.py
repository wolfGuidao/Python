# class A():
#     NameErrore = "wwwroot"
#
#     def __init__(self, name):
#         print("i am __init__")
#         self.NameError = name
#         print(NameError)
#
#     def func(self):
#         print(self.NameErrore)
#
#
# a = A("wolf")

# a.func()

# print(A.__dict__)
# print(a.__dict__)

# print(a.NameError)
# print(A.NameErrore)

# class SS():
#     name = " "
#     Sum = 0
#
#     def __init__(self, _name, sum):
#         print("i am init")
#         self.name = _name
#
#         print(self.name)
#         self.Sum = sum
#         self.__class__.Sum += 1
#         print("当前class个数：%d" % self.__class__.Sum)
#
#     def func(self):
#         print(self.name)
#
#         print(self.Sum)
#         print(SS.Sum)
#         print(self.__class__.Sum)
#
#         print(id(self.Sum))
#         print(id(SS.Sum))
#
# s = SS("wolf", 100)
# s.func()
#
# # s1 = SS("peter")
# # s2 = SS("hell")
#
# print(SS.name)

# class SS():
#     Sum = 0
#     name = "wolf"
#
#     @classmethod
#     def Sumfunc(cls):
#         print("i am class mothod")
#         cls.Sum += 1
#         print("Sum : %d" % cls.Sum)
#         print(cls.__dict__)
#
# s = SS()
# s.Sumfunc()
# SS.Sumfunc()

# class SS():
#     __Sum = 0
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def pub(cls):
#         pass
#
#     @staticmethod
#     def sta(left, right):
#         print("i am static mothod")
#         print(SS.Sum)
#         print(left + right)
#
#     def __test__(self):
#         self.sta(1, 2)
#         print("i am text")
#
# s = SS()
#
# s.__test__()
#
# s.__Sum = -1
#
# print(s.__dict__)
# print(s.__Sum)

# class A():
#     a = 999
#     flag = 0
#
#     def __init__(self, _a):
#         self.a = _a
#
#     def func(self):
#         print("i am A()")
#
# class B(A):
#     b = 666
#     flag = 1
#
#     def __init__(self, _b, _a):
#         self.b = _b
#         # A.__init__(self, _a)
#         super(B, self).__init__(_a)
#
#     def test(self):
#         print(self.b, self.a)
#         # print(A.flag)
#         super(B, self).func()
#
# b = B(1, 2)
#
# b.test()
# b.func()

import re

# a = "C/C++ | Java | Python | Php | C# | Javascript"

# print(a.index("Python"))

# print(a.index("Phpp") > -1)
# print("Php" in a)

# print(re.findall("Pp", a))

# a = "@asf%da%nj%gasgaef   \n \tjqp49n&&g13___94*gjj&1g3!4g1"

# b = re.findall('\d+', a)

# c = re.findall('\D+', a)
# c = re.findall('a[es]f', a)
# c = re.findall('a[^e]f', a)
# c = re.findall('a[a-z]f', a)
# c = re.findall('\w', a)
# c = re.findall('[a-zA-Z0-9_]', a)
# c = re.findall('\W', a)
# c = re.findall('\s', a)
# c = re.findall('\S', a)

# print(b)
# print(c)

# a = "Python Php C/C++ Java Javascript"

# b = re.findall('[a-zA-Z]{3,9}', a)
# b = re.findall('')

# print(b)

# a = "pytho python python1 python11 pythonnnnnn11"

# *:0 - n
# b = re.findall('python*', a)

# ？：0 / 1
# b = re.findall('python?', a)

# +：1 - n
# b = re.findall('python+', a)

# print(b)

# qq = '5190391111111111111111111'

# b = re.findall('\d+', qq)
# b = re.findall('[0-9]{6,10}', qq)
# ^:start $:end
# b = re.findall('^\d{6,10}$', qq)
# print(b)

a = "PythonJavaC/C++PythonPythonJavaPythonJavaPythonPythonJava"

# b = re.findall('(Python){3}', a)
# b = re.findall('python.{1}', a, re.I | re.S)
# b = re.findall('pytho.', a)

# 替换
# b = re.sub('Java', 'Javascript', a, 1)

# a.replace('Java', 'Javascript')

# def func(data):
#     print(data)
#
# b = re.sub('Java', func, a)
# c = re.search()
# d = re.match()
#
# print(b)

# a = "abacadaeaf"

# b = re.compile('\w', a)

# print(b)

import json

# json_str = '[{"name":"wolf", "age":22}, {"name":"guidao", "age":32}]'
#
# a = json.loads(json_str)
#
# print(a)
# print(type(a))
#
# b = {"name": "wolf", "age": 13}
# print(b)

# print(a["name"])

# a = {'name': 'wolf', 'age': 12, 'flag': True}
#
# json_str = json.dumps(a)
#
# print(json_str)
# print(type(json_str))

# from enum import Enum
#
# class VIP(Enum):
#     yellow = 1
#     red = 2
#     black = 3
#
# print(VIP.yellow.value)
# print(VIP.yellow.name)
# print(type(VIP.yellow))
# print(type(VIP.yellow.name))

# a = 1, 2
# print(type(a))

# a = 1
# b = 2
#
# a, b = b, a
#
# print(a, b)

# def a():
#     print("i am A")
#
#     def b():
#         print("i am B")
#     b()
#     return b
#
# c = a()
# print(type(c))
# c()

# import time
#
# print(time.time())
#
#
# def func1(func):
#     def func2(*arg, **kw):
#         print(time.time())
#         func(*arg, **kw)
#     return func2
#
# @func1
# def function(arg1, arg2, **kw):
#     print("this is function" + arg1 + arg2)
#     print(kw)
#
# # f = func1(function)
# # f()
#
# @func1
# def function1(arg1):
#     print("this is function1" + arg1)
#
# function(" wolf ", " guidao ", a = 1, b = 2, c = "999")
# function1(" wolf ")

class A:
    def name(self):

        print("i am A")

class B(A):
    def name(self, name):
        print("i am B")


# a = A()
b = B()
b.name(1)
