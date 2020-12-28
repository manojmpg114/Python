my_list = [1,2,3]

my_list = ['String', 100, 23.2]

print(len(my_list))

print(my_list[0])

print(my_list[1:])

another_list  = ['four', 'five']

print(my_list + another_list) 

combined_list = my_list + another_list

print(f'combined list: {combined_list}' )

combined_list[0] = 'ONE ALL CAPS'

print(f'combined list update: {combined_list}')

#we can also add elements to the end of a list with the list methods like append

combined_list.append('six')

print(combined_list)

combined_list.append('seven')

#remove items from a list with the pop function 

print(combined_list)

print(combined_list.pop())

print(combined_list)

popped_item = combined_list.pop()

print(combined_list)

#remove by index using pop would return and remove the item at that index, reverse indexing also works here

combined_list.pop(0)

print(combined_list)

new_list = ['a', 'e', 'i', 'o', 'u']

num_list = [4,1,8,3]

#we can sort these new list and num lists with the sort functions 

new_list.sort() #doesn't return anything just sorts in alphabetical order and does the sort in place so new list is the same variable 

#special type in python called None which is the return value ofa function that returns nothing 
#can be used as a place holder 

print(new_list)

num_list.sort()

print(num_list)

#reversing the list is just the reverse method 

num_list.reverse()

print(num_list)