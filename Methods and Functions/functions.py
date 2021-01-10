# functions allow us to create blocks of code that can be asily exdcuted many times without needing to rewrite the blocks of code

# def Keyword 

#python uses snake casing for the naming of functions like this: name_of_function(): 
# all lowercase with underscores in the name, we have parenthesis here at the end to pass in arguments and parameters then ending with a colon 

def name_of_function(name):
    ''' Docstring explains functions 
    '''
    print("Hello " + name)

name_of_function("Manoj")

#typically we use the return keyword inside of a function so we can return results from the function 

def add_function(num1,num2):
    return num1+num2

result = add_function(1,2)

print(result)

def say_hello():
    print('hello')
    print('are')
    print('you')


say_hello()

def say_hello(name = 'Default'):
    print(f'Helo {name}')

say_hello("David")

say_hello() #without input we over rided this method it needs to have a point of input, no empty constructors so we need to assign a default value

def add_num(num1, num2):
    return num1+num2

result =add_num(10,20)

print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,30)

result = print_result(10,20)

print(result)

result = return_result(10,23)

print(result)

def myfunc(a,b):
    print(a+b)
    return a+b

results = myfunc(2,3)

print(results)

def sum_numbers(num1,num2):
    return num1+num2

result = sum_numbers(10,20)
print(result)

result = sum_numbers('10','20') #python is dynamically typed so the type of datas wasn't checked 
print(result)

#when getting input we need to make sure we are getting and returning the right data types

