import random
correct = 0
wrong = 0
while wrong < 3:
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    res = n1 + n2
    answer = input(f"{n1}+{n2}=")

    if int(answer) == res:
        print("Правильно!")
        correct += 1
    else:
        print("Неверный ответ.")
        wrong += 1
print("Игра окончена. Правильных ответов:", correct)

