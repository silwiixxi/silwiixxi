#Python Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

#Python Generators
def my_generator():
  yield 1
  yield 2
  yield 3
for value in my_generator():
  print(value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1
for num in count_up_to(5):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

total = sum(x * x for x in range(10))
print(total)

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b
gen = fibonacci()
for _ in range(100):
  print(next(gen))

def echo_generator():
  while True:
    received = yield
    print("Received:", received)
gen = echo_generator()
next(gen) 
gen.send("Hello")
gen.send("World")

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close()

#Python Dates
import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#Python Math
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = pow(4, 3)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) 
print(y)

import math
x = math.pi
print(x)

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

