def division(x, y):
    try:
        answer = x/y
    except ZeroDivisionError:
        print("Can not divide by 0")
    except TypeError:
        print("Can not use strings")
    else:
        print("The answer is:", answer)
    finally:
        print("We are done")
        number1 = int(input("Enter number"))
        number2 = input("Enter number")
        division(number1, number2)