# Lambda functions are anonymous functions defined with the lambda keyword.
# They can take any number of arguments but only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
# Example: A lambda function that adds two numbers
#function without name it is small function that can be used once

def square(x):
    return x*x

#name = lambda parameter(s): expression

double_mult = lambda x,y: 2*x*y
print(double_mult(2,3))

def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()
name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
def name_and_alias2(name,alias):return name.strip().title() + ':' + alias.strip().title()

print(name_and_alias2(' john  ClEEse  ','HECKLER'))
print(name_and_alias(' john  ClEEse  ','HECKLER'))

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
def sort_names(name):
    return name.split(' ')
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)
monty_python.sort(key= sort_names)
print(monty_python)

####################################
def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walkin_cost(2))
print(premium_cost(2))
print(price_calc(1,25)(2))

print((lambda a,b,c: a+b+c)(2,3,4)) 
print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3))
print((lambda *args: sum(args))(2,3,4,50))

#example of lambda function 
print('Lambdas Exercise')

#def f(x): return x + 5
f = lambda x: x + 5#insert equivalent lambda here
print(f(2))


print('Lambdas Exercise')


def strip_spaces(str):
   return ''.join(str.split(' '))
#write equivalent lambda and insert Lambda here
strip_spaces1 = lambda str:''.join(str.split(' '))  
print(strip_spaces1('Monty Pythons Flying Circus')) 

print('Lambdas Exercise')

def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
#write lambda below 
join_list_no_duplicates1 = lambda list_a,list_b:list(set(list_a + list_b))
print(join_list_no_duplicates1(list_a,list_b))

print('Lambdas Exercise')

#Complete the function so it returns a function
def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c
f = create_quad_func(2,4,6)
g = create_quad_func(1,2,3)
print(f(2))
print(g(2))

print('Lambdas Exercise')


signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
#write sorting by integer
print(sorted(signups,key = lambda id:int(id[3:]))) # Integer sort

print('Lambdas Exercise')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
player_list.sort(key = lambda playyer: playyer.score, reverse = True)
print([player.name for player in player_list])