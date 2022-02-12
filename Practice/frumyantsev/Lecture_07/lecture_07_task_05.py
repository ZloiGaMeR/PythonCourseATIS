import os
import re


os.chdir(os.pardir)
os.chdir(os.pardir)
pth = os.path.join(os.path.abspath(os.curdir), 'README.md')

fle = open(pth, 'rb')
by = fle.read()
st = by.decode(encoding='UTF-8')

res1 = re.findall(r' git [a-z][a-zA-Z\./:@\s_-]+[\" ]?' + r'\".*\"', st)
res2 = re.findall(r'\"git [a-z][a-zA-Z\./:@\s_-]+\"', st)
res3 = re.findall(r' git [a-z][a-zA-Z\./:@\s_-]+[^\r\n\d,\",\),\(,а-яА-Я,\s-]', st)

for rs in res1:
    print(f"{rs}")
for rs in res2:
    print(f"{rs}")
for rs in res3:
    print(f"{rs}")


