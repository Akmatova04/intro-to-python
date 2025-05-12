# text = input('Текст жазыңыз: ')
# new_text = text.replace(' ', '_')
# print(new_text)

# text = 'Мен питонду жакшы көрөм'
# print(text.replace('питонду','python'))

# number = input('Санды киргизиңиз: ')
# number_1 = number.replace('-',' ')
# print(number_1)

# text = input('Сап киргизиңиз: ')
# print(text.replace('.',' '))
 
# text = input('Сап киргизиңиз: ')
# print(text.replace('жаман','*****'))

# name = input('Атыңызды киргизиңиз: ')
# print(name.startswith('А'))

# web = input('Веб-дарек киргизиңиз: ')
# if web.startswith('https'):
#     print('Бул коопсуз сайт')
# else:
#     print('Бул сайт коопту')

# proramma = input('Программанын атын жазыңыз:\n ')
# if proramma.startswith('RUN_'):
#     print('Команда ишке кирди')
# else:
#     print('Команда ката')

# doc = input ('Докмент атын киргизиңиз:\n')
# print(doc.endswith('.txt'))

# emaile = input('emil ды киргизиңиз:\n')
# if emaile.endswith('.com'):
#     print('Бул эл аралык email')
# else:
#     print('Бул эл аралык email эмес')

# phone = input('Телефон номер киргизиңиз: \n')
# if phone.endswith('99'):
#     print('Сиздин номер 99 менен аяктайт')
# else:
#     print('Бул номер 99 менен аяктабайт')


command = 'RUN_programm: \n'
if command.startswith('RUN_'):
    print('Команда ишке кирди')
else:
    print('Команда ката')