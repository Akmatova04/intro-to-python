# # phone_book = {
# #     'nazira':990686854,
# #     'doka':555439970,
# #     'miki':778676390,
# # }
# # phone_book.update({
# #     'nuru':776381898,
# # })
# # del phone_book['doka']
# # print(phone_book)
# # if 'Ali' in phone_book:
# #     print(f'Aliнин номери:{phone_book['Ali']}')
# # else:
# #     print('Not found')

# # store = {
# #         'vegetables':['potato','пияз','сабиз'],
# #         'fruits':['банан','киви','алма'],
# #     }
# # print(store)
# # store ['fruits'].append('апелсин')
# # store ['fruits'].append('груша')
# # store ['vegetables'].remove ('potato')
# # print(store)
# # if 'Snacks'not in store :
# #     store['Snacks']=[]
# # store['Snacks'].append('chips')
# # print(store)
# # if 'fruits' in store:
# #     print('fruits категориясындагы товарлар:',store['fruits'])
# # else:
# #     print('Категория табылбай калды')


books = {}
books.update(
    {
    'Война и мир':'Лев Толстой',
    'Кылмыш жана жаза':'Федор Достоевский',
    'Уста жвна Маргарита':'Мехаил Булгаков',
}
)
print(books)

print(books['Война и мир'])
print(books.get('Война и мир'))

books['Анна Каренина'] = 'Лев Толстой'


del books['Кылмыш жана жаза']

print(books)

for book  in books:
    print(book)
    print(books[book])
    print(f'Книга: {book},')












# # books['Анна Каренина'] = 'Лев Толстой'
# # if'Кылмыш жана жаза'in books:
# #     del books ['Кылмыш жана жаза']
# # print('Каталогдогу китептер')
# # for title, autor in books:
# #     print(f'Китеп:{title},Автор')





# # books.update({
# #     'Анна Каренина': 'Лев Толстой',
# #     })
# # del books['Кылмыш жана жаза']

# # print(books)

# # if 'harry poter' not in limbraru_catalig:
# #     print(f'{limbraru_catalig['harry poter']}')

# # Создаем словарь cities
# cities = {}


# cities.update(
#     {
#     "Бишкек": 50,
#     "Ош": 60,
#     "Токмок": 70
# }
# )
# print(cities['Ош'])
# print(cities['Бишкек'] + 100)
# cities['Бишкек']+= 100
# print(cities)