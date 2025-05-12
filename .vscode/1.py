# text = 'Школа гимназия №70'
# print(text.startswith('Школа')) #Бир сөз башталып башталбаганын текшерет.
# print(text.endswith('№70')) #аягын текшерет
# print(text.endswith('гимназия'))


# int_text = '123456'
# print(text.isdigit()) #толугу менен сандан турабы
# print(text.isalpha()) # толугу менен тамгалардан турабы
# print(int_text.isalpha())

# if int_text.isdigit():
#     int(int_text)
# products = 'apple, banana, orange'
# print(products.split(', '))  # Бөлүп алуу ", " белгиси менен

# name = 'Doka'
# age = 22
# print(f'Меня зовут – {name}, мне {age} года')   # f-строка менен өзгөрмөлөрдү кошуу
# print(f'5 + 5 = {5 + 5}')                       # f-строка ичинде эсеп жүргүзүү
# print(f'5 * 3 = {5 * 4}')                       # f-стsasрока ичинде эсеп ргүзүү

num1 = input('Санды киргизиңиз:')
num2 = input('Санды киргизиңиз:')

if num1.isdigit() and num2.isdigit():
    print(f'{num1} + {num2} = {int(num1)} + {int(num2)}')
    print(f'{num1} * {num2} = {int(num1)} * {int(num2)}')
    print(f'{num1} - {num2} = {int(num1)} - {int(num2)}')
