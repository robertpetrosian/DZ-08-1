yearofborn = int(input('В каком году родился А.С.Пушкин? '))
if 1000 < yearofborn < 10000:
    if yearofborn == 1799:
        bornday = input('В какой день? Ответьте цифрами в формате ДДММ: ')
        if bornday=='0606':
            print('Верно')
        else:
            print('Год указан верно, а день рождения неверно')
    else:
        print('Год рождения указали неверно')
else:
    print('Вы должны ввести 4-х значное число')


