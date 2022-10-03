while(True):
    number = input("put your number: ")
    if (number == "quit"):
        break
    elif int(number) > 0:
        print("positive")
    elif int(number) < 0:
        print("Negative")