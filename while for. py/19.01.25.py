# numbers = [1,2,3]
# for number in range(4,11):
#     print('Номер из range:', number)
#     numbers.append(number)
# print(numbers)



# numbers = [1,2,3]
# words = []
# for word in ['test','orange']:
#     words.append(word)
# print(words)

# for number in range(4,11):
#     print('Номер из range:', number)
#     numbers.append(number)
# print(numbers)



# for i in range(1 , 11):
#     print(i, 'в квадрате =',i ** 2)
#     print(f'{i} в квадрате = {i**2}')


# name = 'Nazira'
# age = 20
# print(f'Салам, {name}! Сенин жашың {age}.')


# a = 4
# b = 7
# print(f' {a} + {b} = { a + b }')

# for i in range(1, 11):
#     print(f'{i} * {i} = {i}')


n = int(input('санды киргизиңиз:'))
is_simple = True

for i in range(2, n ):
    print(f'{n} % {i} = {n % i}')
    if n % 2 == 0:
        is_simple = False
        break

       

n = 5
for i in range(1, 11):
    print(f'{n} * {i} = {i * n}')


