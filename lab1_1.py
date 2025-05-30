# Запрашиваем три числа у пользователя и преобразуем ввод в тип float
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

max_num = max(a, b, c)
min_num = min(a, b, c)

all_equal = (a == b == c)

print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)
if all_equal:
    print("Все числа равны.")
else:
    print("Не все числа равны.")
