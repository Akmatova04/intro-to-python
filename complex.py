# def add(*numbers):
#     amount = 0
#     for i in numbers:
#         if i % 2 == 0:
#             amount += i
#     return amount

# print(add(1,2,3,6,5))
# result = add(1,2,3,4,1)
# print(result)
# print(add(result,1,2))


# def describe_person(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# describe_person(name='nazira',age=20,city='batken')


# def add_to_dict(**kwargs):
#     students_names = []
#     students_names.append(kwargs.get('name'))
#     print(students_names)
# add_to_dict(name='nazira',age=20,city='batken')

# def is_even(number):
#     if number %2 == 0:
#         return True
#     else:
#         return False
    
# numbers = range(1,100)

# filter_numbers = []
# for number in numbers:
#     is_even(number)
#     filter_numbers.append(number)
# print(filter_numbers)

# filter_numbers = list(filter(is_even, numbers))
# print(filter_numbers)

# numbers = range(1,100)

# filter_numbers = list(filter(lambda number: number % 2 == 0,numbers))
# print(filter_numbers)

# numbers = range(1,100)
# mapped_numbers = list(map(lambda number: number **2,numbers))
# print(mapped_numbers)

# numbers = range(1,100)
# mapped_numbers = list(map(lambda number: number *2,numbers))
# print(mapped_numbers)


names = ['Doka','Aida','Nazira']
filterred_names = list(filter(lambda x: len (x)<5,names))
print(filterred_names)

# mapped_names = list(map(lambda x: f'Ученик {x[0]+1}: {x[1]}',enumerate(names)))
# print(mapped_names)


