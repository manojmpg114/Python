def myfunc(*args):
    print(args)



myfunc(1,2,3,4,5,6)

# *args or really * anything alows us to use multiple parameters without defining each position, this would show a tuple if the * paramenters name is printed

# by convention we use args but args can be called anything for example like *spam 

# so again *args is an arbitrary number of arguments 

#if we do **kwargs we build a dictionary of key-value pairs in our arguments 

def myfunc(**kwargs):
    print(kwargs) #prints out a dictionary vs a tuple 
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")

myfunc(fruit = 'Apple', veggie = 'beans')

# *args and **kwargs can also go hand in hand in a single function

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)

    print("I would like {} {}".format(args[0], kwargs["food"]))

myfunc(10,20,30,40,50,fruit = "Apples", food = "Tacos")

