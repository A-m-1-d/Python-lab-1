# - Выводит все четные числа из списка.
# - Выводит числа, которые делятся на 3.
# - Вычисляет и выводит среднее арифметическое всех чисел в списке.

import random

# Генерируем список из 20 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(20)]
print("Сгенерированный список:", numbers)

# Находим все четные числа
even_numbers = [num for num in numbers if num % 2 == 0]
print("Четные числа:", even_numbers)

# Находим все числа, делящиеся на 3
divisible_by_3 = [num for num in numbers if num % 3 == 0]
print("Числа, делящиеся на 3:", divisible_by_3)

# Вычисляем среднее арифметическое чисел списка
average = sum(numbers) / len(numbers)
print("Среднее арифметическое чисел в списке:", average)
