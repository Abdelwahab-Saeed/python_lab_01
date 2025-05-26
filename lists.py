#A program to list some lists (multiplication table)

#The big list to hold the lists
container = []

#Take user input for the number of lists
limit = int(input("Enter the number of lists you want to create: "))
#A for loop to create the lists
for i in range(1, limit+1):
    #A new list to hold inner lists
    inner_list = []
    #A for loop to create the inner lists
    for j in range(1, i+1):
        inner_list.append(i * j)
    #Append the inner list to the container
    container.append(inner_list)

print("The lists are: ", container)



