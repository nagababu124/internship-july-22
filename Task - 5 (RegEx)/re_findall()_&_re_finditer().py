# -*- coding: utf-8 -*-
"""Re.findall() & Re.finditer()

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zPcJjmJhFoptUB0xZX1AjEnG-RyYaff
"""

import re
m = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", input(), flags = re.I)
if m:
    for i in m:
        print(i)
else:
    print(-1)