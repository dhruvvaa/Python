a=0
b=1
c=0
n=int(input('Enter a number:'))
if(n<0):
    print("Please enter positive number")
else:
    print("Fibonacci Series:")
    for i in range (1,n+1):
        print(c)
        a=b
        b=c
        c=a+b
    