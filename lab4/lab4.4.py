bilet = input("Введите номер билета:")
def lucky(bilet):
    if len(bilet) % 2 != 0 or len(bilet)== 0:
        print ("введите корректный номер билета")
        return False
    half = len(bilet) // 2
    return sum(map(int, bilet[:half])) == sum(map(int, bilet[half:]))
if lucky(bilet):
    print("билет счастливый")
else:
    print ("билет не счастливый")