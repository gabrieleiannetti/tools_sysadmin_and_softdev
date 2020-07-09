#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename: module_4_solution.py

# Practice exercise for exercises 18-24
# from the book Learn Python the Hard Way (third edition)


def add_numbers(arg1, arg2):
    return arg1 + arg2

def print_something(text):
    print("Hello... %s" % text)

def print_hello_world():
    print("Hello World!")

num1 = 34.643254353
num2 = 56.845345456
result = add_numbers(num1, num2)

print("Calculation: %s + %s = %s" % (num1, num2, result))
