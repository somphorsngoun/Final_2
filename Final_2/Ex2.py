array = eval(input('>'))
indexOfseven = 0
for n in range(len(array)):
    if array[n] == 7:
        indexOfseven = n
        boolean = False
if boolean:
    print("Not found")
else:
    print(indexOfseven)