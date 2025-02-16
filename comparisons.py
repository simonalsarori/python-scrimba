'''
a = [3,7,42]
b = a
print(a == b)
print(a is b) # a and b point to the same memory location identical 
print(id(a), id(b))

c = [3,7,42]
print(a == c)
print(a is c) # a and c point to different memory locations identity
'''
'''
a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity
'''

'''
print(bool(0))
print(bool(1))
print(bool(2))
print(bool(-1))
print(bool(None))
print(bool(''))
print(bool(' '))
print(bool([]))
print(bool({}))
print(bool(False))
'''

'''
is_raining = False
is_cold = True
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
    
else:
    print("Shirt is fine!")
    '''
    
mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')