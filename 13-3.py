# -*- coding: utf-8 -*-
import random
import string
import sys
import os

path = 'C:\\'
os.chdir(path)
os.mkdir('tên thư mục')
x = ''
y = ''
z = 0
n = random.randint(1024**2,1024**3)
m = 1024*1000
while n > m:

    while sys.getsizeof(y) <= m:
        x = random.choice(string.ascii_letters)
        y = y + x
    y = y[:-1]
    t = "C:\\tên thư mục\\tên tập tin" + str(z) + ".txt"
    with open(t, 'w', encoding='utf-8') as f:
        f.write(y)
        f.close()
    n = n - sys.getsizeof(y)
    z = z + 1
    y = ''
x = ''
y = ''
q = "C:\\tên thư mục\\tentaptincuoicung" + ".txt"
while sys.getsizeof(y) <= n:
    x = random.choice(string.ascii_letters)
    y = y + x
with open(q, 'w', encoding='utf-8') as f:
    f.write(y)
    f.close()
        
    
        
        



