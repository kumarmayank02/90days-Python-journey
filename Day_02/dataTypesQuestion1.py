#Q1: Check if a number is integer, float or complex
num = eval(input("Enter a number: "))

if isinstance(num, int):
    print(num, "is Integer")
elif isinstance(num, float):
    print(num, "is Float")
elif isinstance(num, complex):
    print(num, "is Complex")
else:
    print("Unknown type")