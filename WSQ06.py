import random
counter = int(1)
number = random.randint(1,100)
print("Try to find the number i´m thinking. It´s between 1 and 100")
innum = int(input("Give me your number"))
while innum != number:
    counter = counter + 1
    if(innum > number):
        print(innum," is HIGHER than my number")
        innum = int(input("Give me another number"))
    else:
        print(innum," is LOWER than my number")
        innum = int(input("Give me another number"))          
print("CORRECT, ",number," was the right number")
print("You tried ",counter," times")

