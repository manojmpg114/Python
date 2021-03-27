def spy_game(nums):
    zeros = 0
    result = False
    if 0 not in nums or 7 not in nums:
        return False

    for num in nums:
        if num == 0:
            zeros+=1

        if num == 7:
            if zeros >= 2:
                return True
            elif zeros < 2:
                zeros = 0
                
    return result    

    #keep a 0 counter 
    #if a 7 appears before 2 0's reset 0's counter
    #when counter is 2 0's at the time of finding a 7 mark 
    #maybe have a boolean to determine result and return 


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#same function but with better code / shorter code 

def spy_game2(nums): 
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([7,0,7,0,7,0]))

print(spy_game2([7,0,7,0,7,0]))

def count_primes(num): #very math orientated 
    #check for 0 or 1 input

    if num < 2:
        return 0
    # 2 or greater
    primes = [2]
    
    #counter going up to the input num
    x = 3

    #x is going through every number up to input num
    while x <= num:
        #check if x is prime
        #for y in range (3,x,2):
        for y in primes:
            if x%y == 0:
                x += 2 # we skip by 2's so we can avoid all even numbers
                #prime numbers are not even
                break
        else: # FOR ELSE STATEMENT -- unique to python
            primes.append(x)
            x += 2
    print(primes)
    len(primes)
    print(len(primes))

count_primes(100)