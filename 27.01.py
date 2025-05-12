# def add(number_1, number_2):
#     return number_1 + number_2
# result = add(10,10)
# result2 = add(100,100)
# print(f'{result} \n {result2}')

# def sub(number_1,number_2):
#     return number_1 - number_2
# result = sub(10,10)
# result2 = sub(101,100)
# print(f'{result} \n {result2}')

# def sub(number_1,number_2):
#     return number_1 * number_2q
# result = sub(10,10)
# result2 = sub(101,100)
# print(f'{result} \n {result2}')

# def calculate_points(points):
#     goot_points = []
#     bad_points = []
#     print(points)

#     for point in points:
#         print(point)
#         if point>=4:
#             '''добавить в список goot_points'''
            # goot_points.append(point)
#         else:
#             '''добавит в список bad_points'''
#             bad_points.append(point)
    # return goot_points ,bad_points 
# points = [2,3,4,5,6,7,8,85,]
# result = calculate_points(points)
# print(result)

def separate_points(points):
    points_dict = {
        'good_points': {},
        'bad_points': {},
    }

    for name, grade in points.items():
        if grade >= 4:
            points_dict['good_points'][name] = grade
        else:
            points_dict['bad_points'][name] = grade

    return points_dict


students_grades = {
    'Aida': 5,
    'Gulzada': 4,
    'Gamburgerbek': 2,
    'Shawarmagul': 3,
    'Nazira':5
}

# separated_grades = separate_points(students_grades)
# print(separated_grades)




# def separate_points(points):
#     points_dict = {
#         'good_points': {},
#         'bad_points': {},
#     }

#     for student,point  in points.items():
#         if point  >= 4:
#             points_dict['good_points'].update({
#                 student:point,
#             })
#         else:
#             points_dict['bad_points'].update({
#                   student:point,
#             })

#     return points_dict


# points = {
#     'Aida': 5,
#     'Gulzada': 4,
#     'Gamburgerbek': 2,
#     'Shawarmagul': 3,
#     'Nazira':5
# }

# result = separate_points(points)
# print(result)

def greet_person (name,age):
    return(f'Салам,{name} сен {age} жаштасың')
print(greet_person('Nazira',20))

