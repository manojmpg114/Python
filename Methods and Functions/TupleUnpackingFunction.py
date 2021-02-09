stock_prices = [('AAPL', 200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)


for ticker,price in stock_prices:
    print(ticker)
    print(price + (0.1*price))

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass




    #return
    return(employee_of_month, current_max)

name,hours = employee_check(work_hours)
print(employee_check(work_hours))

print(name)
print(hours)

#when working with someone elses code we should let the result / return be assigned to a single item and explore that item before breaking it down to confirm the amount of returns

