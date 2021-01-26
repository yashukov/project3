#Список городов
cities = ['Москва', 'Париж', 'Лондон']

#Информация о людях
users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

#Сопоставление человека и города
tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

#______________________________________________________________________
#Ввод запроса пользователем
city = input('Введите город: ')

#Сопостовление введённых данных с базой
if city.title() == cities[0]:
    print(f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город лондон")
elif city.title() == cities[1]:
    print(f"Турист {users[2]['name']} возраст {users[2]['age']}. Посетил город лондон")
elif city.title() == cities[2]:
    print(f"Турист {users[0]['name']} возраст {users[0]['age']}. Посетил город лондон")
else:
    print('Город не найден')

#end
