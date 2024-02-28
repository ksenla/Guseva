result = ""
word=""
while word != "stop":
    word = input("Введите слово или stop:")
    result += word + " "

print("Результат соединения слов:")
print(result)