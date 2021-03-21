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

def old_macdonald(text): #using upper
    firstLetter = text[0]
    inbetween = text[1:3]
    fourthletter = text[3]
    rest = text[3:]

    return firstLetter.upper() + inbetween + fourthletter.upper() + rest

print(old_macdonald("testercase"))

def old_macdonald(text): #using capitalize we can do the same as with upper but with less slices 
    part1 = text[:3]
    part2 = text[3:]

    return part1.capitalize() + part2.capitalize()

print(old_macdonald("tacotuesday"))

def reverse_sentence(sentence):
    wordlist = sentence.split()
    reversed_wordlist = wordlist[::-1]
    return ' '.join(reversed_wordlist)

print(reverse_sentence("taco tuesday with the homies"))

def almost_there(num):
    if (abs(100-num) <= 10) or (abs(200-num) <= 10):
        return True
    else:
        return False

print(almost_there(110))


