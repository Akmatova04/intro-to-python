# class PaymentMethod:
#     def procaess_payment(self):
#         pass
# class MBank(PaymentMethod):
#     def procaess_payment(self,amount):
#         print(f' {amount} сом суммасында төлөм MBank аркылуу жүргүзүлдү' )


# class OptimaBank(PaymentMethod):
#     def procaess_payment(self,amount):
#         print(f' {amount} сом суммасында төлөм MBank аркылуу жүргүзүлдү ')
   
#     def __str__(self):
#         return 'Optima'
# mbank = MBank()
# optima = OptimaBank()
# mbank.procaess_payment(100)
# optima.procaess_payment(100)
# print(optima)



class PaymentMethod:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self,amount): 
        self.__balance += amount
        print(f'Депосит алынды: Жаңы балас: {self.__balance}')
        
    def process_payment(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Платеж иштелди: Жаңы баланс {self.__balance}')

        else:
            print('Каражат жетишсиз')

    
    def get_balance(self):
        return self.__balance
        
payment_method = PaymentMethod(2, 2)
payment_method.deposit(3)
payment_method.process_payment(4)
print(payment_method.get_balance())