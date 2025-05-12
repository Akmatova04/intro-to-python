


# phone = input('Телефон номерди киргизиңиз:')
# if phone.startswith('+996')and len(phone) == 13 and phone[4:].isdigit():
#     number = phone[4:]
#     formatted = f'+996({number[:3]}){number[3:6]} - {number[6:9]} - {number[9:]}'
#     print('Телефон номер туура:',formatted)
# else:
#     print('+996 менен башталып 9 сан болушу керек')

# card_number = input('16 орундуу картаңызды киргизиңиз:')
# masked_pard = card_number[:12].replace(card_number[:10],'*' * 10)
# visble_part = card_number[12:]
# masked_pard = f'{masked_pard[:4]}-{masked_pard[4:8]}-{masked_pard[8:12]}-{visble_part}'
# print(masked_pard)

 
# card_number =input("16 орундуу сан киргизиңиз: ")
# masked_pard= card_number[:12].replace(card_number[:12],'*' * 12)
# visble_part = card_number[12:]
# masked_pard = f'{masked_pard[:4]}-{masked_pard[4:8]}-{masked_pard[8:12]}-{visble_part}'
# print(masked_pard)



# card_number = input('16 орундуу санды киргизиңиз: ')
# masked_part = card_number[:12].replace(card_number[:12],'*' * 12)
# visible_part= card_number[12:]
# if card_number.startswith('4444') and len(card_number)==16 and card_number.isdigit():
#     masked_pard = f'0044{masked_part[:4]}-{masked_part[4:8]}-{masked_part[8:12]}-{visible_part}'
#     print('Карта номери туура:',masked_pard)
# else:
#     print('0044 менен башталып 16 сан болушу шарт')

# card_number = input('!6 орундуу сан киргизиңиз: ')
# masked_part = card_number[:12].replace(card_number[:12],'*' *12)
# visible_part = card_number[12:]
# if card_number.startswith("4444")and len(card_number)==16 and card_number.isdigit:
#     masked_part = f'0044{masked_part[:4]}-{masked_part[4:8]}-{masked_part[8:12]}-{visible_part}'
#     print('Карта номери туура:',masked_part)
# else:
#     print('4444 менен башталып 16 орундуу сан болушу шарт')

### string сап сөз кошуп жазат
# name = 'Nazira'
# city = 'Batken'
# print(f'Hello,{name}!you live in {city}.')

# product = input('Товардын атын киргизиңиз: ')
# price = input('Товардын баасын киргизиңиз: ')
# print(f'Сиздин {product},{price} сом болду')


####split '' кошуп чыгарат же жок кылат
# string = input('Текст киргизиңиз: ')
# word_list = string.split()
# print(word_list)

# numbers_string = input('Сандарды киргизиңиз: ')
# numbers = [int(i) for i in numbers_string.split(',')]
# total = sum(numbers)
# print(f'Сандардын суммасы {total}')


## count эсептөө
# string = input('Текстти киригиңиз: ')
# symbol = input('Симболду киргизиңиз: ')
# print(string.count(symbol))

# sting = 'banana'
# symbol = 'a'
# print(sting.count(symbol))


## алмаштыруу
# string = 'nazira'
# print(string.replace('nazira','mirlan'))

string = 'I love java'
old_word = 'java'
new_word = 'python'
print(string.replace(old_word,new_word))
 

####  башталабы жокпу текшерет
# string = 'Hello word!'
# print(string.startswith('Hello'))

# string = 'Apple!'
# print(string.startswith('A'))


####бүтөбү жокпу текшерет
# string = 'docment.pdf'
# print(string.endswith('pdf'))

