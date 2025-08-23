def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-99))


def nop():
    pass

if age >= 18:
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

r = move(100, 100, 60, math.pi / 6)
print(r)

def power(x):
    return x * x

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * n
    return s

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

def enroll(name, gender, age = 6, city = 'BeiJing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=[]):
    L.append('END')
    return L

add_end([1,2,3])

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)

        
    