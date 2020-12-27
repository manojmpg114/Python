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

