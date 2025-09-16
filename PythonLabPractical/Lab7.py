#Write a program find mean ,median ,mode for the given set of numbers in a list .
#Write a function unique to the find all the sequence of the element of a line .
numbers = [5, 2, 9, 2, 5, 7, 3, 5]

mean = sum(numbers) / len(numbers) 

numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
max_freq = max(frequency.values())
mode = [k for k, v in frequency.items() if v == max_freq]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
