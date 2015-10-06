n = int(input("Write a non-negative integer number"))
num = n
mult = 1
while n < 0 or n == str:
    n = int(input("Please write a positive integer number"))
while num != 0:
    mult = mult*num
    num = num-1
print ("The fatorial of ",n," is ",mult)
