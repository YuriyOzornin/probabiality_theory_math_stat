import math
import numpy as np
from os import system
system("cls")
'''
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, 
среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
'''
# Среднее арифметическое (mean) можно вычислить, суммируя все значения массива и деля их на количество элементов в массиве.


salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65,
            17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

mean = sum(salaries) / len(salaries)
print(f'Cреднее арифметическое = {mean: .2f}')


# Среднее квадратичное отклонение(standard deviation) можно вычислить, используя формулу: σ = √ ( ( ∑ ( xi - μ )² ) / N )

stddev = math.sqrt(sum((x - mean) ** 2 for x in salaries) / len(salaries))
print(f'\nCреднее квадратичное отклонение = {stddev: .4f}')

# Смещенная оценка дисперсии можно вычислить, используя формулу: σ² = (∑ (xi - μ)²) / N
var = sum((x - mean) ** 2 for x in salaries) / len(salaries)
print('\nСмещенная оценка дисперсии = ', var)

# Несмещенная оценка дисперсии можно вычислить, используя формулу: σ² = ( ∑ ( xi - μ )² ) / (N-1)
unbiased_var = sum((x - mean) ** 2 for x in salaries) / (len(salaries) - 1)
print(f'\nНесмещенная оценка дисперсии = {unbiased_var: .4f}')


# =======================================================================================================

print("\n" + "=" * 50)
print('\nЕсли же нужно сделать это более оптимально и быстро можно использовать библиотеку numpy и ее функции mean, var, std и.т.д\n')

mean = np.mean(salaries)
print("Mean: ", mean)

stddev = np.std(salaries)
print("Std deviation: ", stddev)

var = np.var(salaries)
print("Variance: ", var)

unbiased_var = np.var(salaries, ddof=1)
print("Unbiased variance: ", unbiased_var)
