#A program to print the locations of 'i' in a given string

#This is a variable to hold the sentence
sentence = input("Enter a sentence: ")

#This is a variable to hold the character to find
my_char = 'i' 

#This is a list to hold the locations of the character
locations = []  

#A for loop to find the locations of the character
for index, char in enumerate(sentence):
    if char == my_char:
        locations.append(index+1)
#We are going to print the locations of the character in the sentence
print(f"The character '{my_char}' is found at the following locations: {locations}")