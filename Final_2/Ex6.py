listOfname = eval(input())
sum = 0
X = True
for n in range(len(listOfname)):
    if 6 >= len(listOfname[n])>= 4:
        sum += 1
    if sum == len(listOfname):
        print("GOOD")
        X = False
if X:
    print("BAD")