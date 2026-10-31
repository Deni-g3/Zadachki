numbers = []

for i in range(5):
    chislo = int(input('Enter the number:'))
    numbers.append(chislo)

print('The first list of numbers:', numbers)

new_number = int(input('Enter a new number in the list:'))
numbers.append(new_number)


remove_number = int(input('Enter the number you want to remove:'))

if remove_number in numbers:
    numbers.remove(remove_number)
else:
    print('The number doesnt exist in the list.')

print('The final list of numbers is:', numbers)