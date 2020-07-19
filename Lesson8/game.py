
def guess_reverse():
    print("Загадайте число от 1 до 100")

    max_number = 100
    min_number = 1
    answer = None

    while answer != 1:
        number = min_number + (max_number - min_number) // 2
        print(f"Вы загадали число {number}?")
        print(" 1. Победа")
        print(" 2. Загаданное число меньше")
        print(" 3. Загаданное число больше")
        answer = int(input("Ввведите номер ответа: "))
        if answer == 2:
            max_number = number
        else:
            min_number = number

    print("Число угадано")
