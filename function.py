'''
def greeting(name, age=28, color = 'red'): #default values parameters
    #Greets user with 'name' from 'input box' and 'age' next year, if available, default age is used
    # also includes favorite color
    print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter favorite color: ')
greeting(name, int(age), color) #positional notation arguments
# greeting(age=27, name="brian",color="Blue") named notation
'''

# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 
'''
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax

price = value_added_tax(100)    
print(price, type(price))
'''

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax   # return amount, tax, total_amount 'tuple' return [amount, tax, total_amount] list  return {amount, tax, total_amount} set

price = value_added_tax(100)    
print(price, type(price))