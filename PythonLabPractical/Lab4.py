#Write a program using a  while loop that asks user for a number and print a countdown from that number

''' num=int(input("Enter the number :")
 
while num > 0:
    print(num)
    num -= 1

print("Countdown finished")'''

#Write a program to count the number of characters in the string and print countdown from the number


user_input = input("Enter a string ")

char_count = len(user_input)

print("Number of characters:", char_count)

print("Countdown:")
for i in range(char_count, 0, -1):
    print(i)






