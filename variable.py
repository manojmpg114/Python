#best practice pep8 variables are in lowercase 
#avoid syntax words like "list" and "str"

#python uses dynamic typing so you can use 2 variables of the same name to 
#represent 2 data types like an int named my_dog can also be a list named
#my_dog 

#may result in bugs but it makes it faster to develop and easy to work with

#python has a type() function to check data types of variables 

a = 5

print(a)

print(a+a)
a = a+a
print(type(a))

print(a)
a = 30.1
print(type(a))

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)