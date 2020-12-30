#start with some basic .txt files

#if used jupiter notebook there is a command to create adn write a text file

""" %%writefile myfile.txt
    Hello this is a text file
    this is the second line
    this is the third line

 """

print("test")

myfile = open('/Users/manojgeorge/Documents/Python/Python Obect and data stucture basics/myfile.txt')
contents = myfile.read()
print(contents)
myfile.close()

print("using with open \n")

with open('/Users/manojgeorge/Documents/Python/Python Obect and data stucture basics/myfile.txt', mode= 'r') as myfile:
     contents = myfile.read()
     print(contents)

with open('/Users/manojgeorge/Documents/Python/Python Obect and data stucture basics/mynewfile.txt', mode= 'r') as f:
    print(f.read())

with open('/Users/manojgeorge/Documents/Python/Python Obect and data stucture basics/mynewfile.txt', mode= 'a') as f:
    f.write('\nFOUR ON FOURTH')

with open('/Users/manojgeorge/Documents/Python/Python Obect and data stucture basics/mynewfile.txt', mode= 'r') as f:
    print(f.read())

#we can also write a file with the mode being w for write
with open('randomfilewriting.txt', mode='w') as f:
    f.write("I CREATED THIS FILE")

with open('/Users/manojgeorge/Documents/Python/randomfilewriting.txt') as f:
    print(f.read())
""" more comments

    myfile = open('myfile.txt')
    myfile.read() #this outputs the contents from myfile.txt and it represents new lines with the \n command 

    if we did the same command again we would get an empty string, this happens because as its read a cursor keeps its place so the cursor would be at the end of the file

    myfile.seek(0)
    myfile.read()

    myfile.seek(0)
    contents = myfile.read()

    myfile.readlines() #this would make a list where each line is populated into a list and ended with a \n aka new line key

    file locations and paths: 

        windows we need to use double backslashes so python doesn't reat the initial slash \ as an escape character 
            myfile = open("C:\\Users\\UserName\\Folder\\test.txt")
        MacOS and Linus you can use forward slashes 
            myfile = open("/Users/YourUserName/Folder/myfile.txt") 

    After we are done working with some files we need to close it so we would write myfile.close()

    we can also run this to auto close when we are done using the file as need be and not worry about closing the file later 

    with open('myfile.txt') as my_new_file:
        contents = my_new_file.read()

 """ 

 #myfile.close()

 