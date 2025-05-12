
login = 'admin'
password = '1234'

login = input("Логиниңизди киргизиңиз: ")
password = input("Сырсөзүңүздү киргизиңиз: ")

if login == "admin" and password == "1234":
    print("Кирүүгө уруксат берилди.")
elif login == "admin" and password != "1234":
    print("Сырсөз туура эмес.")
else:
    print("Колдонуучу табылбады.")


number = int(input('Санды киргизиңиз'))
if number % 2 == 0:
    print('Жуп сан')
else:
    print('Так сан')


score = int(input('Баллды киргизиңиз'))
if score >= 80:
    print('Эң жакшы')
elif 75 <= score < 80:
    print('Жакшы')
elif 50 < score < 75:                          
    print('Канаттандырарлык')
else:
    print('Канаттаръндырбайт')

year = int(input('Жылды киргизиңиз'))
if (year %4 == 0 and year %100 != 0) or (year %400 ==0 ):
    print('Високостность ')
else:
    print('Високосность эмес')

price = int(input('Товардын баасын киргизиңиз'))
if price > 1000:
    print('Сизге 1% арзандатуу берилет')
else:
    print('Сизге арзандатуу берилбейт')

age = int(input('Жашыңызды киргизиңиз'))
has_pass = input('Пропускаңыз барбы?(да\нет):')

if age >= 18 and has_pass == "да":
        print('Сиз кире аласыз')
elif age >= 18 and has_pass == "нет":
    print('Сизге пропуска керек')
else:
      print("Сизге эрте")

name = input('Атыңызды киргизиңиз')
age = int(input('Жашыңызды киргиңиз'))
has_license = input('Айдоочулук күбөлүк барбы? (да\нет):')

if age > 18 and has_license == "да":
    print('Сиз машина айдай аласыз')
elif age > 16 and has_license == 'нет':
    print('Сиз автошколада окуп жатасыз')
else:
    print('Сизге машина айдоого эрте')

































