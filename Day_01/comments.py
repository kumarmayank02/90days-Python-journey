



#Hii this is kumar Mayank don't remove it ,python is here 
#to keep the information for the next day understanding the content
#so dont remove it .

print("Hii i am good boy ");



'''******Python Comments****
A comment is a part of the coding file that the programmer 
does not want to execute, rather the programmer
uses it to either explain a block of code or 
to avoid the execution of a specific part of code while testing.'''

#This is a 'Single-Line Comment'
print("This is a print statement.")
print("Hello World !!!") #Printing Hello World
print("Python Program")
#print("Python Program")

'''Multi-Line Comments:
To write multi-line comments you can use 
‘#’ at each line or you can use the multiline string.'''

'''Example 1: The use of ‘#’.
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.'''
  
p=7
if(p>5):
    print("p is greater than 5");

else:
    print("p is not greater than 5");

'''*****Escape Sequence Characters*****
To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:'''


'''print("This doesnt "execute")'''  #it will not be execute'''
print("This will \" execute") #it will be execute'''



#****** MORE ON Print STATEMENT*********


#The syntax of a print statement looks something like this is following
#print(object(s), sep=separator,end=end,file=file,flush=flush)

print("Hey",6,7,sep="-",end="008\n")
print("kumar Mayank")


'''Other Parameters of Print Statement
1.object(s): Any object, and as many as you like. Will be converted to string before printed.
2.sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3.end='end': Specify what to print at the end. Default is '\n' (line feed)
4.file: An object with a write method. Default is sys.stdout'''


