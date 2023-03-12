from os import system
from math import factorial
system("cls")
'''
Условие:
На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
'''
# Формула подсчета количества сочетаний по k элементов из множества n
#    C(nk) = n!/(k!*(n - k)!)


def f_combination(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


'''
    P(A)=m/n - общее количество исходов определяется кол-ом сочетаний из 10 возможных 3,
    а количество благоприятных исходов открытия замка 1
'''
m = 1  # m = 1
n = f_combination(10, 3)  # n = из "10" "3"
P = m / n
print(
    f'\n<<< Вероятность того, что замок откроется с первой попытки = {round(P*100,3)}% >>>')
