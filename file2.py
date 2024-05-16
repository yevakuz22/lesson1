while True:
    try:
        user_input = input("Введіть число: ")
        number = int(user_input)
        print("Введене число:", number)
        break
    except ValueError:
        print("Помилка! Введені дані не можуть бути конвертовані в число. Спробуйте ще раз.")