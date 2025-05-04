class NegativeNumberError(Exception):
    pass
def checkPositive(num):
    if(num<0):
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("Correct Number")
try:
    checkPositive(-4)
except NegativeNumberError as e:
    print("Caught custom exception:",e)