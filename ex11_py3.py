# -*- coding: utf-8 -*-

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print("So you are %r old, %r tall and %r heavy." % (
    age, height, weight))

while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i, end=" ")
