numbers=[]

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input("Enter an number: "))
    numbers.append(element)

print('The list of numbers is:', numbers)
print('The number of elements in the list is:', len(numbers))