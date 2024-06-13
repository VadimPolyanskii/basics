
year = 1799
day = 6

year_birth = int(input("Введи год рождения А.С.Пушкина: "))

while year_birth != year:
    if year_birth > year:
        print("Неверно! Попробуй ещё раз")
    else:
        print("Неверно! Попробуй ещё раз")

    year_birth = int(input("Введи год рождения А.С.Пушкина: "))

print("Верно!")

day_birth= int(input("Введи день рождения А.С.Пушкина: "))

while day_birth != day:
    if day_birth > day:
        print("Неверно! Попробуй еще раз")
    else:
        print("Неверно! Попробуй ещё раз")

    day_birth = int(input("Введи день рождения А.С.Пушкина: "))

print("Верно!")