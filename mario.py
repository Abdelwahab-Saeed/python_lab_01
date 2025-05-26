#7 mario triangle 
num = int(input("Enter a number: "))
for i in range(1,num+1):
    s = ' ' * (num-i)
    p = '*' * i
    print(s+p)