'''''Негизги set методдору жана операциялары:
set – сэт (көптүктүн өзү, типтин аталышы)
add() – эд (элемент кошуу)
update() – апде́йт (бир нече элементти кошуу/жаңыртуу)
remove() – риму́в (элементти алып салуу, жок болсо ката берет)
discard() – диска́рд (элементти алып салуу, жок болсо ката бербейт)
pop() – поп (каалаган бир элементти алып салуу жана кайтаруу)
clear() – кли́эр (баардык элементтерди тазалоо)
union() (же | оператору) – ю́нион (көптүктөрдүн биригүүсү)
intersection() (же & оператору) – интерсе́кшн (көптүктөрдүн кесилиши)
intersection_update() – интерсе́кшн апде́йт (кесилишүүнү учурдагы set'ке сактоо)
difference() (же - оператору) – ди́фференс (көптүктөрдүн айырмасы)
difference_update() – ди́фференс апде́йт (айырманы учурдагы set'ке сактоо)
symmetric_difference() (же ^ оператору) – симме́трик ди́фференс (симметриялык айырма)
symmetric_difference_update() – симме́трик ди́фференс апде́йт (симметриялык айырманы учурдагы set'ке сактоо)
copy() – ко́пи (көптүктүн көчүрмөсүн түзүү)
isdisjoint() – из-дисджо́йнт (эки көптүктүн орток элементтери жок экенин текшерүү)
issubset() (же <= оператору) – из-са́бсэт (бир көптүк экинчисинин ички көптүгү экенин текшерүү)
issuperset() (же >= оператору) – из-су́персэт (бир көптүк экинчисин камтыганын текшерүү)
'''
#1. class
names = {'nazira','mmirlan','uulkan','abal','aigul'}
print(type(names))

# 2. add() – бир элемент кошуу
names = {'nazira','mmirlan','uulkan','abal','aigul'}
names.add('nako')
print(names)



# # 3. update() – бир нече элемент кошуу
names = {'nazira','mmirlan','uulkan','abal','aigul'}
names.update(['alina', 'kamila'])
print(names)


# # 4. remove() – элементти алып салуу (жок болсо ката берет
names = {'nazira','mmirlan','uulkan','abal','aigul'}
names.remove('abal')
print(names)

# 5. discard() – элементти алып салуу (жок болсо ката бербейт
names = {'nazira','mmirlan','uulkan','abal','aigul'}
names.discard('bakty')
print(names)

# 6. pop() – туш келди бир элементти алып салуу
names = {'nazira','mmirlan','uulkan','abal','aigul'}
removed_name = names.pop()
print(names)



# # 7. clear() – баарын тазалоо
names = {'nazira','mmirlan','uulkan','abal','aigul'}
names.clear()
print(names)


# # 8. union() – кошуу (жаңы set берет)
a = {'apple', 'banana'}
b = {'banana', 'cherry'}
result = a.union(b)
print(result)


# # 9. intersection() – кесилиш
a = {'apple', 'banana'}
b = {'banana', 'cherry'}
result = a.intersection(b)
print(result)

# # 10. intersection_update() – азыркы set’ке сактоо
a = {'apple', 'banana'}
b = {'banana', 'cherry'}
a.intersection_update(b)
print(a)


# # 11. difference() – айырма
a = {'apple', 'banana'}
b = {'banana', 'cherry'}
result = a.difference(b)
print(result)


# # 12. difference_update() – айырманы сактоо
a = {'apple', 'banana'}
b = {'banana', 'cherry'}
a.difference_update(b)
print(a)


# 15. copy() – көчүрмөсүн алуу
names = {'nazira','mmirlan','uulkan'}
names_copy = names.copy()
print(names_copy)


# 16. isdisjoint() – орток элемент барбы?
a = {'apple', 'banana'}
b = {'cherry', 'melon'}
print(a.isdisjoint(b))  # True



# 17. issubset() – ички көптүкпү?
a = {'a', 'b'}
b = {'a', 'b', 'c'}
print(a.issubset(b))  # True



# 18. issuperset() – толук камтыйбы?
print(b.issuperset(a))  # True


