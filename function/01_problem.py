def gratest(a,b,c):
    if(a>b and a >c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 1
b = 20
c = 3
print(gratest(a,b,c))