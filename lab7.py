def z1():
    from PIL import Image
    filename = "buildings.jpg"
    with Image.open(filename) as img:
        img.load()
        print(f"Размер изображения:{img.size}")
        print(f"Формат изображения:{img.format}")
        print(f"Цветовая модель изображения:{img.mode}")
z1()
def z2():
    from PIL import Image
    filename = "buildings.jpg"
    with Image.open(filename) as img:
        low_res_img = img.reduce(3)
        img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
        img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
        low_res_img.save("first.jpg")
        img2.save("second.jpg")
        img3.save("third.jpg")
z2()
def z3():
    from PIL import Image, ImageFilter
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for img in images:
        image = Image.open(img)
        imgfilt = image.filter(ImageFilter.CONTOUR)
        imgfilt.save('filters/'+str(img))
z3()
