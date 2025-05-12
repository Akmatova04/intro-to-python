# number = list (range(1,11))
# print(number)

# product = ['banana','apple','cherry']
# print(product[1])

# number = [1,2,3,4,5]
# print(sum(number))

# name = 'Nazira Akmatova'
# print(name[::-1])

# numbers = [1,2,3,4,5,3]
# for number in numbers:
# 	if number % 2 == 0:
# 		print(number,'Жуп сан')
# 	elif number %2 !=0:
# 		print(number,'Так сан')

# list_1 = [1,2,3,4,5,6,7,8,9,0]
# list_2 = [0,1,2,3,4,5]
# print(list_1 + list_2)

# list_1 = [1,2,3,4,5,6,7,8,9,0]
# print(max(list_1))
# print(min(list_1))

# list_1 = [1,2,3,4,5,6,7,8,9,0,0,1,1,2]
# print(set(list_1))

# for i in range(1,6):
# 	print(i)
	
# for i in range(1,101):
# 	if i % 2 ==0:
# 		print(i,'Жуп сан')
# 	elif i % 2 !=0:
# 		print(i,'Так сан')

# num = int(input('Санды киргизиңиз: '))
# total = 0
# for i in range(5):
# 	total += num
# print(total)

# i = 10
# while i >=1:
#     print(i)
#     i -=1

# i = 12
# while i >=1:
#     print(i)
#     i-=1


# for i in range(1,50):
#     if i %3 ==0:
#         print(i)

# number  = (10,20,30,40)
# for i in number:
#     print(i)

# text = input('Сап киргизиңиз: ')
# for i in text:
#     print(i)

# num = int(input ('Санды киргизиңиз: '))
# total = 0
# while True:
#     if num ==100:
#         break
#     total+=num
# print(total)

# num = int(input('Санды киргизиңиз (100 кирсе сан токтойт)' ))
# total=0
# while True:
#     num = int(input('Санды киргизиңиз (100 кирсе сан токтойт)' ))
#     if num ==100:
        
#         break
#     total += num
#     print('Жыйынтык',total)



# name = 'hello word'
# print(name)

# name = input('Атыңызды киргизиңиз:')
# print('Сaлам',name)





# number = int(input('Санды киргизиңиз:'))
# if number % 2== 0:
#     print('Жуп сан')
# else:
#     print('Так сан')

# num = 10
# decimal = 3.12
# word = 'python'
# is_true = True
# print(type(num),type(decimal),type(word),type(is_true))


# text = input('Сап киргизиңиз:')
# print(f'Саптын узундyгу:' ,len(text))

# num =10
# name = 'nazira'
# num = 1.2
# is_true = True
# print(type(num),type(name),type(is_true))

# programma = input('Сүүйүктүү программаңызды киргизиңиз ')
# print('Сүүйүктүү программаңыз:',programma)

# text = input('Сап киргизиңиз: ')
# for i in text:
#     print(i)
# text = input('Сапты киргизиңиз; ')
# for i in text:
#     print(i)


# with open('test.txt','w') as f:
#    f.write('Hello world')

# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open('test.txt','a') as f:
#     f.write('Hello world')  

# name = ['Nazira','Doka','Aida']
# print(name)

# name = ('nazira','doka','aida')
# print(name)


# unique_number = [1,2,3,4,5,5,6,7,8,9,12,3,4,4,1]
# print(set(unique_number))

# name = {
#     'name':'nazira',
#     'age':24,
#     'city':'baken', 
# }
# print(name.keys())
# print(name.values())
# print(name.items())

# number = int(input('Санды киргизиңиз: '))  
# number = []
# for i in range(10):
#     number.append(number)
# number.sort()
# print(number)
# print(number[0])

# number = input('Санды киргизиңиз: ')
# sorted_list = sorted([int(i) for i in number.split(',')])
# print(sorted_list)


jornal = {
    'Акматова Назира':'90',
    'Акматова Айда':'67',
    'Акматов Дока':'30'
}
if jornal >=75:
    print('Эң жакшы')
elif jornal >=50 == 75:
    print('Жакшы')
elif jornal >=25 == 50:
    print('Канаттандырарлык')
else:
    print('Канаттарбайт')