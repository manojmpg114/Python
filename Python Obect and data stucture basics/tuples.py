#tuples are similar to lists except that they are immutable i.e once an element is inside a tuple it can not be reassigned
#tuples use paraenthesis: (1,2,3)

t = (1,2,3)

mylist = [1,2,3] #list because square brackets

print(len(t))

print(t)

t = ('one', 2)
print(t[0])
print(t[-1])

t = ('a','b','a')

print(t.count('a'))

print(t.index('a'))
print(t.index('b'))

print(t)
print(mylist)

mylist[0] = "NEW"

print(mylist)

#t[0] = 'A' #this would cause an error because tuple objects are immutable and don't support item assignment 

#tuples are ideal for data integrity to make sure objects don't get changed or reassigned in larger points of code
