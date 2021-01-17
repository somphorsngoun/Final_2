array = eval(input())
arrayOfindex = []
for n in range(len(array)):
    if array[n] == 7:
        arrayOfindex.append(n)

print(arrayOfindex)