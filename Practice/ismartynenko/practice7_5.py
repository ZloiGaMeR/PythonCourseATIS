import re

with open("../README.md", "r", encoding="utf-8") as f:
    text = f.readlines()
    regexp = []
    for i in text:
        matchObj = re.findall(r'git [a-z]+ ?[-_:/.@A-z]* ?[_a-z]*[ "А-я]*', i)
        if len(matchObj) != 0:
            regexp.append(matchObj)
    print(regexp)
