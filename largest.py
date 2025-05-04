def largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
a=23
b=45
c=12
max=largest(a,b,c)
print(f"The largest number is:{max}")