from math import factorial
from os import system
system("cls")

'''
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
Какова вероятность того, что 3 мяча белые? 
'''


def f_combination(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


probability = f_combination(5, 2)*f_combination(3, 0)/f_combination(8, 2) * f_combination(5, 1)*f_combination(7, 3)/f_combination(12, 4) \
    + f_combination(5, 1)*f_combination(3, 1)/f_combination(8, 2) * f_combination(5, 2)*f_combination(7, 2)/f_combination(12, 4) \
    + f_combination(5, 0)*f_combination(3, 2)/f_combination(8, 2) * \
    f_combination(5, 3)*f_combination(7, 1)/f_combination(12, 4)
print(
    f">>> Вероятность, что 3 мяча белые = {probability: .5f} -> {probability*100:0.2f}%")
