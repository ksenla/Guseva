chislo = int(input("Введите число:"))
set = [22, 25, 66, 7, 5]
if chislo in set:
    print ("Поздравляю, Вы угадали число!")
else:
    print ("Нет такого числа!")
print ("Исходный список:", set)
print ("Ваше число:", chislo)