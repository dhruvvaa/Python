import math
def isPrime(n):
    if(n<0):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
num=int(input("Enter a number:"))
if isPrime(num):
    print(f"The number is prime")
else:
    print("The number is not prime")