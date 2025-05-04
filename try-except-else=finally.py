def tryBlock():
    try:
        num=int(input("Enter a number:"))
        result=10/num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        print("Result:",result)
    finally:
        print("This block runs always")
tryBlock()