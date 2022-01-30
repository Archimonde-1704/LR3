def f1(x):
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            return x
        except:
            pass
