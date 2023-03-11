from os import system
from math import factorial
system("cls")

'''
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. 
Из каждого ящика вытаскивают случайным образом по два мяча. 
Какова вероятность того, что все мячи белые? 
Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?

'''


def f_combination(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


# Вероятность того, что все мячи белые
probability = f_combination(7, 2)*f_combination(3, 0)/f_combination(10, 2) * \
    f_combination(9, 2)*f_combination(2, 0)/f_combination(11, 2)
print(
    f">>> Вероятность, что все мячи белые = {probability:.5f} -> {probability*100:0.2f}%")

# Вероятность того, что ровно два мяча белые
probability = f_combination(7, 2)*f_combination(3, 0)/f_combination(10, 2) * f_combination(9, 0)*f_combination(2, 2)/f_combination(11, 2) \
    + f_combination(7, 1)*f_combination(3, 1)/f_combination(10, 2) * f_combination(9, 1)*f_combination(2, 1)/f_combination(11, 2) \
    + f_combination(7, 0)*f_combination(3, 2)/f_combination(10, 2) * \
    f_combination(9, 2)*f_combination(2, 0)/f_combination(11, 2)
print(
    f">>> Вероятность того, что ровно два мяча белые = {probability:.5f} -> {probability*100:0.2f}%")

# Вероятность того, что хотя бы один мяч белый
probability = 1 - f_combination(7, 0)*f_combination(3, 2)/f_combination(
    10, 2) * f_combination(9, 0)*f_combination(2, 2)/f_combination(11, 2)
print(
    f">>> Вероятность того, что хотя бы один мяч белый {probability:.5f} -> {probability*100:0.2f}%")
