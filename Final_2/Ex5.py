X = int(input(">"))
letter = True
number = 1
while X != 72 and letter:
    number += 1
    if number == 4:
        letter = False
    X = int(input(">"))
if letter:
    print("Win")
else:
    print("Lost")