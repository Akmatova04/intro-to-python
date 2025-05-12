'''' Башка элементти кошуу'''
# colors =['Жашыл','көк','кызыл']
# colors [1]='сары'
# print(colors)

''''append аркылуу элементтерди кошуу'''
# name = []
# name.append('nazira')
# name.append('nazi')
# name.append('naz')
# print(name)

'''' зринтте эленметтерди кошуу мисалы салам деген сөз сыяктуу'''
# def salamdahuu (at):
#     return f'Salam,{at}!'
# print(salamdahuu('nazira'))


'''''Сандарды кошуу'''
# def summa(sandar):
#     return sum(sandar)
# print(summa([11,22,3,33,33]))

''' Сандарды удалить кылуу'''
# sandar = list(range(1,21))

# for san in range(3,21,3):
#     sandar.remove(san)
# print(sandar)


'''5 сөздон коп создорду очуруу'''
sozdor =['nazira','mirlan','aida']
for soz in sozdor[:]:
    if len(soz)<5:
        sozdor.remove(soz)
print(sozdor)

# def tamgalar(sap):
#     unduu_tamgalar = 'аеиоуыэяю'
#     result = ''
#     for tamga in sap:
#         if tamga not in unduu_tamgalar:
#             result += tamga
#     return result
# print(tamgalar('привет'))


# def kvadrat_tizmesi(san):
#     result = []
#     for i in san:
#      result.append(i ** 2)

#     return result
# print(kvadrat_tizmesi([1,2,3,4,5,6,7]))

