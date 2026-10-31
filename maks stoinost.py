numbers_list = []


for i in range(5):
    number = int(input('Enter the number:'))
    numbers_list.append(number)

print('List:', numbers_list)
print('Maximum number:', max(numbers_list))
print('Minimum number:', min(numbers_list))
print('Sum of numbers:', sum(numbers_list))

avarage = sum(numbers_list) / len(numbers_list)

print('Avarage of numbers:', avarage)
