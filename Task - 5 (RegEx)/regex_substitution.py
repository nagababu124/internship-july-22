# -*- coding: utf-8 -*-
"""Regex Substitution

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zPcJjmJhFoptUB0xZX1AjEnG-RyYaff
"""

import re
for _ in range(int(input())):
    code = input()
    
    while ' && ' in code or ' || ' in code:
        code = code.replace(" && ", " and ").replace(" || ", " or ")
    
    print(code)