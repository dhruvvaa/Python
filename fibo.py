def Fibonacci(n):
    if(n<+0):
        return 0
    elif(n==1):
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)
n=6
print(f"{n}th fibonacci term if {Fibonacci(n)}") 