#dictionaries are unordered and can not be sorted key value pairs 
#created with curly braces { } and combined via :

#lists can be retrieved by location 

my_dict = {'key1':'value1', 'key2':'value2'}

print(my_dict)

print(my_dict['key1'])

price_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}

print(price_lookup['apple'])

d = {'k1':123, 'k2':[0,1,2], 'k3': {'insidekey': 100}}

print(d['k2'])

print(d['k3'])

print(d['k3']['insidekey'])

print(d['k2'][2])

d = {'key1': ['a', 'b', 'c']}

print(d)

print(d['key1'][2].upper()) #one liner to reach the character 'c' and make it to uppercase from teh dictionary 

#adding to dictionaries

d = {'k1':100, 'k2':200}
print(d)

d['k3'] = 300 #adding the k3 key value pair to the d dictionary

print(d)

#same technique can be used to overwrite values in the dictionary
d['k1'] = 'New Value'

print(d)

d = {'k1':100, 'k2':200, 'k3':300}

print(d)

print(d.keys())

print(d.values())

print(d.items())

#results appear in paranthesis making them tuples 
#dictionaries are mappings and do not retain order, if i want dictionary capabiltiies and ordering should look into orderreddict object