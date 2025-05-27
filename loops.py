'''
num = 76
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-100: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')
    
'''

'''
for furgle in range(1,15,3):
    print(furgle)
print("For Loop done!")
'''
'''
friends = ['John','Terry','Eric','Michael','George']
for index in range(len(friends)):
    print(friends[index])
    if friends[index] == 'Eric':
        print('Found ' + friends[index] + '!')
        continue # break would stop the loop    

print("For Loop done!")
'''
'''
#nested loops
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")
'''
'''
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
#names.extend(names1)
names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    #msg1 = f'{name.title()}! {msg}'
    msg1 = name.title() + '! ' + msg
    print(msg1)
'''
'''
print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

i = 1
for friend in friends:
    print(i, friend)
    i = i +1 # += 1
for num, friend in enumerate(friends,1):  #1 start number
    print(num, friend)
'''

'''
print('sort() and sorted()') #sort() is mutating method and sorted() is not mutating method sort not return anything sorted return new list object
print('Immutability and return values')

friends = ['John','Terry','Eric','Michael','George']
friends.sort()
print(friends)
my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'
print(my_list,'original')
print(sorted(my_list))  #print(my_list.sort())  None
print(my_list,'new')
my_list1 =sorted(my_list) #or my_dict or my_tuple or my_string
print(my_list1)
'''

'''
my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_llist, key = lambda item :item[2]))
'''


