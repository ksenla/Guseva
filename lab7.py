def z1():
    from PIL import Image
    filename = "buildings.jpg"
    with Image.open(filename) as img:
        img.load()
        print(f"Размер изображения:{img.size}")
        print(f"Формат изображения:{img.format}")
        print(f"Цветовая модель изображения:{img.mode}")
#print(z1())
def z2():
    from PIL import Image
    filename = "buildings.jpg"
    with Image.open(filename) as img:
        low_res_img = img.resize(img.width // 3, img.height // 3)
        low_res_img.show()
print(z2())
