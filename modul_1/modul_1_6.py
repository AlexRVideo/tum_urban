my_dict = {'Васли': 1970, 'Акпатыр': 2000, 'Эйвика': 1997, 'Ольош': 1986, 'Осяндра': 2015}
print(my_dict)
print(my_dict['Осяндра'])
print(my_dict.get('Салика'))
my_dict.update({'Миклай': 1999,
                'Айвика': 2007})
print(my_dict)
print(my_dict.get('Акпатыр'))
del my_dict['Акпатыр']
print(my_dict.get('Акпатыр'))
print(my_dict)

my_set = {1, 'Пире', 23.4, 56.3, 'Рывыж', 1, 'Пире', 23.4,}
print(my_set)
print(my_set.add(8))
print(my_set.add('Кайык'))
print(my_set)
print(my_set.remove(56.3))
print(my_set)