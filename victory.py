lst_writers=['Пушкиин','Лермонтов','Гоголь','Есенин','Толстой']
lst_years = [1799, 1814,1809,1895,1828]
while True:
    score=0
    for i in lst_writers:
        otv=int(input('Когда родился '+i+'? '))

        if otv == lst_years[lst_writers.index(i)] :
            score += 1

    print('Количество ответов '+ str(len(lst_writers)))
    print('Количество верных ответов '+ str(score))
    print('IQ=' +  str(round(100*score/len(lst_writers)))+'%')

    if input('Введите 1 , если хотите начать заново, нет - людой символ ') != '1' :
        break


