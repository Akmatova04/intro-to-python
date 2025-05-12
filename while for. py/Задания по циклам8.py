

# n = int(input('Санды киргизиңиз'))

# for i in range(2, n + 1, 2):
#     print(i)
#     if i % 6 == 0:
#          break



# n = int(input('Санды киргизиңиз'))
# for i in range(n, 0, -1):
#     print(i)



# n = int(input("Сан киргизиңиз: "))
# print("Бөлүү таблицасы:")
# for i in range(1, 11):
#     result = n / i
#     print(n,'/',i,'=', n/i)



n = int(input("Сан киргизиңиз: "))

for i in range(2, n + 1): 

    is_prime = True
    for n in range(2, i): 
        if i % n == 0:  
            is_prime = False
            break
    if is_prime:  
        print(i)










