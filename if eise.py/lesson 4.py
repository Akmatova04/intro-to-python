# is_raining = True

# if is_raining == True:
#     print('возьми зонт')
# else:
#     print('не возьми зонт')
  

# is_raining = False

# if is_raining == True:
#     print('возьми зонт')
#     print('Погода холодная')
# else:
#     print('не возьми зонт')
#     print('Погода теплая')
# print('Программа завершена')


# == спарвнение салыштыруу
# > больше чоң
# < меньше кичине
# >= больше или равно чоң же барабар
# <= меньше или равно чоң же кичине
# != не равно барабар эмес


# number_1 = 30
# number_2 = 20
# if number_1 == number_2:
#     print('число равны')
# elif number_1 > number_2:    
#     print('Первое число больше второго')
# elif number_1 < number_2:    
#     print('Первое число меньше второго')  
# else:
#     print('число не равны')


# number = input('Введите число')
# number = int(number)

# print(type(number))
# print(number)

# if number % 2 == 0:
#     print('число четное')
# else:
#     print('Число нечетное')

age = int(input('канча жаштасызq'))
has_passport = input("Есть ли у вас паспорт (да\нет):")

if age >= 20 and age < 45 and has_passport == 'да':
    print('Вы можете пройти')
elif age >= 20 and has_passport == 'нет':
    print('Возмите паспорт')
else:
    print("Вы не подхите")