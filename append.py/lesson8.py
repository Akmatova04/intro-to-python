# shopping_list = []

# user_product = input('Эмне алгыңыз келет')
# shopping_list.append(user_product)
# print(shopping_list)



# shopping_list = []

# while True:
#     user_product = input('Эмне алгыңыз келет:')
#     shopping_list.append(user_product)
#     print(len(shopping_list))
#     print(shopping_list)
#     if len(shopping_list) >= 3:
#         break

# what_delete = input('Эмнени өчүргүңуүз келет:')
# if what_delete in shopping_list:
#     shopping_list.remove(what_delete)
# print(shopping_list)





numbers = (1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8)
unique_numbers =[]
for number in numbers:
    if number not in unique_numbers:
        print('добавили', number)
        unique_numbers.append(number)
    else:
        print('Такой номер уже есть', number)
print(unique_numbers)