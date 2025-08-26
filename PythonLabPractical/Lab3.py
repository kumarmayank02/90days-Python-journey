'''#Write a program to find nth fabonacci number without function 

n = int(input("Enter the value of n: "))

a, b = 0, 1

if n == 0:
    print(f"The {n}th Fibonacci number is: {a}")
elif n == 1:
    print(f"The {n}th Fibonacci number is: {b}")
else:
 
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    
    print(f"The {n}th Fibonacci number is: {b}")'''


#write a program to sum of nth number
num = int(input("Enter the number: "))  
sum = 0 
for i in range(1, num + 1): 
    sum += i  
print("Sum is:", sum)



