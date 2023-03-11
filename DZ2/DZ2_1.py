from os import system
from math import factorial
system("cls")

'''
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз. 
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
'''


def probability(n, k, p):  # формула Бернулли
    formula = factorial(n)/(factorial(k)*factorial(n-k))
    return formula*(p**k)*(1-p)**(n-k)


n = 100
k = 85
p = 0.8


print(
    f'Вероятность того, что стрелок попадет в цель ровно 85 раз = {probability(n,k,p):.5f} -> {probability(n,k,p)*100:1.2f}%')
