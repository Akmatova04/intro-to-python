class BankAccount:
    def __init__(self, account, full_name, account_type):
        self.account = account
        self.full_name = full_name
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Кошулган сумма: {amount}. Жаңы баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Ката! Эсепте жетиштүү каражат жок.")
        else:
            self.balance -= amount
            print(f"Алып салынган сумма: {amount}. Жаңы баланс: {self.balance}")

    def show_info(self):
        print(f"Эсеп номери: {self.account}")
        print(f"Ээсинин аты-жөнү: {self.full_name}")
        print(f"Эсептин түрү: {self.account_type}")
        print(f"Учурдагы баланс: {self.balance}")

account1 = BankAccount(1002231123, "Акматова", "Сактоочу")
account2 = BankAccount(2003342234, "Алина ", "Учёттук")
account3 = BankAccount(3004453345, "Бакыт ", "Ишкердик")


account1.deposit(1000)
account1.withdraw(500)
account1.show_info()

account2.deposit(2000)
account2.withdraw(1500)
account2.show_info()

account3.deposit(5000)
account3.withdraw(6000)  
account3.show_info()