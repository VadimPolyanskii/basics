year = input("Назовите год рождения А.С.Пушкина: ")

if int(year) == 1799:
    birthday = input("Теперь назовите день рождения А.С.Пушкина: ")
    if int(birthday) == 6:
        print(("Верно!"))
    else:
        print("Неверный день рождения!")
else:
    print("Неверный год рождения!")