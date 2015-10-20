def main():
    list1 = []
    list2 = []
    a = 0
    b = 0
    while a != "end":
        r = input("Give me your numbers, write ""end"" if you want to end.")
        if r != "end":
            r = int(r)
            list1.append(r)
        a = r
    while b != "end":
        r = input("Give me the numbers of list 2, write ""end"" if you want to end.")
        if r != "end":
            r = int(r)
            list2.append(r)
        b = r
    def dot_product(x,y):
        counter = 0
        add = 0
        print ("This is your list 1:",list1)
        print ("This is your list 2:",list2)
        if len(list1) != len(list2):
            return float('NaN')
        while counter != len(list1):
            mult = list1[counter]*list2[counter]
            add += mult
            counter += 1
        return add
    print (dot_product(list1,list2))
main()
