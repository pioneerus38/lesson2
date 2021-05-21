def hello_user():
    while True:
        answer = input("Как дела? ")
        if answer == "Хорошо":
            print("Рад за тебя. Пока!")
            break

hello_user()