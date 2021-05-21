def occupation(age):
    if 3 <= age < 7:
        return "Вы ходите в детский сад"
    elif 7 <= age < 18:
        return "Вы учитесь в школе"
    elif 18 <= age < 22:
        return "Вы учитесь в ВУЗе"
    elif 22 <= age < 65:
        return "Вы работаете"
    else:
        return "Ваш возраст позволяет Вам отдыхать"

while True:
    try:
        years = abs(int(input("Сколько Вам полных лет? ")))
        break
    except ValueError:
        print("Ошибка: ожидается целое число")

s = occupation(years)
print(s)