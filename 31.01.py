#Бириктирүү
print('Nazira' + '' + 'Akmatova')
#Көбөйтүү
print('Nazira' * 3)
#Индекс боюнча символду алуу
name = 'Nazira'
print([0])
print([-1])
#Кыркып алуу
print(name[1:3])
print(name[1:2])
print(name[::-1])

# name = 'Nazira Akmatova'
# print(name.title()) # Ар бир сөздүн башын чоң кылат
# print(name.capitalize()) # Биринчи тамганы чоң кылат
# print(name.upper()) # Баары баш тамгага айланат
# print(name.lower()) # Баары кичине тамгага айланат

# name = '   Akmatova  '
# print(name.strip()) # Баш аягындагы боштуктарды жок кылат
# print(name.rstrip()) # Боштук оң же сол жактан өчүрүлөт
# print(name.lstrip()) # Боштук оң же сол жактан өчүрүлөт



# city_name = 'Баткен' 
# print(city_name[0]) # 1- симбол
# print(city_name[1]) # 2- симбол
# print(city_name[-1]) # акыркы симбол
# print(city_name[1]) # 1-индекс
# print(city_name[2]) # 2- индекс
# print(city_name[-1]) # акыркы индекс
# print(city_name[:3]) # кыркып алуу акыркы 3 симбол
# print(city_name[:6:2]) # алгачкы 6 симбол 2 кадам менен
# print(city_name[-4:]) # акыркы 4 симбол
# print(city_name[::-1]) #баардык симбол тескери тартипте

# book_name = 'Маркумдар үнү'
# print(book_name.title())
# print(book_name.capitalize())
# print(book_name.upper())
# print(book_name.lower())

# school_name = ' Школа лицей №13 '
# print(school_name.upper())
# print(school_name.lower())
# print(school_name.capitalize())
# print(school_name.title())
# print(school_name.lstrip()) #башындагы боштук
# print(school_name.rstrip()) # акырындагы
# print(school_name.strip()) # эки жагындагы


# gadget_name = 'Ipfone 15  Pro Max'
# print(gadget_name.replace('15','16')) #replase саптагы санды алмаштыруу
# gardet_name = gadget_name.replace('15','16') #өзгөрмө жаңыланат
# print(gadget_name)

# index_ =gadget_name.find('15') #find бир симболдун индексин табуу
# #Сапты экиге бөлүү
# print(gadget_name[index_:])
# print(gadget_name[:index_])
# #Белгилүү бир симболду саноо
# print(gadget_name.count('1'))

the_best_teacher = 'Dair Sheshenaliev 22 years'
                  # 123456789101112131415161718
print(the_best_teacher.replace('22','19'))
print(the_best_teacher.replace('Dair','Doka'))
print(the_best_teacher.find('ey'))
print(the_best_teacher.find('ev'))
print(the_best_teacher.find('nali'))



count = the_best_teacher.count('a')
count = the_best_teacher.count('e')
count = the_best_teacher.count('2')
count = the_best_teacher.count('ir')
count = the_best_teacher.count('ev')