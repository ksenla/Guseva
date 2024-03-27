def z1():
    chislo = int(input("Введите число:"))
    set = [22, 25, 66, 7, 5]
    if chislo in set:
        print ("Поздравляю, Вы угадали число!")
        else:
        print ("Нет такого числа!")
    print ("Исходный список:", set)
    print ("Ваше число:", chislo)
print(z1())

def z2():
    list = [1, 22, 23, 22, 25, 76, 25]
    for item in list:
        if list.count(item) > 1 :
            print ("Повторяющиеся элементы:",item)
            break
        else:
            print ("Повторяющихся элементов нет.")
#print(z2())