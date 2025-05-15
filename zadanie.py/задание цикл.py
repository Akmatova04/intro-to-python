N = int(input("Санды киргизиңиз: "))
for num in range(1, N + 1):
    if num % 2 == 0:  
        print(num)
    if num % 6 == 0:  
        break

N = int(input("Санды киргизиңиз: "))
for num in range(N, 0, -1):  
    print(num)

N = int(input("Санды киргизиңиз: "))
for i in range(1, 11): 
    result = N / i
    print(f"{N} / {i} = {result:.2f}")  
