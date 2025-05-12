

 #№3- тапшырма
file_name = input("Файлдын аты: ")
search_word = input("Издөөчү сөз: ")

#окуу
with open(file_name, 'r') as file:
    text = file.read()               # Бардык текстти окуйт
    words = text.split()             # Текстти сөздөргө бөлөт
    print(words)
    count = words.count(search_word) # Сөздүн канча жолу жолуктарын эсептейт


print(f"'{search_word}' сөзү {count} жолу жолукту.")
