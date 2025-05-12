# class PaymentMethod:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self._balance = balance  
#     def deposit(self, amount):
#         self._balance += amount
#         print(f'Депосит алынды: Жаңы балас: {self._balance}')  

#     def process_payment(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#             print(f'Платеж иштелди: Жаңы баланс: {self._balance}')  
#         else:
#             print('Каражат жетишсиз')

#     def get_balance(self):
#         # return self._balance
#         print(f'Cиздин баланс: {self._balance}')


# payment_method = PaymentMethod(12321312231, 200)
# payment_method.deposit(300)
# payment_method.process_payment(400)
# print(payment_method.get_balance())

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def info (self):
#         print(f'Аты: {anumals1.name},Жашы:{anumals1.age}')
# anumals1 = Anumals('Бобик', 23)
# # anumals1.info()
 

# class Anumals:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def sound (self):
#         pass

# class Dog(Anumals):
#         def sound(self):
#             print(f'{self.name} {self.age}жашта ал мындай үн чыгарат: гав гав')

# class Cat(Anumals):
#      def sound(self):
#           print(f'{self.name} {self.age} жашта ал мындай үн чыгарат: мияу')
# dog1 = Dog('Бобик',20)
# cat1 = Cat('Сары',20)

# dog1.sound()
# cat1.sound()


# class Cars:
#      def __init__(self,name,model,color,year):
#           self.name = name
#           self.model = model
#           self.color = color
#           self.year = year 
#           pass
#      def speed(self):
#           pass
# class Car (Cars):
#     def speed(self):
#      print(f'{self.name } машинасынын модели {self.model} ал {self.color} түстө ал {self.year} жылы чыккан, 120 km ылдамдык менен жүрөт.')
# class ElectirCar(Cars):
#      def speed(self):
#          print(f'{self.name} машинасынын модели {self.model} ал {self.color} түстө ал {self.year} жылы чыккан, 120 km ылдамдык менен жүрөт.') 
# car1 = Car('camry','jany','red',2013)
# electir_car1 =ElectirCar ('bmw','eski','cary',2000)  

# car1.speed()
# electir_car1.speed()

# class Vehicle:
#     def __init__(self,brend,model,price,fuel):
#         self.brend = brend
#         self.model = model
#         self.__price = price
#         self.fuel = fuel
        
#     def get_price(self):
#         return f'{self.brend} {self.model} ,баасы:$ {self.__price}'
    
#     def start_engine(self):
#         print(f'{self.brend} {self.model} кыймылдаткыч күйгүзүлдү')

# class Car (Vehicle):
#     def __init__(self,brend,model,price,fuel,doors):
#         super().__init__(brend,model,price,fuel)
#         self.doors = doors
#     def start_engine(self):
#         print(f'{self.brend} {self.model} кыймылдаткыч күйгүзүлдү')

# class ElectricCar(Vehicle):
#     def __init__(self,brend,model,price,battery_size):
#         super().__init__(brend,model,price,'Electric')
#         self.battery_size = battery_size

#     def start_engine(self):
#         print(f'{self.brend} {self.model} аккумлятор{self.battery_size}kwh жүктөлүүдө')

# car1 = Car ('Toyota','Camry',300,'Gasoline',4,)
# electric_car1 = ElectricCar('Tesla','Model','99',80,)
# print(car1.get_price())
# car1.start_engine()

# print(electric_car1.get_price())
# electric_car1.start_engine()


# class Athlete:
#     def __init__(self,name,age,sport_type):
#         self.name = name
#         self.age = age
#         self.sport_type = sport_type
    
#     def info(self):
#         print(f'Аты:{self.name} жашы: {self.age} спорт түрү: {self.sport_type}')


# class FootballPlayter(Athlete):
#     def __init__(self,name,age,team):
#         super().__init__(name,age,'Фудбол')
#         self.team = team

        
#     def play(self):
#          print(f'{self.name} {self.team} командасы фудбол ойноп жатат! ')
    
# class Swimmer(Athlete):
#     def __init__(self,name,age,best_time):
#           super().__init__(name,age,'Сууда сүзү')
#           self.best_time = best_time
#     def swim(self):
#          print(f'{self.name} бассейнде сүзүп жатат! ушул убакыттагы мыкты натыйжасы {self.best_time}')


