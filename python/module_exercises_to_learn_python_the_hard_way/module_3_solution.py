#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename: module_3_solution.py

# Practice exercise for exercises 15-17
# from the book Learn Python the Hard Way (third edition)

# Truncate the given file by solving the two TODO sections.
#
# The idea is to read the file first and then truncate it afterwards.
#
# For more detailed documentation check the official Python3 docs:
# https://docs.python.org/3/library/io.html#module-io


test_file_name = "test_file.txt"

write_file = open(test_file_name, 'w')
write_file.write("THIS IS A TEXT LINE!\n")
write_file.close()

# TODO-1: Initialize the access_mode for processing the file appropriately!
access_mode = 'r+'

truncate_file = open(test_file_name, access_mode)

file_len = len(truncate_file.read())

if file_len:
    print("%d bytes were read from the file: %s"
          % (file_len, truncate_file.name))
else:
    raise RuntimeError("Could not read anything from the file "
                       "before truncate should happen...")

# TODO-2: Truncate the file...
truncate_file.seek(0)
truncate_file.truncate()
truncate_file.close()

# Check file after truncate:
read_file = open(test_file_name, 'r')
file_len = len(read_file.read())
read_file.close()

if file_len:
    raise RuntimeError("File should have been truncated!")
else:
    print("Well done!")
