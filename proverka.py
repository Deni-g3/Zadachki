numbers=[]

for i in range(6):
    enter = int(input('Enter the number:'))
    numbers.append(enter)

search = int(input('Enter the number to search:'))

if search in numbers:
    print('The number is in the list.')
else:
    print('The number is not in the list.')

