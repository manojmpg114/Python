#taking specfic charAt() in python include the use of [] square brackets
#within the brackets we use a number index to indicate positions
#python alsos reverse indexing so referencing the -1 position would refelct the last character in the string

#slicing lets you do substring() of a string in python 
#sice syntax: [Start:Stop:Step]
#start is numberical index the slice starts 
#stop is index we go up to but DOES NOT INCLUDE that index
#step is the size of the jump we take - need more information on that reference 

print('hello')
print('world')

'this is a string'

print('this is a string')

print("i'm going on a run")

print('hello \n world') #\n is he new line key command and \t would be the tab built in function 

#length of a string is the len function

print(len('I am'))

my_string = "Hello world"

print(my_string)

print(my_string[0])
print(my_string[8])

print(my_string[-2])

#last letter of the string
print(my_string[-1])

#slicing is also substrings per java terms 

mystring = 'abcdefghikj'

print(mystring[2:]) #we took everything from the 2nd index 0,1,2 to th end of the string which is noted by the : 

#if we wanted everything up to the 3rd index, up to not including its like this 
print(mystring[:3])

print(mystring[3:6])

print(mystring[1:3])

#how slicing step size works 

print(mystring[::2]) #so we only take the 2nd character from the beining to the end 

#GOOD METHOD OF USING THIS FOR REVERSING A STRING IS mystring[::-1]

print(mystring[::-1]) #how this works is splicing / substring taking steps from the back to the front 
#above start is empty so from the beginning, stop is empty so to the last, then -1 steps means from index 0 we start from the back not the front 
#if we wanted to interate from the front it would be mystring[::] or mystring[::1]
#by default steps start are an interation of 1