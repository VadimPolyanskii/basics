
year_birth_Pushkin = 1799           # Год рождения А.С.Пушкина
year_birth = input("Введите год рождения А.С.Пушкина цифрой: ")

while True:
    if int(year_birth) == year_birth_Pushkin:
        print(" Верно!")
        break
    else:
        year_birth = input("Введите год рождения А.С.Пушкина цифрой: ")
        if int(year_birth) == year_birth_Pushkin:
            print(" Верно!")
            break