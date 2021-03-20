def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        #if this condition is true return lesser of the even numbers
        if a<b:
            result = a
        else:
            result = b
    else:
        #if one or both numbers are odd 
        if a > b:
            return a
        else:
            return b
    return result

print(lesser_of_two_evens(2,4))

print(lesser_of_two_evens(2,5))

def less_two_evens_simp(a,b):
    if a%2 ==0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    
    return result

print(less_two_evens_simp(4,6))
print(less_two_evens_simp(2,3))

def animal_crackers(text):
    words = text.split()
    print(words)

    first = words[0]
    second = words[1]

    if first[0] == second[0]:
        return True
    
    return False

print(animal_crackers("Taco Tuesday"))


print(animal_crackers("Crazy Kangaroo"))


def animal_crackers_quick(text): #ideally we also look to make the texts the same case before checking 
    words = text.split()
    print(words)

    if words[0][0] == words[1][0]:
        return True
    
    return False

print(animal_crackers_quick("Taco Tuesday"))


print(animal_crackers_quick("Crazy Kangaroo"))

def makes_twenty(num1,num2):

    return num1 == 20 or num2 == 20 or (num1+num2) == 20
    

print('makes twenty')
print(makes_twenty(20,30))

print(makes_twenty(2,30))

print(makes_twenty(12,8))

