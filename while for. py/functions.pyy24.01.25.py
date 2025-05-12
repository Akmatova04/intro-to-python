# def sum_(a,b):
#     print(a+b)
# sum_(30,40)


# def divide(a,b):
#     print(a/b)
# divide(55,5)


# def multiply(a,b):
#     print(a*b)
# multiply(10,40)


# def sumscract(a,b):
#     print(a-b)
# sumscract(40,40)

# def get_milk (name):
#     products ={
#         'Веселый молочник':120,
#     }
#     return products[name]
# milk_price = get_milk('Веселый молочник')
# print(milk_price)

# def greet_user(name):
#     print(f'Hello,{name}!')
# greet_user('Nazira')

# def greet_user(name,age):
#     print(f'hello,{name}!Сиздин жашыңыз {age}.')
# greet_user(name='Nazira',age=20)

# def greet_user(name='Nazira'):
#     print(f'hello,{name}!')
# greet_user()
# greet_user('Nazira')

# def calculate(a,b):
#     return a+b,a-b,a*b
# sum_,diff,prod = calculate(5,3)
# print(f'sum:{sum_}, Difference:{diff},Product:{prod}')

def temperature_report(city,temperature=25):
    print(f'temperature in {city} is {temperature} degrees.')

temperature_report('Batkeh')
temperature_report('batken',10)