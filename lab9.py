def z12():
    import os
    from PIL import Image, ImageFilter

    images_folder = "images/"
    filters_folder = "filter/"

    if not os.path.exists(filters_folder):
        os.makedirs(filters_folder)

    for img_file in os.listdir(images_folder):
        if img_file.endswith(".jpg") or img_file.endswith(".png"): #задание 2: проверка расширения файла
            img_path = os.path.join(images_folder, img_file)
            image = Image.open(img_path)
            imgfilt = image.filter(ImageFilter.CONTOUR)
            filtered_img_path = os.path.join(filters_folder, img_file)
            imgfilt.save(filtered_img_path)
z12()
def z3():
    total = 0
    print("Нужно купить:")
    with open('products.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            product, quantity, price = line.strip().split(',')
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total} руб.")
z3()
