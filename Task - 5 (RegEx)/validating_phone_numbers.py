# -*- coding: utf-8 -*-
"""Validating phone numbers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zPcJjmJhFoptUB0xZX1AjEnG-RyYaff
"""

import re
for _ in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')