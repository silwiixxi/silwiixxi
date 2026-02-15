#301
def check_number(number):
    n = abs(number)
    while n > 0:
        if (n % 10) % 2 != 0:
            print("Not valid")
            return
        n //= 10
    print("Valid")
num = int(input())
check_number(num)

#302
def isUsual(num):
    if num <= 0:
        return False
    for p in [2, 3, 5]:
        while num % p == 0:
            num //= p
    return num == 1
n = int(input())
print("Yes" if isUsual(n) else "No")

#303
codes={"ONE":"1","TWO":"2","THR":"3","FOU":"4","FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9","ZER":"0"}
rev_codes={v:k for k,v in codes.items()}
s=input()
for op in "+-*":
    if op in s:
        a,b=s.split(op)
        break
def decode(x):
    return int("".join(codes[x[i:i+3]] for i in range(0,len(x),3)))
def encode(x):
    return "".join(rev_codes[d] for d in str(x))
a_num=decode(a)
b_num=decode(b)
if op=="+":res=a_num+b_num
elif op=="-":res=a_num-b_num
else:res=a_num*b_num
print(encode(res))

#304
class StringHandler:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
obj = StringHandler()
obj.getString()
obj.printString()

#305
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
n = int(input())
s = Square(n)
print(s.area())

#306
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
l, w = map(int, input().split())
r = Rectangle(l, w)
print(r.area())

#307
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
p1 = Point(x1, y1)
p1.show()
p1.move(x2, y2)
p1.show()
p2 = Point(x3, y3)
print(f"{p1.dist(p2):.2f}")

#308
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance
b, w = map(int, input().split())
acc = Account("Owner", b)
print(acc.withdraw(w))

#309
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
r = int(input())
c = Circle(r)
print(f"{c.area():.2f}")

#310
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
name, gpa = input().split()
s = Student(name, float(gpa))
s.display()

#311
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)
a1, b1, a2, b2 = map(int, input().split())
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)
res = p1.add(p2)
print(f"Result: {res.a} {res.b}")

#312
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def total_salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects
    def total_salary(self):
        return self.base_salary + 500 * self.completed_projects
class Intern(Employee):
    pass
data = input().split()
role = data[0]
if role == "Manager":
    emp = Manager(data[1], int(data[2]), int(data[3]))
elif role == "Developer":
    emp = Developer(data[1], int(data[2]), int(data[3]))
else:
    emp = Intern(data[1], int(data[2]))
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")

#313
from math import isqrt
nums = list(map(int, input().split()))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, isqrt(n)+1))
primes = list(filter(is_prime, nums))
print(" ".join(map(str, primes)) if primes else "No primes")

#314
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    op = input().split()
    if op[0] == "add":
        arr = list(map(lambda a, x=int(op[1]): a + x, arr))
    elif op[0] == "multiply":
        arr = list(map(lambda a, x=int(op[1]): a * x, arr))
    elif op[0] == "power":
        arr = list(map(lambda a, x=int(op[1]): a ** x, arr))
    elif op[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))
print(*arr)