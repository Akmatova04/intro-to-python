class Person:
    def __init__(self, name, age, gender, birthday_date):
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday_date = birthday_date

    def speak(self, sentence):
        print(f"{self.name} айтат: {sentence}")

    def eat(self, food):
        print(f"{self.name} жейт {food}")

    def drink(self, beverage):
        print(f"{self.name} ичет {beverage}")

    def display_info(self):
        print(f"Аты-жөнү: {self.name}")
        print(f"Жашы: {self.age}")
        print(f"Жынысы: {self.gender}")
        print(f"Туулган күнү: {self.birthday_date}")


person1 = Person("Айжан", 22, "F", "03.05.2002")
person1.display_info()
person1.speak("Салам!")
person1.eat("плов")
person1.drink("чай")


class Student:
    def __init__(self, name, age, group, course):
        self.name = name
        self.age = age
        self.group = group
        self.course = course

    def study(self, subject):
        print(f"{self.name} {subject} предметин окуйт")

    def sleep(self, hours):
        print(f"{self.name} {hours} саат уктайт")

    def display_info(self):
        print(f"Аты-жөнү: {self.name}")
        print(f"Жашы: {self.age}")
        print(f"Группа: {self.group}")
        print(f"Курс: {self.course}")


student1 = Student("Бекболот", 20, "kk9-3-20", 2)
student1.display_info()
student1.study("математика")
student1.sleep(6)


class Animal:
    def __init__(self, species, name, age, habitat):
        self.species = species
        self.name = name
        self.age = age
        self.habitat = habitat

    def speak(self, sound):
        print(f"{self.name} үн чыгарат: {sound}")

    def eat(self, food):
        print(f"{self.name} жейт {food}")

    def sleep(self, hours):
        print(f"{self.name} {hours} саат уктайт")

    def display_info(self):
        print(f"Түрү: {self.species}")
        print(f"Аты: {self.name}")
        print(f"Жашы: {self.age}")
        print(f"Жашаган жери: {self.habitat}")


animal1 = Animal("Ит", "Бобик", 3, "Үй")
animal1.display_info()
animal1.speak("Гав-гав!")
animal1.eat("сөөк")
animal1.sleep(8)



class Person:
    def __init__(self,name,age,gender,birthday_date):
        self.name = name
        self.age = age
        self.gender = gender
        self.birthdae_date = birthday_date
    
    def speak(self,senctece):
        print(f'{self.name} айтат {senctece}')

    def eat(self,food):
        print(f'{self.name} {food} жейт')

    def drink(self,cola):
        print(f'{self.name} {cola} ичет')

    def display_info(self):
        print(f'Аты жөнү: {self.name}\nЖашы:{self.age}\nЖынысы:{self.gender}\nТуулган күнү:{self.birthdae_date}')

person = Person('Nazira',20,'f','18.04.2004')
person.display_info()
person.speak('Hello')
person.eat('манты')
person.drink('fanta')



class Student:
    def __init__(self,name,age,group,course):
        self.name = name
        self.age = age
        self.group = group
        self.course = course
    def study(self, subject): 
        print(f'{self.name} {subject} пердметин окуйт.')
        
    

    



    