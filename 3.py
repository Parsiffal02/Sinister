import random
while True:                                        #Проверка на дурака
    try:
        count = ( int(input('Введите колличество элементов массива:' ))) 
        delta = int(input('Введите дельта:' ))                               
        break
    except ValueError:
         print('Вы должны ввести числа! Попробуйте снова!')
lst = [random.randint(0, 1000) for i in range(count)]
print('Массив:', lst)
result = lst.count(min(lst) + delta)
print('Колличество эллементов:',result)
