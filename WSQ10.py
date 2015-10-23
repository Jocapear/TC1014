def main(y):
    print("Give me",y,"numbers")
    r = int(input())
    numbers =[]
    while len(numbers) < y:
        numbers.append(r)
        if len(numbers) < y:
            r = int(input("Give me another number"))
    print (numbers)
    #sum of the 10 numbers
    def function(x):
        name = x
        var = 0
        for i in numbers:
            var += i
        result = var/len(numbers)
        if name == 1:
            return var
        else:
            return result
    #Paul´s blog idea -->https://pololarinette.wordpress.com/2015/10/15/wsq10-lists/
    #Standar deviation
    import statistics
    statistics.stdev(numbers)

    print("The sum of the",y,"numbers is",function(1))
    print("The average of the",y,"numbers is",function(2))
    print("The stardart deviation is",statistics.stdev(numbers))
main(10)#change the number if you want
