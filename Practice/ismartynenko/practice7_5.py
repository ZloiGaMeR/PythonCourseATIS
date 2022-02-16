import re

with open("../README.md", "r", encoding="utf-8") as f:
    text = f.readlines()
    regexp = []
    after_clean = []
    for i in text:
        matchObj = re.findall(r'git [a-z]+ ?[-_:/.@A-z]* ?[_a-z]*[ "А-я]*', i)
        if len(matchObj) != 0:
            for match in matchObj:
                after_clean = match.rstrip()
                if after_clean.count('"') == 1 and after_clean.endswith('"'):
                    after_clean = match.rstrip('"')
            regexp.append(after_clean)

print(regexp)
