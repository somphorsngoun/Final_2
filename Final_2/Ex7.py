listOffruit = eval(input())
name = []
for dic in listOffruit:
    if dic["price"] < 20:
        name.append(dic["name"])
print(name) 