# class BankAccount:
#     def __init__(self,owner,balance,account_type):
#         self.owner = owner
#         self.__balance = balance
#         self.account_type = account_type

#     def get_balance(self):
#         return self.__balance
    
#     def deposit (self,amount):
#         self.__balance += amount
#         return self.__balance
         
# bank_account = BankAccount('Nazira',200,'saving')
# print(bank_account.owner)
# print(bank_account.get_balance())
# print(bank_account.account_type)
# print(bank_account.deposit(1000))


# Жаныбар классы — бардык жаныбарларга бирдей мүнөздөмөлөрдү жана ыкмаларды камсыз кылат

class Animal:
    # init методун түзүү: ал классты түзгөндө ат жана түр маалыматтарын алат
    def __init__(self, name, species):
        self.name = name  # Жаныбардын аты
        self.species = species  # Жаныбардын түрү 

    # Бул базалык версиясы, үн чыгарбайт, бирок аны башка класстарда өзгөртүүгө болот
    def make_sound(self):
        print('Ничего')
  

# Dog классы Animal классын мурас кылат жана конкреттүү жаныбар — итти көрсөтөт
class Dog(Animal):

    # Dog классында дагы жаныбар атын жана түрүн алыш керек, бирок кошумча порода дагы берилет
    def __init__(self, name, species, breed):
        super().__init__(name, species)  # Animal классынын конструкторун чакыруу (ата-энеси)
        self.breed = breed  # Иттин породу

    # Иттин үнү "гав" деп өзгөртүлөт
    def make_sound(self):
        print('гав')  # Иттин үнү "гав"


# Cat классы Animal классын мурас кылып, кошкону көрсөтөт
class Cat(Animal):
    # Бул учурда, Cat классы үчүн конструктор түзүлгөн эмес, ошондуктан Animal классынын конструктору колдонулат

    # Мышык классында үн чыгаруу ыкмасы "мяу" деп өзгөртүлөт
    def make_sound(self):
        print('мяу')  # Мышык "мяу"

# Dog классы аркылуу ит объектиси түзүлөт. Бул жерде атын, түрүн жана породасын берүүдөбүз.
dog = Dog('рекс', 'собачьи', 'лабрадор')

# Cat классы аркылуу кошка объектиси түзүлөт. Бул жерде атын жана түрүн гана көрсөтөбүз.
cat = Cat('корниш рекс', 'кошачьи')

# Иттин атын, түрүн жана породасын чыгарып көрсөтүү
print(dog.name, dog.species, dog.breed)

# Иттин үнү "гав" деп чыгарылаары көрсөтүлөт.
dog.make_sound()

# Мышыктын атын жана түрүн чыгарып көрсөтүү
print(cat.name, cat.species)

# Мышык үнү "мяу" деп мияктоо
cat.make_sound()


class OnlineCourse:
    def __init__(self,course_name,students=[]):
        self.__course_name = course_name
        self.__students = students


    


