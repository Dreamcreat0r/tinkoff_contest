n, t = input().split()  # n - кол-во этажей для посещения,     t - время, через которое bich уйдет
stages = input() # номера этажей для посещения
bich = int(input()) # номер в списке этажа на котором сидит bich

lst = stages.split() # переводим этажи в список
bich -= 1
bich = lst[bich]
bich = int(bich) # теперь в bich хранится не номер этажа в списке, а сам этаж
n=int(n)
t=int(t)
f1, f2 = 0, 0
# проверяем, можно ли начать с одного из концов
a = lst[0]
a = int(a)
from_low = bich - a
if from_low <= t:
    f1 = 1

b = lst[-1]
b = int(b)
from_up = b - bich
if from_up <= t:
    f2 = 1
allt = b - a

# если да:
if f1+f2 >= 1:
    print(allt)
else:
    # если нет:
    closest = min(from_low, from_up) # берем близжайший к bich конец
    allt += closest # и добавляем к общему числу этажей
    print(allt)

# в принципе, можно было не вводить так много перемнных, но для наглядности...
