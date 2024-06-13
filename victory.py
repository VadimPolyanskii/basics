
# Года рождений известных людей
Pushkin = 1799
Gogol = 1809
Lermontov = 1814
Dostoevsky = 1821
Tolstoy = 1828

# Счётччик верных и неверных ответов
correct_answer = 0
incorrect_answer = 0
correct_answer_2 = 0
incorrect_answer_2 = 0


print("Игра 'Викторина'")
print("----------------------")
while True:
    Pushkin_answer = int(input("Назовите год рождения А.С.Пушкина: "))                  # 1799
    if Pushkin_answer == Pushkin:
        correct_answer += 1
    else:
        incorrect_answer += 1

    Gogol_answer = int(input("Назовите год рождения Н.В.Гоголя: "))                     # 1809
    if Gogol_answer == Gogol:
        correct_answer += 1
    else:
        incorrect_answer += 1

    Lermontov_answer = int(input("Назовите год рождения М.Ю.Лермонтова: "))             # 1814
    if Lermontov_answer == Lermontov:
        correct_answer += 1
    else:
        incorrect_answer += 1

    Dostoevsky_answer = int(input("Назовите год рождения Ф.М.Достоевского: "))          # 1821
    if Dostoevsky_answer == Dostoevsky:
        correct_answer += 1
    else:
        incorrect_answer += 1

    Tolstoy_answer = int(input("Назовите год рождения Л.Н.Толстого: "))                 # 1828
    if Tolstoy_answer == Tolstoy:
        correct_answer += 1
    else:
        incorrect_answer += 1


    print()
    print("Правильных ответов:", correct_answer)
    print("Неправильных ответов:", incorrect_answer)
    print()
    print("Процент правильных ответов:", correct_answer * 100/5)
    print("Процент неправильных ответов:", incorrect_answer * 100/5)

    print()
    continue_game = input("Желаете сыграть ещё раз? Ответьте 'Да' или 'Нет': ")

    print()
    if continue_game == "Да" or "да":
        Pushkin_answer = int(input("Назовите год рождения А.С.Пушкина: "))  # 1799
        if Pushkin_answer == Pushkin:
            correct_answer_2 += 1
        else:
            incorrect_answer_2 += 1

        Gogol_answer = int(input("Назовите год рождения Н.В.Гоголя: "))  # 1809
        if Gogol_answer == Gogol:
            correct_answer_2 += 1
        else:
            incorrect_answer_2 += 1

        Lermontov_answer = int(input("Назовите год рождения М.Ю.Лермонтова: "))  # 1814
        if Lermontov_answer == Lermontov:
            correct_answer_2 += 1
        else:
            incorrect_answer_2 += 1

        Dostoevsky_answer = int(input("Назовите год рождения Ф.М.Достоевского: "))  # 1821
        if Dostoevsky_answer == Dostoevsky:
            correct_answer_2 += 1
        else:
            incorrect_answer_2 += 1

        Tolstoy_answer = int(input("Назовите год рождения Л.Н.Толстого: "))  # 1828
        if Tolstoy_answer == Tolstoy:
            correct_answer_2 += 1
        else:
            incorrect_answer_2 += 1

        print()
        print("Правильных ответов:", correct_answer_2)
        print("Неправильных ответов:", incorrect_answer_2)
        print()
        print("Процент правильных ответов:", correct_answer_2 * 100 / 5)
        print("Процент неправильных ответов:", incorrect_answer_2 * 100 / 5)
        print("Игра окончена")
        break

    else:
        print("Игра окончена")
        break
