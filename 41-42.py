print("Цикл1")
for i in range(0, 3, 2):
    for j in range(0, 2, 1):
        print(f"Вывод {i - 4} {j}")

print("Цикл2")
for i in range(0, 3, 1):#i=0
    for j in range(0, 9, 1):#j=0 1
        i -= 1#i = 0-1 = -1 i=-1-1=-2
        print(f"Вывод {i - 2} {j}" ) #-3 0 -4  1
