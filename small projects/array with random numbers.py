from random import randrange

array = []

for row in range(3):
    new_row = []
    for item in range(3):
        new_row.append(randrange(1000))
    array.append(new_row)

for row in array:
    for item in row:
        print(str(item) + " ", end=" ")
    print("")

for i in range(3):
    print("+----+----+----+")
    print(("|" + str(array[i][0]) + "\t" + "|"+ str(array[i][1])+ "\t"+ "|" + str(array[i][2])+ "\t|").expandtabs(5))
print("+----+----+----+")