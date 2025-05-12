






# telefon = {
#     'Nazira':'0990686854',
#     'Nazi':'0778676763',
#     'nurtilek':'0550050721',
# }

# #### Байланышты кошуу
# def add_contact (name,telefon_number):
#     if not telefon.get(name):
#         telefon[name] = telefon_number
#     print(telefon)
# ###Байланышты издөө
# def search_contact(name):
#     number = telefon.get(name)
#     if number:
#         print(number)
#     else:
#         print('Байланыш номер жок!')

# ###Баардык-= маалыматтарды көрсөтүү
# def print_all_contacts():
#     text = ''
#     for name,telefon_number in telefon.items():
#         text +=f'{name} - {telefon_number} \n'
#     print(text)

# while True:
#     command = input(
#         'Кандай команда аткарат элеңиз? \n'
#         '1.Контакт кошуу \n'
#         '2.Контакт издөө\n'
#         '3.Баардык контакт көрүү \ n'
#         '4.Программаны токтотуу\n'
#     )

#     if command == '1':
#         name = input(' Аты-жөнүн киргизиңиз: ')
#     telefon_number = input('Телефон номерин киргизиңиз: ')
#     add_contact(name,telefon_number)
#     elif command == '2':   
#             name = input('Издей турган адамдын атын киргизиңиз: ')
#             search_contact(name)
        
#         elif command == '3':
#             print_all_contacts()
            

    