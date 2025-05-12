# def number(*numbers):
#     amount = 0
#     for i in numbers:
#         if i % 2 !=0:4
#         amount += i   
#     return amount

# result = number(1,2,3,4,5,6)
# print(result)

# def find_max(*args):
#     return max(args)
# print(find_max(100,50,200,150))

# def describe_car(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# describe_car(марка='toyta',жыл=2020,түс='көк')

# def user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}:{value}')
# user_info(name='Nazira',age=24,city='Batken')

# def filter_positive_number(*numbers):
#     return list(filter(lambda x: x > 0, numbers))

# filterred_numbers = filter_positive_number(-10,15,-15,20,0,-3,30)
# print(filterred_numbers)

# names = ['Nazira','Doka','Aida']
# filterred_names =list(filter(lambda x: len(x)>5,names))
# print(filterred_names)

# numbers = range(1,51)
# mapped_numbers = list(map(lambda number: number **2,numbers))
# print(mapped_numbers)

# numbers = range(1,51)
# mapped_numbers = list(map(lambda number: number + (number * 0.5), [100, 200, 300]))
# print(mapped_numbers)


# students = ['Nazira','Doka','Aida']
# mapped_students = list(map(lambda x:f' {x[0]+1}: {x[1]}',enumerate(students)))
# print('\n'.join(mapped_students))
# # print(mapped_students)

# product = ['apple', 'banana','orange']
# mapped_product = list(map(lambda x: f'Товар{x[0]+1}: {x[1]}',enumerate(product)))
# print('\n'.join(mapped_product))
# # print(mapped_product)



from PIL import Image

# Жүктөлгөн сүрөттүн жолун ачабыз
image_path = "/mnt/data/resized_image_100x50cm_300dpi.png"
image = Image.open(image_path)

# Бир аз кичирейтип, мисалы 80% кылабыз
scale_factor = 0.8
new_width = int(image.width * scale_factor)
new_height = int(image.height * scale_factor)

# Кайра өлчөмдөө
resized_smaller = image.resize((new_width, new_height), Image.LANCZOS)

# Сактоо
smaller_path = "/mnt/data/resized_image_80_percent.png"
resized_smaller.save(smaller_path)

smaller_path
