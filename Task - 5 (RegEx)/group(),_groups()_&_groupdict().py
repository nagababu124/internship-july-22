# -*- coding: utf-8 -*-
"""Group(), Groups() & Groupdict()

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zPcJjmJhFoptUB0xZX1AjEnG-RyYaff
"""

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)