def errors():
    try:
        a=5
        b=10
        result=a/b
        list=[1,2,3]
        print(list[5])
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except IndexError:
        print("Error: List index out of range")
errors()