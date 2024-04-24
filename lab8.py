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
    filename = "otkritka.jpg"
    with Image.open(filename) as img:
        img.load()
        img_crop = img.crop((200, 400, 600, 950))
        img_crop.show()
        img_crop.save("otkritka_crop.jpg")
        name = input("Введите имя:")
        draw = ImageDraw.Draw(img_crop)
        font = ImageFont.load_default()

        text = f"{name}, поздравляю!"
        text_color = (0, 0, 0)
        text_position = (50, img_crop.height - 50)
        draw.text(text_position, text, font=font, fill=text_color)
#проблема со шрифтом!!!
        img_crop.save("new_card.png")
z3()
