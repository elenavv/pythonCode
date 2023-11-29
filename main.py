'''
while условие:
    действие_1
else:
    действие_которое_выплнится_если_цикл_весь_выполнился
'''
import random #подключение библиотеки
import time
import math

print(f"Время с начала эпохи {time.time()}")
startTime = time.time()
#time.strptime() - превращает строку в Объект времени в заданном формате
print(time.strptime('29 11 2023',"%d %m %Y"))




for i in range(5):
    randNum = random.random() #от 0 до 1
    print(f"Случайное число: {randNum}")

'''
random.sample(population, k) - 
список длиной k из последовательности population.
'''
randList = random.sample([10,'a',30,True],3)
print(f"Список случайный: {randList}")

randValue= random.choice('asdfghjk')
print(f"Значение случайное: {randValue}")

tempStr = ['1','2','3']
random.shuffle(tempStr)
print(f"Перемешанный список: {tempStr}")





num = 0
while num<5:
    print(f"Строка внутри цикла {num}")
    num+=1
else:
    print(f"Строка выполнится, если цикл пройдёт все шаги")

num = 0
while num<5:
    if num==3:
        print(f"Выполнится break , а else нет ")
        num += 1
        continue
    print(f"Строка внутри цикла {num}")
    num += 1
else:
    print(f"Строка выполнится, если цикл пройдёт все шаги")
