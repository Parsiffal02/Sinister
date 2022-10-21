import random
while True:                                        #Проверка на дурака
    try:
        count = ( int(input('Введите колличество элементов первого массива:' )))
        count1 = ( int(input('Введите колличество элементов второго массива:' )))                                    
        break
    except ValueError:
         print('Вы должны ввести числа! Попробуйте снова!')

lst = [random.uniform(0, 1000) for i in range(count)]
lst1 = [random.uniform(0, 1000) for i in range(count1)]
print(lst)
print(lst1)
print(set(lst) & set (lst1))

