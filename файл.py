

# # 1. Файлды ачуу
# file = open("example.txt", "w")  # Жазуу режими

# # 2. Маалымат жазуу
# file.write("Бул Python'до файл менен иштөө мисалы.") 

# # 3. Файлды жабуу
# file.close()

# students = open('students.txt','w')
# students.write('nazira')
# students.close()



# students = open('students.txt','a')
# students.write('\n nazi')
# students.close()


# students = open('students.txt','r')
# text = students.read()
# print = text
# students.close()

# with open('students.txt','w') as f:
#     f.write('nazira \n aida \n miki ')

# with open('students.txt','r') as f:
#     text = f.read()
#     print(text)

# with open('students.txt','a') as f:
#     f.write('\n nazi \n ai \n mi ')

# with open('students.txt','r') as f:
#     text = f.read()
#     print(text)

# with open('students.txt','a') as f:
#     f.write('\n nazi \n ai \n mi ')

# with open('students.txt','r') as f:
#     text = f.readlines()
#     print(text)

# with open('students.txt','w') as f:
#     f.writelines(['1\n','2\n','3\n' '4\n '])

# with open('students.txt','r') as f:
#     names = f.readlines()
#     for name in names:
#         print(name)

with open('cars.txt','w') as f:
   f.write( 'mers, 2020\n',)
   f.write('BMW,2017\n',)


with open('cars.txt','a') as f:
   f.write( 'AUDI,2002\n',)
   f.write('TOYOTA,2015\n',)

with open('cars.txt','r') as f:
    names = f.readlines()
    for name in names:
        print(name)

def add_car():
    car_name = input('Машинанын атын киргизиңиз:')
    car_year = input('Машинанын жылын киргизиңиз:')

    with open('cars.txt','a') as f:
        f.write(f'{car_name},{car_year}\n')
    print(f'{car_name},{car_year}\n')

add_car()

print('\n Баардык маалыматтар')
with open('cars.txt','r') as f:
    data = f.read()
    print(data)

