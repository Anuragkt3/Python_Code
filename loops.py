''' 
for i in "Myblog":
    print(i,'?')

for i in range(15,20):
    print(i)


for i in range(1,11):
    print(i)

for i in range(1,21,2):
    print(i)

for i in range(20,0,-2):
    print(i)

num = int(input("Enter any number"))
for i in range(1,11):
    print(num*i)    

num = int(input("Enter the number"))
for i in range(1,11):

num = int(input("Enter the number:"))
p = 1
while(num):
    r = num % 10
    p = p*r
    num = num//10
print("Product of digits is",p) 

num = int(input("Enter the number: "))
f = 1
for i in range(1,num+1):
    f = f*i
print("Factorial is",f)    

# Program to sum to digits of a number
i = int(input("Enter the number"))
sum = 0
while(i>0):
    sum = sum+i%10
    i = i//10
print("The sum of digits is",sum)    

# Sum of cube of digits
i = int(input("Enter the number "))
sum = 0
while(i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10
print("The sum is",sum)  


#Product of digits
i = int(input("Enter the number: "))
prod = 1
while(i>0):
    prod = prod*(i%10)
    i = i//10
print("The product is",prod) 


# Check wether a number is Armstrong or not
i = int(input("enter the number"))
sum = 0
ori = i
while(i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10
if ori==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")        '''

# Find sum of even and product of odd number

i = int(input("Enter the number: "))
sum = 0
prod = 1
while(i>0):
    d = i%10
    if d%2 == 0:
        sum = sum+d
    else:
        prod = prod*d
    i = i//10
print("The sum is",sum,"The product is",prod)                        






