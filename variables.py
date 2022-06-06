sotrudniki = {'001':{
                'fio' : 'Petrov Petr',
                'salary' : 30000,
                'age' : 22,
                'married' : True,
                'childs' : ['Ivan', 'Maria']
                },
              '002':
                {
                'fio': 'Petrov Petr',
                'salary': 30000,
                'age': 22,
                'married': True,
                'childs': ['Ivan', 'Maria']
                }
            }

print( 'Тип sotrudniki', type(sotrudniki))
print('Тип кодов БД ', type(sotrudniki.keys()))
print('Тип значения сотрудника с кодом 001', type(sotrudniki['001']))
print('Тип ФИО сотрудника 001',type(sotrudniki['001']['fio']))
print('Тип возраста сотрудника 001',type(sotrudniki['001']['age']))
print('Тип признака семейности сотрудника 001',type(sotrudniki['001']['married']))
