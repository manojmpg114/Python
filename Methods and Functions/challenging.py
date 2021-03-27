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