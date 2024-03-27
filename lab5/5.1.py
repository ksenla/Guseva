chislo = int(input("введите число:"))
set = [25, 673, 22, 123, 66]
if chislo in set:
    print ("Поздравляю, Вы угадали число!")
else:
    print ("Нет такого числа!")
print("Исходный список чисел:", set)
print("Ваше число:", chislo)