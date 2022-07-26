# -*- coding: utf-8 -*-
"""Validating Postal Codes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zPcJjmJhFoptUB0xZX1AjEnG-RyYaff
"""

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)