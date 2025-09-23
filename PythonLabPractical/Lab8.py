#Write a function dups to find all Duplicates in the list  
#list1=5,7,8,9,10,7,8,9,10,50,16,60}
def find_duplicates(lst):
    duplicates = []  # List to store duplicate values
    seen = set()  # Set to store unique values we have already seen

    for item in lst:  # Loop through each item in the list
        if item in seen:  # If the item has already been seen, it's a duplicate
            duplicates.append(item)  # Add it to the duplicates list
        else:
            seen.add(item)  # Otherwise, add it to the seen set

    return duplicates  # Return the list of duplicates

#Example usage
my_list = [5,7,8,9,10,7,8,9,10,50,16,60]
print(find_duplicates(my_list))  # Output: [1, 2, 3]
