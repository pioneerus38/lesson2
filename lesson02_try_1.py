def hello_user():
    while True:
        try:
            response = input("Как дела? ")
        except KeyboardInterrupt:
            print("Пока!")
            break

hello_user()