# football = FootballPlayter('Nazira',20,'Барселона' )
# swimmer = Swimmer('Dado',12,'00:45')

# football.info()
# football.play()

# swimmer.info()
# swimmer.swim()

# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
# class Student(Person):
#     def __init__(self,name,age,gender,grade):
#         super().__init__(name,age,gender,)
#         self.grade = grade

#     def study(self):
#         print(f'{self.name} {self.age} жашта жынысы аял ал тили сабагынан {self.grade} балл алды')
#     def info(self):
#         print(f'Аты: {self.name},жашы:{self.age},Жынысы: {self.gender}')
# class Teacher(Person):
#     def __init__(self,name,age,gender,subject):
#         super().__init__(name,age,gender,)
#         self.subject = subject

#     def teach(self):
#         print(f'{self.name} {self.age} жашта жынысы {self.gender} ал {self.subject} сабагынан мугалим')
    
#     def info(self):
#         print(f'Аты: {self.name},жашы:{self.age},Жынысы: {self.gender}')


# stydent1 = Student('Nazira',20,'аял',96)
# teacher = Teacher('Aida',45,'аял','физика')

# stydent1.study()
# stydent1.info()
# teacher.teach()
# teacher.info()


# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age =age
#         self.gender = gender
    
#     def info(self):
#         print(f'Аты: {self.name} Жашы: {self.age} Жынысы:{self.gender} ')
    
# class Student(Person):
#     def __init__(self, name, age, gender,grade):
#         super().__init__(name, age, gender,)
#         self.grade = grade

#     def study (self,subject):
#         print(f'{self.name} {subject} сабагынан {self.grade} балл алды.')

# class Teacher(Person):
#     def __init__(self, name, age, gender,subject):
#         super().__init__(name, age, gender)
#         self.subject = subject

#     def teach(self):
#         print(f'{self.name} {self.subject} сабагын өтүп жатат.')
# class School:
#     def __init__(self,name):
#         self.name = name
#         self.students = []
#         self.teachers = []
    
#     def add_teacher(self,teacher):
#         self.teachers.append(teacher)
#         print(f'{teacher.name} мугалим болуп ишке кирди')

#     def add_student(self,student):
#         self.students.append(student)
#         print(f'{student.name} мектепке кошулду')

#     def show_students(self):
#         print(f'\n{self.name} мектебиндеги окучуулар:')
#         for student in self.students:
#             student.info()

#     def show_teachers(self):
#         print(f'\n{self.name} мектебиндеги мугалимдер:')
#         for teacher in self.teachers:
#             teacher.info()

# school = School('Билим ордо')

# student1 = Student('Айжан',16,'аял',95)
# student2 = Student('Гулжан',14,'аял',89)
# teacher1 = Teacher('Эмил',40,'эркек','Математика')
# teacher2 = Teacher('Мирлан',40,'эркек','Кыргыз тили')

# school.add_student(student1)
# school.add_student(student2)

# school.add_teacher(teacher1)
# school.add_teacher(teacher2)

# school.show_students()
# school.show_teachers()

# student1.study('Кыргыз тили')

# teacher1.teach()


# class Book:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
# class Library:
#         def __init__(self):
#             self.books = []
        
#         def add_book(self,book):
#             self.books.append(book)
#             print(f'"{book.title}" китеби кошулду')

#         def show_books(self):
#             if not self.books:
#                 print('Китеп канада китептер жок')
#             else:
#                 print('\n Китепканадагы китептер')
#                 for book in self.books:
#                   print(f'"{book.title}" - {book.author} ({book.year})')

#         def find_by_author(self,author):
#             found_books = [book for book in self.books if book.author == author]
#             if found_books:
#                 print(f'\n Автор:{author} китептери')
#                 for book in found_books:
#                     print(f'{book.title} ({book.year})')
#             else:
#                 print(f'❌ "{author}" авторунун китептери табылган жок.')  
# library = Library()

# # Китептерди жаратуу
# book1 = Book("Жамгыр алдында", "Чыңгыз Айтматов", 1970)
# book2 = Book("Кызыл алма", "Чыңгыз Айтматов", 1980)
# book3 = Book("Обон", "Мухтар Ауэзов", 1965)

