

# # name = input('Машинаңыз бузулдубу? (нет/ да):')
# # if name  == 'нет':
# #     print('машина канаттандырарлык абалда')
# # elif name == 'да':
# #     print('машина күзөтүүго муктаж')
# # else:
# #     print('машинанын абалын так киргизиңиз')



# # age = int(input('Жашыңызды киргизиңиз'))
# # document = input('Документтиңиз барбы? (Да/Нет):')

# # if age >= 18 and document == 'да':  
# #     print('Сизге виза берилет')
# # elif age >= 18 and document == 'нет':
# #     print('Виза берилбейт, жаш курагыныз жетишпейт')
# # else:
# #     print('Документтер жок')



# # hair_color = input('Чачыңыздын түсүн киргизиңиз. (сары,кызыл,кара) :')

# # if hair_color == 'сары':
# #         print('сары чач')
# # elif hair_color == 'кызыл':
# #         print('кызыл чач')
# # elif hair_color == 'кара':
# #         print('кара чач')
# # else:
# #         print('Мындай чач жок')

# # word = input('Сөздү жазыңыз (күчтүү/жаман): ')

# # if word == 'күчтүү':
# #     print('позитивдүү')
# # elif word == 'жаман':
# #     print('негатив')
# # else:
# #     print('мындай сөз жок')

# # ecology = input('Сиз экология салым кошуп жатасызбы? (ообa/жок): ')
 
# # if ecology == 'ооба':
# #     print('азаматсыз сиз экологияны колдоп жатасыз')
# # elif ecology == 'жок':
# #     print('сураныч экологияга коңүл буруңуз')
# # else:
# #     print('маалыматты туура киргизиңиз')

# # name = input('Атыңызды киргизиңиз')
# # age = int(input('Жашыңзды киргизиңиз'))
 
# # if age >= 18:
# #     print('Салам улуу адам')
# # elif 12 <= age < 18:
# #     print('Салам өспүрүм')
# # else:
# #     print('Салам бала')


# # star_time = int(input('Жумушка барган убакытты жазыңыз'))
# # end_time = int(input('Жумуштан кайткан убакытты жазыңыз'))

# # work_hous = end_time - star_time

# # if  work_hous < 8:
# #     print('Жумушта аз убакыт өткөрдүнүз')
# # elif work_hous > 8:
# #     print('Жумушта көп убакыт өткөрдүңүз')
# # else:
# #     print('Жумушка барган жоксуз')


# # card = int(input('Акчаны тандаңыз'))

# # if card >5000:
# #     print('Акча алып жатасыз')
# # elif card <5000:
# #     print('Баланс жетишсиз')
# # else:
# #     print('Баланс жок')



# # salary = int(input('Канча айлык аласыз'))

# # if salary <10000:
# #     print('Айлык жакшы эмес')
# # elif salary >10000:
# #     print('Айлык жакшы')
# # else:
# #     print('Айлык жок')



# # card_number = input('Картаңыздын номерин киргизиңиз')

# # if card_number == '5':
# #     print('Платновая карта')
# # elif card_number == '4':
# #     print('Голд карта')
# # elif card_number == '3': 
# #     print('Бронзовая карта')
# # else:
# #     print('Сизге карта жок')

# # croup1_score = int(input('Сиздин командаңыз канча упай алды?'))
# # croup2_score = int(input('Каршы команда канча упай алды?'))
# # if croup1_score > croup2_score:
# #     print('Жеңиш')
# # elif  croup1_score == croup2_score:
# #     print('Тең эсеп')
# # else:
# #     print('Жеңилиш')









# # oil_level = float(input('Машинаңыздын майын киргизиңиз (%):'))
# # if oil_level >= 75 :
# #     print('Майдын деңгели жакшы')
# # elif 50 <= oil_level < 75:
# #     print('Май деңгели орто')
# # else:
# #     print('Май төмөн')


# oil_level = float(input('Майдын деңгелин киргизиңиз (%):'))
# if oil_level >= 75:
#     print('Май деңгели жакшы')
# elif 50<= oil_level >75:
#     print('Май денгели орточо')
# else:
#     print('Май деңгели төмөн')



# number = int(input("Сан киргизиңиз: "))

# print("Жөнөкөй сандар:")
# for i in range(2, number + 1):  # 2ден баштап берилген санга чейин текшерүү
#     is_prime = True
#     for j in range(2, i):  # 2ден i-1ге чейин бөлүнүп же бөлүнбөгөнүн текшерүү
#         if i % j == 0:  # Эгер бөлүнсө, жөнөкөй сан эмес
#             is_prime = False
#             break
#     if is_prime:  # Эгер жөнөкөй болсо, басып чыгарат
#         print(i)






















# list = ['Яблоко','банан','виноград']
# print(list)


# list = ['Яблоко','банан','виноград']
# list.append('апельсин')
# print(list)

# list = ['Яблоко','банан','виноград']
# list.remove('банан')
# print(list)

# list = ['Яблоко','банан','виноград']
# list.append('апелсинь')
# list.remove('Яблоко')
# print(list)


# number = int(input('Санды киргизиңиз'))
# if number >10:
#     print('число больше 10')
# else:
#     print('Число 10 или меньше')

# age = int(input('Жагыңызды киргизиңиз'))
# if age >= 18:
#     print('Совершеннолетний')
# elif age  >13 :
#     print('Подросток')
# # else:
# #     print('Ребенок')

# num_1 = int(input('санды киргизиниз'))
# num_2 = int(input('санды киргизиниз'))
# if num_1 + num_2 >100:
#     print(('Сумма больше'))
# elif num_1 - num_2 == 0:
#     print('Число не равны')
# else:
#     print('ни одно из условий не выполено')


# str типиндеги өзгөрмө
# str_variable = "Салам, дүйнө!"
# print("Маани:", str_variable, ", Типи:", type(str_variable))

# # int типиндеги өзгөрмө
# int_variable = 10
# print("Маани:", int_variable, ", Типи:", type(int_variable))

# # float типиндеги өзгөрмө
# float_variable = 3.14
# print("Маани:", float_variable, ", Типи:", type(float_variable))

# # bool типиндеги өзгөрмө
# bool_variable = True
# print( type(bool_variable))





# my_list = ['яблоко','милк','груша' ,1,3,5, True ]
# print('Баштапкы тизме')
# my_list.append('23')
# my_list.pop(3)
# print(my_list)


user_input = input("Санды киргизиңиз: ")

if '.' in user_input:
    print("Бул ондук сан (float).")
else:
    print("Бул бүтүн сан (int).")