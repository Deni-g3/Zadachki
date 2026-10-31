numbers=[]

for i in range(7):
    enter = int(input('Enter the numbers:'))
    numbers.append(enter)

print('The list of numbers now is:', numbers)

numbers.sort()

print('The numbers sorted from the biggest to smallest:', numbers)

numbers.sort(reverse=True)

print('The numbers sorted from the smallest to biggest:', numbers)

numbers.reverse()
print('The numbers in reverse order:', numbers)