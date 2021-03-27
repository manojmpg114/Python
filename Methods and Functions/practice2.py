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

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return "BUST"

print(blackjack(1,2,43))

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    
    return total

print(summer_69([1,3,5]))
