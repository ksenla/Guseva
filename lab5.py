def z1():
    chislo = int(input("Введите число:"))
    set = [22, 25, 66, 7, 5]
    if chislo in set:
        print ("Поздравляю, Вы угадали число!")
    else:
        print ("Нет такого числа!")
    print ("Исходный список:", set)
    print ("Ваше число:", chislo)
#print(z1())

def z2():
    list = [1, 22, 23, 22, 25, 76, 25]
    for item in list:
        if list.count(item) > 1 :
            print ("Повторяющиеся элементы:",item)
            break
    else:
        print ("Повторяющихся элементов нет.")
#print(z2())

def z3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekend = week[-weekendnumber:]
    work = week[:-weekendnumber]
    print("Ваши выходные дни:", ",".join(weekend))
    print("Ваши рабочие дни:", ",".join(work))
#print(z3())

def z4():
    md25 = ["Гусева", "Овчинников", "Зайцев", "Постников", "Токарева", "Поспелова", "Свириденко", "Петров", "Зотова", "Идрисова"]
    md20 = ["Белкина", "Близгарёв", "Богданчук", "Казарян", "Кучев", "Кучинова", "Левченко", "Малкиель", "Решетников", "Семёнов"]
    sportteam = tuple(md25[:5]+md20[:5])
    print("МД-25:", md20)
    print("МД-20:", md20)
    print("Спортивная команда:", sportteam)
    print ("Длина кортежа:", len(sportteam))

    sortedteam = tuple(sorted(sportteam))
    print("Сортированный кортеж:", sortedteam)

    surname = "Иванов"
    if surname in sportteam:
        print("Фамилия Иванов входит в спортивную команду.")
        print(f"Количество Ивановых:{sportteam.count(surname)}")
    else:
        print("Фамилия Иванов не входит в спортивную команду.")
#print (z4())


