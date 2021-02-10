example = [1,2,3,4,5,6,7]

from random import shuffle #built in random shuffle function in python 

shuffle(example) #shuffle happens in place so nothing is returned

print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)

print(result)

mylist = [' ', 'O', ' ']

result = shuffle_list(mylist)

print(result)

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2 ") #input returns and always returns in the form of a swing
    
    return int(guess) #return / cast input as a integer 

#print(player_guess())

myindex = player_guess()

print(myindex)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong Guess")
        print(mylist)

#initial list

#shuffle list

#user guess

#check user guess

#initial list
mylist = [' ', 'O', ' ']

#shuffle list
mixedup_list = shuffle_list(mylist)

#user guess
guess = player_guess()

#check user guess
check_guess(mixedup_list, guess)





