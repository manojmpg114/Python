#iterable means you can interate over the object 
#perform an action through every element of an object
#strings we can interate over the characters
#items in a list
#keys in a dictionary etc

#syntax of a for loop
# my_interable = [1,2,3]
#for item_name in my_interable:
    #print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]

for nums in mylist: #nums variable name represents objects in my collection
    print(nums)

for jelly in mylist:
    print('hello')

for num in mylist:
    #Check for evens
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum) #if we took out of code block would only give us the final sum

print(f"Total sum of mylist: {list_sum}")

mystring = "Hello World"

for letter in mystring:
    print(letter);

for letter in "Taco Tuesday":
    print(letter);

tup = (1,2,3)

for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)

for (a,b) in mylist: #by writing the for variable in the same manner as a tuple we can do tuple unpacking
    print(a) #what tuple unpacking does is by mimicing the tuple style we can take a single part of the tuple in this case just the first item in each tuple is marked var 'a'
    print(b) #the second item would be in var 'b'

print('\n')
for (a,b) in mylist:
    print(a)

#it is also more common to do this without the parenthesis and it still works the same 
print('\n')
for a,b in mylist:
    print(b)

mylist = [(1,2,3),(5,6,7),(8,9,10)]
print('\n')
for a,b,c in mylist:
    print(b)

d = {'k1': 1, 'k2':2, 'k3':3}
print('\n')

for item in d: #this statement would only allow us to interate through the items of the dictionary
    print(item)

for item in d.items(): #this one makes it key value pairs
    print(item)

for k,v in d.items():
    print(v) #this method we can do the unpacking and only print the values of the dictionary (tuple unpacking)

for value in d.values():
    print(value) #dictionaries are unordered so no gaurantee things come back in the order we put them

