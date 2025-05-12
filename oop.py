
# # class Car:
# #     make= 'Toyota'
# #     model = 'camry'
# #     year = 2020

# # car1 = Car()
# # car2 = Car()
# # print(car1.make)

# # class Car:
# #     def __init__(self,make,model,year,color,driver):
# #         self.make = make
# #         self.model = model
# #         self.year = year
# #         self.color = color
# #         self.driver = driver

# #     def drive(self):
# #         print('Машина поехали')

# #     def stop(self):
# #         print('Машина остановилась')

# #     def on(self):
# #         print('Машина завадена')

# #     def off(self):
# #         print('Машина выключена')


# # car3 = Car('Toyota','camry',2020,'кызыл','Nazira')
# # print(car3.make,car3.model,car3.year,car3.color,car3.driver)
# # car3.driver = 'Atambek'
# # print(car3.make,car3.model,car3.year,car3.color,car3.driver)

# # car3.on()
# # car3.off()
# # car3.drive()
# # car3.stop()


# # class Book:
# #     def __init__(self,title,autor,year,color):
# #         self.title = title
# #         self.autor = autor
# #         self.year = year
# #         self.color1 = color
# # book1 = Book('Бетме бет','Чыңгыз Айтматов',2013,'red')
# # print(book1.title,book1.autor,book1.year,book1.color1)
# # book1.autor = 'Алыкул Осмонов'
# # print(book1.title,book1.autor,book1.year,book1.color1)
# # book1.color1 = 'Жашыл'
# # print(book1.title,book1.autor,book1.year,book1.color1)
    

# # class Person:
# #     def __init__(self,name,age,sex,birthday_date):
# #         self.name = name
# #         self.age = age
# #         self.sex = sex
# #         self.birthday_date = birthday_date
# # person = Person('Nazira',20,'j',('18.04.2004'))
# # print(person.name,person.age,person.sex,person.birthday_date)


# # class Person:
# #     def __init__(self,name,age,sex,birthday_date):
# #         self.name = name
# #         self.age = age
# #         self.sex = sex
# #         self.birthday_date = birthday_date

# #     def speak(self,sentence):
# #         print(sentence)    

# #     def eat(self,food):
# #         print(f'Кушает {food}')

# #     def drink (self,drink_name):
# #         print

    
# # person = Person('Nazira',20,'j',('18.04.2004'))
# # print(f'Aты:{person.name}\nЖашы:{person.age}\nЖынысы:{person.sex}\nТуулган күнү:{person.birthday_date}')
# # print(f'Аты: {person.name}')
# # print(f'Жашы: {person.age}')
# # print(f'Жынысы: {person.sex}')
# # print(f'Туулган күнү: {person.birthday_date}')
# # person.speak('text sdsfsad')
# # person.eat('banana')

# # class Student:
# #     def __init__(self,name,age,group,course):
# #         self.name = name
# #         self.age = age
# #         self.group = group
# #         self.course = course

# #     def study(self,subject):
# #         print(f'Учит {subject}')
# #     def sleep(self,hourse):
# #         print(f'Спит{hourse}')
# # student = Student('Nazira',20,'kk9 3 20','')

# class BankAccount:
#     def __init__(self,account_number,account_holders_name,balance,account_type):
#         self.account_number = account_number
#         self.account_holders_name = account_holders_name
#         self.balance = balance
#         self.account_type = account_type

#     def withdraw(self,amount):
#         if self.balance < amount:
#             print(f'Каражат жетишсиз: {amount - self.balance}')
#         else:
#             self.balance -= amount
#             print(f'Ийгиликтүү алынды: {amount}\nСиздин калдык: {self.balance}')


# bank_account = BankAccount(1002231123,'Nazira',0,'Агымдагы')
# bank_account.withdraw(500)
# bank_account.withdraw(1000)
# print(f'Эсеп номери: {bank_account.account_number}\nЭэсинин аты: {bank_account.account_holders_name}\nБаланс: {bank_account.balance}\nЭсептин түрү: {bank_account.account_type}')

year = {
    'jan':31,
    'feb':28,
    'mar':30,
    'may':30,
    'jul':33,
    'sep':22,
    'dec':33,
    'apr':22,
}
for key,value in year .items():
    print(f'{key}: {value}')