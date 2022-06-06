yearofborn = int(input('Когда родился А.С.Пушкин? '))
if 1000 < yearofborn < 10000:
    if yearofborn == 1799:
        print('Верно')
    else:
        print('Не верно')
else:
    print('Вы должны ввести 4-х значное число')