import os
import re


os.chdir(os.pardir)
os.chdir(os.pardir)
pth = os.path.join(os.path.abspath(os.curdir), 'README.md')

fle = open(pth, 'rb')
by = fle.read()
st = by.decode(encoding='UTF-8')
res = re.findall(r'git [a-z]+[\s]*[a-zA-Z/.:@]+', st)

for rs in res:
    print(rs)
