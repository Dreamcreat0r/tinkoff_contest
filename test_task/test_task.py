lst = ["Мама", "авТо", "гриБ", "Яблоко", "яБлоко", "ябЛоко", "яблОко", "яблоКо", "яблокО", "агент007", "стриж", "ГТО", "Три богатыря"]

def checkregister(s):
    k = 0
    for letter in s:
        if letter.isupper():
            k += 1
    if k == 1:
        return 1
    else:
        return 0

for s in lst:
    if s.isalpha()==1:
        if checkregister(s) == 1:
            print(s)
