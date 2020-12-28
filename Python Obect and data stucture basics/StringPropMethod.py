#immutability of strings aka can't change so no item assignment in python
#to replace the S in sam to P to make pam you need to make a new string declaration for pam 

name = "Sam"

last_letters = name[1:]

print(last_letters)
print('P' + last_letters)

x = 'Hello world'
print(x + " it is a beautiful outside!")

x = x + " it is beautiful outside!"

print(x)

print(x*2)

#if we tried to concatenate a string with a number it would cause errors 

#2 +3 is fine "2" + "3" is fine 
#5              23
#2 + "3" would result in an error 

x =  'Hello world'
# comment x = x.upper()
print(x.upper())

#without the () python reads x.upper as a request to what it is aka its a function called upper 

#x.split would split the string into a list 
print(x.split())

x = 'Hi this is a string to split'

print(x.split()) #we can also split on other characters other than white space, it would remove that character in the result 

#x.split(i) would include the white spaces but not the 'i's in the list
print(x.split('i'))

#String interpolation is putting a variable into a string 

#STRING FORMATTING with .format() method or f-strings (formated string literals)

#formating with .format() method

print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

#we can also assign keywords
print('The {q} {b} {f}'.format(f='fox', b ='brown', q ='quick'))

print('The {f} {f} {f}'.format(f='fox', b ='brown', q ='quick'))

#float formatting follows "{value:width.precision f}"

result = 100/777
print(result)

print("The result was {r}".format(r=result))


print("The result was {r:1.3f}".format(r=result))


name = 'Manoj'
print(f'Hello, his name is {name}') #the f strings is the new way to combine variables with string literals more like java and other programs where its easier
#combine the two

name = 'David'
age = 26

print(f'{name} is {age}') #always remember its f then string 

