def file(cars):
    count = 0
    city = 0
    highway = 0
    price = 0
    for line in cars:
        if (count % 2 == 0):
            a = float (line[52:54])
            city += a
            b = float (line[55:57])
            highway += b
            c = float (line[42:46])
            price += c
        count += 1
        d = count/2

        cityaverage = city/d
        highwayaverage = highway/d
        priceaverage = price/d
        return (cityaverage, highwayaverage, priceaverage)
cars = open("93cars.dat.txt")
(cityaverage, highwayaverage, priceaverage) = file(cars)
print (cityaverage)
print (highwayaverage)
print (priceaverage)
