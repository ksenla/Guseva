def z1():
    import json
    json_data = '''
    {
      "products": [
        {
          "name": "Шоколад",
          "price": 50,
          "available": true,
          "weight": 100
        },
        {
          "name": "Кофе",
          "price": 100,
          "available": false,
          "weight": 250
        },
        {
          "name": "Чай",
          "price": 70,
          "available": true,
          "weight": 50
        }
      ]
    }
    '''
    data = json.loads(json_data)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
z1()

def z2():
    import json

    product_name = input("Введите название продукта: ")
    product_price = float(input("Введите цену продукта: "))
    product_weight = input("Введите вес продукта: ")
    product_available = input("Продукт в наличии?: ").lower() == 'да'

    product_data = {
        "name": product_name,
        "price": product_price,
        "weight": product_weight,
        "available": product_available
    }

    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"products": []}

    data["products"].append(product_data)

    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print("Информация:")
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
z2()

def z3():
    ru_en_dict = {}

    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        for line in file:
            english, russian = line.strip().split(' - ')
            for word in [word.strip() for word in russian.split(',')]:
                ru_en_dict[word] = ru_en_dict.get(word, []) + [english]

    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for russian_word in sorted(ru_en_dict):
            file.write(f"{russian_word} - {', '.join(ru_en_dict[russian_word])}\n")

z3()
