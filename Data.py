#31 January 2021

    import sys

a = 11**45678
print(a)
print(type(a))
print(sys.getsizeof(a))



"""
x = 11
print(x)#11
print(type(x))#<class 'int'>
print(id(x))#it is used to display unique id of variable(ie address)

y = 3.14
print(y)#3.14
print(type(y))#<class 'float'>
print(id(y))#it is used to display unique id of variable(ie address)

z = 3+4j
print(z)#(3+4j)
print(type(z))#<class 'complex'>
print(id(z))#it is used to display unique id of variable(ie address)

str = "hello"
print(str)#(3+4j)
print(type(str))

a = True
print(a)#(3+4j)
print(type(a))

arr = [10,20,30,40]
print(arr)#(3+4j)
print(type(arr))

arr1 = (10,20,30,40)
print(arr1)#(3+4j)
print(type(arr1))

arr2 = {10,20,30,40}
print(arr2)#(3+4j)
print(type(arr2))

arr3 = {"a":10,"b":20,"c":30,"d":40}
print(arr3)#(3+4j)
print(type(arr3))

k = None
print(k)
print(type(k))

output
11
<class 'int'>
1963506362992
3.14
<class 'float'>
1963512474160
(3+4j)
<class 'complex'>
1963512473584
hello
<class 'str'>
True
<class 'bool'>
[10, 20, 30, 40]
<class 'list'>
(10, 20, 30, 40)
<class 'tuple'>
{40, 10, 20, 30}
<class 'set'>
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
<class 'dict'>
None
<class 'NoneType'>
"""
