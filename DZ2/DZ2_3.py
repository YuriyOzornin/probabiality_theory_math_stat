from os import system
from math import factorial
system("cls")

'''
Монету подбросили 144 раза. Какова вероятность, что вероятность, что орел выпадет ровно 70 раз?

'''


def probability(n, k, p):  # формула Бернулли
    formula = factorial(n)/(factorial(k)*factorial(n-k))
    return formula*(p**k)*(1-p)**(n-k)


n = 144
k = 70
p = 0.5


print(
    f'Вероятность того, что орел выпадет ровно 70 раз = {probability(n,k,p):.5f} -> {probability(n,k,p)*100:1.2f}%')
