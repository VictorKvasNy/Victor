a = int(input("Введите общее количество элементов списка"))
c = []
for i in range (a):
    i +=1
    b = int(input("введите значение элемента"))
    if b !=0:
        if b % 2 == 0:
            c.append(b)
print(c)
