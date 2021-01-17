number = eval(input())
letter = True
for n in range(len(number)):
    if number[n] == 7 and letter == True:
        print(n)
        letter = False
if letter:
    print("Not found")
