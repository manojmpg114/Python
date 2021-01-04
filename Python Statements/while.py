# synax for while loops; while some_boolean_condition:
#   do something
#  else:
# do something else

x = 50

while x < 5:
    print(f'The current value of x is {x}')
    x = x+1 #you can also write x += 1
else: #if the condition never went true the else statement can still print
    print("X IS NOT LESS THAN 5")

#jupitar notebooks can interpt the cell marked by a star should a infinite loop run

# keywords like break, continue, and pass in loops to add additional functionality
# break: breaks out of the current loop enclosing - same as java
# continue: goes to the top of the closest enclosing loop
# pass: does nothing at all --

x = [1,2,3]

for item in x:
    # comment isn' enough for loops it would cause an error in python 
    #to avoid syntax errors just the pass method so we can hold the space and make the loop valid
    pass

print('end of my script')

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue #this will come more naturally later on
    print(letter)

for letter in mystring:
    if letter == 'a':
        break 
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

