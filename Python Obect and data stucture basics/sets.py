#sets are unordered collections of UNIQUE elements
#one representitive of the same object 

myset = set() #returns an empty set 

print(myset)

myset.add(1)

print(myset)

myset.add(2)

print(myset)

myset.add(2) #trying to add another 2 which already exists wouldn't change the set 

print(myset) #a bette way to use sets is to cast lists into sets that way we only get the unique values of the list

mylist = [1,1,1,1,1,1, 2,2,2,22, 3,3,3,3, 4]

print(set(mylist)) #shows unique values in the list, casted as a set

