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
print("Product of digits is",p) '''

num = int(input("Enter the number: "))
f = 1
for i in range(1,num+1):
    f = f*i
print("Factorial is",f)    