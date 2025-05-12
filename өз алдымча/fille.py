# with open('names.txt','w')as f:
#     f.write('Айбек,\nЭлиза\nАлия\n')

# with open('names.txt','a')as f:
#     f.write('Мирлан\nАтиргүл\n')

# with open('names.txt','r')as f:
#     name = f.read()
#     print(name)


# def aad(fail_name):

#     with open('names.txt','w',encoding='UTF-8') as f:
#         name = input('Атыңызды киргизиңиз:').strip()
#         user = input('Атаңыздын атын киргизиңиз:').strip()
#         f.write(f"{name}, {user}")
# def rif(fail_name):      
#     with open('names.txt','r',encoding='UTF-8') as f:
#         for i in f:
#          name,user = i.strip().split(',')
#     print(name,user)
# fail_name = 'names.txt'
# aad(fail_name)
# rif(fail_name)

with open('names.txt','w',encoding='UTF-8') as f:
        name = input('Атыңызды киргизиңиз:').strip()
        user = input('Атаңыздын атын киргизиңиз:').strip()
        f.write(f"{name}, {user}")
with open('names.txt','r',encoding='UTF-8') as f:
        for i in f:
         name,user = i.strip().split(',')
        print(name,user)


