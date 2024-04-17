def z1():
    country_capital = {
        'Россия': 'Москва',
        'Швеция': 'Стокгольм',
        'Япония': 'Токио',
        'Португалия': 'Лиссабон'
    }
#a)   Выведите на экран все пары ключ-значение.
    for country, capital in country_capital.items():
        print (f'{country} - {capital}')

#b)  Выведите на экран столицу для определенной страны.
        print(f'Столица России: {country_capital["Россия"]}')

#c) Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.''
    sortedcountry = dict(sorted(country_capital.items()))
    for country, capital in sortedcountry.items():
        print(f'{country} - {capital}')
#print(z1())
def z2():
   points = {
        'А': 1, 'В': 1, 'Е' : 1, 'И' : 1, 'Н' : 1, 'О' : 1, 'Р' : 1, 'С' : 1, 'Т' : 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь':3, 'Я':3,
        'Й' :4, 'Ы' :4,
        'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5,
        'Ш':8, 'Э':8, 'Ю':8,
        'Ф':10, 'Щ':10, 'Ъ':10
    }
   word = input("Введите слово:").upper()
   score = sum(points.get(letter,0) for letter in word)
   print (f'Стоимость слова: {score} очков')
#print(z2())

def z3():
    students_lang = {
        'Иван': ['английский', 'немецкий'],
        'Марк': ['английский', 'французский', 'китайский'],
        'Яна': ['английский', 'китайский'],
        'Виктория': ['английский', 'французский']
    }
    languages = set()
    chinese = []
    for student, language in sudents_lang.items():
        languages.update(language)
#ищем студентов, которые знают китайский язык.
        if 'китайский' in language:
            chinese.append(student)
#отсортированный список этих языков.
    sortedlang = sorted(languages)
    print(f'Языки, которые знают студенты: {sortedlang}')
#список студентов, которые знают китайский язык.
    print(f'Студенты, знающие китайский:{", ". join (chinese)}')
#print(z3())

