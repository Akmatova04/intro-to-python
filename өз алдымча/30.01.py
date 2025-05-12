# products = {
#     'алма':50,
#     'банан':60,
#     'киви':100,
# }
# products_str = ''
# for name,value in products.items():
#     products_str += f'{name} - {value}\n'
# print(products_str)

# with open('products.txt','w') as f:
#      f.write(products_str)

# with open('products.txt', 'w') as f:
#     f.write(products_str)

# with open('products.txt', 'r') as f:
#     content = f.read()

# with open('products.txt', 'a') as f:
#     f.write('potato - 40')

# with open('products.txt', 'r') as f:
#     products = f.readlines()
# amount = 0
# for product in products:
#     product_data = product.split()
# print(product_data)
# price = product_data[-1]
# amount += int(price)
# print(price)
# print(amount)



# with open("products.txt", "w") as f:
#     f.write("Алма,100\n")
#     f.write("Банан,150\n")
#     f.write("Сабиз,80\n")


# with open("products.txt", "a") as f:
#     f.write("Нан,50\n")

# with open("products.txt", "r") as f:
#     for i in f:
#         print(i.strip())


# total_sum = 0
# with open("products.txt", "r") as f:
#     for i in f:
#         _, price = i.strip().split(",")
#         total_sum += int(price)


# with open("summary.txt", "w") as f:
#     f.write(f"{total_sum} \n")

# print(f'\n{total_sum} ')


with open("cities.txt", "w") as f:
    f.write("Ош,122220000\n")
    f.write("Бишкек,150000\n")
    f.write("Баткен,80000\n")

with open("cities.txt", "a") as f:
    f.write("Нарын,50000\n")

filtered_cities = []
with open("cities.txt", "r") as f:
    for i in f:
        population = int(i.split(',')[-1])
        if population > 100000:
            filtered_cities.append(i)
print(filtered_cities)

with open('filtered_cities.txt', 'w') as f:
    f.writelines(filtered_cities)

