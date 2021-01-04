mylist = [1,2,3]

for num in range(10): #this method can handle slicing of sorts
    print(num)

for num in range(3,10):
    print(num)

for num in range(0, 11, 2): #this version of range generators numbers 0 to 11 with a step of 2
    print(num)


# again range itself is a generator so to view the numbers being listed we can cast the range to a list to build and collect its values

print(list(range(0,11,2)))

# generators generate information without storing it to memoory

# enumerate ;;

index_count = 0

for letter in 'abcde':
    print('At Index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

for item in enumerate(word):
    print(item) #doing it this way with enumerate give us the index coutning and results in tuples
    # we can then use tuple unpacking to get the pairs or indexes as need be  without an additional variable

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5,6]

mylist2 = ['a','b','c']

mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2): #the zip function is able to create tuples out of lists / objects 
    print(item)

for item in zip(mylist1, mylist2, mylist3):
    print(item) #opposite result of decoupling or unpacking a tuple, again we are creating tuples with the lists

#zip is only able to include as many indexes as the shortest portion it is zipping, it won't give an error for zipping less than the max indexs

print(list(zip(mylist1, mylist2, mylist3)))

#in operator lets us check if something is in a list
print('x' in [1,2,3])

print(2 in [1,2,3])

print('a' in 'a world')

#in aso works with keys for dictionaries 
print('mykey' in {'mykey':345})

d = {'mykey': 345}

print(345 in d.values())

print(345 in d.keys())

# min function returns min

mylist = [10,20,30,40,100]

#max function returns max

print(min(mylist))
print(max(mylist))

#random library 

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist) #inplace function so handles operations there
print(mylist)

from random import randint

print(randint(0,100))

print(randint(0,100))

mynum = randint(0,10)

print(mynum)

input('Enter a number here: ') #how to get input form users and this result can be stored 

#input accepts anything given to it as a string

result = input("Enter a number: ")

print(type(result))

print(float(result))

print(int(result))

result2 = float(input("Enter a number: "))

print(result2)