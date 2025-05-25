# This program counts the number of vowels in a given string
#This is a variable to hold the count of vowels
count = 0
#Take the string as input from the user
user_input = input("Enter a string: ")
#Convert the string to lower case
user_input = user_input.lower()
#A list of vowels
exceoption_chars = ['a', 'e', 'i', 'o', 'u']
result = user_input
#A for loop to test the user input
for char in user_input:
    if(char in exceoption_chars):
        count += 1
        result = result.replace(char, '')
        result = result.strip()
#We are going to print the count of vowels in the string        
print("Number of vowels in the string is: ", count)
## We are going to print the string after removing the vowels
print("String after removing vowels: ", result)








