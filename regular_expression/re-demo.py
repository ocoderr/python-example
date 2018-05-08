# -*- coding: utf-8 -*-
import re

f = open('demo.txt', 'r')
html = f.read()
f.close()

title = re.search('<title>(.*?)</title>', html, re.S).group(1)
print(title)

links = re.findall('href="(.*?)"', html, re.S)
for each in links:
    print(each)

ul_text = re.findall('<ul>(.*?)</ul>', html, re.S)[0]

the_text = re.findall('">(.*?)</a>', ul_text, re.S)
for ery in the_text:
    print(ery)

for i in range(2,5):
    link = re.sub('pageNum=\d+','pageNum=%d'%i,'pageNum=1',re.S)
    print(link)