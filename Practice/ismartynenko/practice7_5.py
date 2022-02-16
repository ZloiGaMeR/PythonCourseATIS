import re

with open("../README.md", "r", encoding="utf-8") as f:
    text = f.readlines()
    regexp = []
    for i in text:
        matchObj = re.findall(r'git [a-z]+ ?[-_:/.@A-z]* ?[_a-z]*[ "А-я]*', i)
        if len(matchObj) != 0:
            regexp += matchObj

clean_lst = []
for i in regexp:
    if i.count('"') == 1 and i.endswith('"'):
        clean_lst.append(i.rstrip('"'))
    else:
        clean_lst.append(i.rstrip())
print(clean_lst)
