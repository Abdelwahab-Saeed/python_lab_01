#A program to count the number of existence of an expression in a given string
#This is a variable to hold the sentence
sentence = "I am a student at iti and I glad to be a student at iti"
#This is a variable to hold the expression
expression = "iti"
#This is a variable to hold the count of the expression
count = 0
count  = sentence.count(expression)
# We are going to print the count of the expression in the sentence
print(f"The expression '{expression}' appears {count} times in the sentence.")



