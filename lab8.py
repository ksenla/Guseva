def z1():
    from PIL import Image
    filename = "otkritka.jpg"
    with Image.open(filename) as img:
        img.load()
        img_crop = img.crop((200, 400, 600, 950))
        img_crop.show()
        img_crop.save("otkritka_crop.jpg")
z1()

def z2():
    from PIL import Image

    holidayotkritka = {
        "день рождения": "birthday_card.jpg",
        "новый год": "new_year_card.jpg",
    }

    holiday = input("Введите название праздника: ")

    if holiday in holidayotkritka:
        card_file = holidayotkritka[holiday]
        print(f"Открытка к празднику '{holiday}':")

        card_image = Image.open(card_file)
        card_image.show()
    else:
        print("Открытка к данному празднику не найдена.")
z2()

def z3():
    from PIL import Image, ImageDraw, ImageFont
    name = input("Введите имя:")
    image = Image.open("otkritka.jpg")
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((50,18), name, font=font, fill='black')
    drawer.text((150, 18), ", поздравляю!", font=font, fill='black')
    image.save("new_card.png")
    image.show()
z3()
