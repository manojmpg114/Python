def has_33(numlist):

    for i in range(0, len(numlist)-1):
        if numlist[i] == 3 and numlist[i+1] == 3:
            return True
    return False  

mylist = [1,3,4,5,3,2,3,5,2]

print(has_33(mylist))

#we could accomplish the same thing using another if statement that is sleeker but less readable


def has_33(numlist):

    for i in range(0, len(numlist)-1):
        if numlist[i:i+2] == [3,3]:
            return True
    return False  

mylist = [1,3,4,5,3,2,3,3,5,2]

print(has_33(mylist))

def paperdoll(word):
    result = ''
    for char in word:
        result += char*3
    
    return result

print(paperdoll("yes"))