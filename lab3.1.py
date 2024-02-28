N = int(input("Введите количество слов: "))
result = ""

for i in range(N):
    word = input(f"Введите слово {i+1}: ")
    result += word + " "

print("Результат соединения слов:")
print(result.strip())
