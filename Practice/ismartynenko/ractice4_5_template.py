fake_site = {"{KEYWORD}": "car", "{PHRASE}": "reliable", "{DESC}": "powerfully"}
text = 'It is the best {KEYWORD} in the World. The most {DESC} on the planet. LADA is {PHRASE} {KEYWORD} =)'
print(text)
lst = text.split()
for i in range(len(lst)):
    if lst[i] in fake_site:
        lst[i] = fake_site.get(lst[i])

lst = " ".join(lst)
print(lst)
