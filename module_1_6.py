my_dict = {'Игорь' : 30}
print(my_dict)
print(my_dict['Игорь'])
print(my_dict.get('Миша'))
my_dict.update({'Илья': 20, 'Вася': 27})
print(my_dict)
del my_dict['Игорь']
print(my_dict)
my_set = {1,4,6,6,2,1,5,3,3,'Hello'}
print(my_set)
my_set.update({8, 'Cook'})
print(my_set)
my_set.discard(3)
print(my_set)
