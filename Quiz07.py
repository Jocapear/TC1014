#first excersise
import math
x1 = int(input("Give me x1"))
y1 = int(input("Give me y1"))
x2 = int(input("Give me x2"))
y2 = int(input("Give me y2"))
def distance(x1,y1,x2,y2):
    a = (x2-x1)*(x2-x1)
    b = (y2-y1)*(y2-y1)
    d = a + b
    c = math.sqrt(d)
    return c
print("The distance between (",x1,",",y1,") and (",x2,",",y2,") is",distance(x1,y1,x2,y2))

#second excersise
position = int(input("Give me the position"))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = fibonacci(n-1)+fibonacci(n-2)
        return value
fibonacci(position)
print ("The fibonacci of",position,"is",fibonacci(position))
