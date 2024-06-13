

year_birth = input("Введите год рождения А.С.Пушкина цифрой: ")

while True:
    if int(year_birth) == 1799:
        print(" Верно!")
        break
    else:
        year = input("Введите год рождения А.С.Пушкина цифрой: ")
        if int(year) == 1799:
            print(" Верно!")
            break