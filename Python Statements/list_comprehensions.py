mystring = "Hello"

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)


# format of list comphresension means we can do this in a single line / with less fluff

mylist = [letter for letter in mystring]

print(mylist)

mylist = [x for x in 'word'] #as long as the x is the same object name it would work

print(mylist)

mylist = [x for x in range(0,11)]

print(mylist)

mylist = [x**2 for x in range(0,11)] #now we are doing the operation x squared for each element x in the range 0-11

print(mylist)

mylist = [x for x in range(0,11) if x%2 ==0] #in this case we are making an if statement in the loop to build the list

print(mylist)

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp +32) for temp in celcius] #code 1 flattened version of append functionality in the loop; list comphrehension

print(fahrenheit)

#the long way to get the same result for fahrenheit is this:

fahrenheit = [] #block of code under this is the exact same as the portion referenced code 1 line 35

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))

print(fahrenheit)

results = [x if x%2 == 0 else 'ODD' for x in range(0,11)] #writing it in this method might make it harder to read especially if you dont look at
#list comprehensions for months at a time 
#this is an if else and you will notice that the if statement in this case is before the loop while in previous appending cases 
#the if condition was after the loop; again can be confusing and if it does become so its not worth doing a if else one liner 

print(results)

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]

print(mylist)