
#This is a program to sort a list of numbers in ascending and descending order
#This is a list to hold the numbers
numbers = []
#This is a for loop to take input from the user
for i in range(0, 5):
    num = int(input("Enter a number: "))
    numbers.append(num)

#I will sort the list in ascending order
numbers.sort()
print("Numbers in ascending order: ", numbers)

#I will sort the list in descending order
numbers.reverse()
print("Numbers in descending order: ", numbers)