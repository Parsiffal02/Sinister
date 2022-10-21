import random
while True:                                        #Проверка на дурака
    try:
        count = ( int(input('Введите колличество элементов массива:' )))                                   
        break
    except ValueError:
         print('Вы должны ввести числа! Попробуйте снова!')
lst = [random.uniform(0, 1000) for i in range(count)]
print(lst)
print("Max element:",max(lst), ". Index of max element:", lst.index(max(lst))+1)
for i in range(lst.index(max(lst))+1, len(lst)):
    lst[i]=0
print(lst)