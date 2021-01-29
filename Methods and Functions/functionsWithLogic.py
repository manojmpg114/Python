def even_check(number):
    #result = number % 2 == 0
    return number % 2 == 0

even_check(20)
print(even_check(20))


#return true if any number is even inside a list 

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass #pass means don't do anything 

    return False #same level indentation as the for loop so if loop doesn't break return function we default to returning false



print(check_even_list([1,2,3]))

print(check_even_list([1,1,3]))

def check_even_list(num_list):
    #return all the even numbers in a list

    #placeholder variables 

    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

print(check_even_list([1,2,3,4]))

print(check_even_list([1,3,3,1]))
    