# # Китепканага кошуу
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Китепканадагы бардык китептерди көрсөтүү
# library.show_books()

# # Белгилүү бир автордун китептерин издөө
# library.find_by_author("Чыңгыз Айтматов")
# library.find_by_author("Түгөлбай Сыдыкбеков")      


# class Calculator:

#      def add(self,a,b):
#           return a+b
     
#      def subtract(self,a,b):
#           return a-b
#      def multiply(self,a,b):
#           return a*b
#      def divide(self,a,b):
#           if b==0:
#                return 'Нөлго бөлүүгө болбойт'
#           return a/b

#      calc = Calculator()

#      print(f'Кошуу: {calc.add(10,5)}')
#      print(f'Кемитүү: {calc.subtract(10,5)}')
#      print(f'Көбөйтүү: {calc.multiply(10,5)}')
#      print(f'Бөлүү: {calc.divide(10,5)}')


# age = 23
# print(age)

# pi_value = 3.4
# print(pi_value)
# name = 'Nazira'
# print(name)

# name = True
# print(name)
 
# x = 10
# if x > 5:
#      print('x 5тен чоң')
# else:
#      print('x 5ке барабар')


# name = input('Атыңызды киргизиңиз:')
# print(name)

# print(7+3)


# age = int(input('Жашыңызды киргизиңиз:'))
# if  age > 18:
#      print('Сиз чоң адамсыз:')
# elif 13 <= age <=18:
#      print('Сиз өспүрүмсүз:')
# else:
#      print('Cиз баласыз')
# for i in range (1,20):
#      print(i)
# i = 1
# while i<=5:
#      print(i)
# #      i+=1
# i = 5
# while i <= 20:
#      print(i)
#      i+=2

# def add_number(a,b):
#      return a+b
# result1 = add_number(5,6)
# print(result1)


# numbers = [1,2,3,4,5]
# for i in numbers:
#      print(i)
# numbers.extend([12,11])
# print('Жаңыртылган тизме', numbers)

# info = {
#      'Аты':'Назира',
#      'Жашы':'20',
#      'Шаары':'Баткен'
# }
# for key,value in info.items():
#      print(f'{key}:{value}')
# info['Хобби'] = 'Китеп окуу'
# print('Жаңыртылган маалымат',info)



# name = ('nazira','mirlan', 'aida')
# for i in name:
#      print(i)
# print('Биринчи элемент:',name[0])
# print('Акыркы элемент:',name[-1])

# name = input('Атыңызды киргизиңиз:')
# age  = int (input('Жашыңызды киргизиңиз:'))
# if age > 18:
#      print('Сиз чоң адамсыз')
# else:
#      print('Сиз жашсыз')
# matrix = [
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
# ]
# for i in matrix:
#      for item in i:
#           print(item,end='')
#      print()

# def sum_of_two_numbers(a,b):
#      return a+b

# num1 = int(input('Cанды киргизиңиз:'))
# num2 = int(input('Cанды киргизиңиз:'))
# result = sum_of_two_numbers(num1,num2)
# print('Сандардын суммасы:',result)

# number = [10,20,30,40,50]
# print(number)
# new_number = []
# for i in number:
#      new_number.append(i*2)
# print(new_number)

# people = {
#      'Nazira':20,
#      'Mirlan':21,
#      'Aida':22
# }
# for name,age in people.items():
#      print(f'Аты: {name}, Жашы: {age}')
# print('Назиранын жашы:',people['Nazira'])

# m = 1
# while m<=10:
#      print(m)
#      m+=1

# total_sum = 0
# while True:
#      user_input = input('Санды киргизиңиз же "exit" деп жазып токтот:')
#      if user_input.lower() == 'exit':
#           break
#      else:
#           try:
#                number = int(user_input)
#                total_sum += number
#           except ValueError:
#                 print('Туура сан киргизиңиз!')

# print(f'Сандардын жалпы суммасы: {total_sum}')

# class Person:
#      def __init__(self, name, age):
#           self.name = name
#           self.age = age

#      def greet(self):
#           print(f'Салам, менин атым {self.name}, мен {self.age} жаштамын.')
