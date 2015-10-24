n = int(input("Write a non-negative integer number"))
while n < 0:
    n = int(input("Please write a positive integer number"))
num = n
mult = 1
while num != 0:
    mult = mult*num
    num = num-1
print ("The fatorial of ",n," is ",mult)

