
#list
friends = ['John','Michael','Terry','Eric','Graham']
#print(friends)
#print(friends[1],friends[-1])
#print(len(friends))
#print(friends.index('Eric'))

#friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
#print(friends)
#friends.sort()
#print(friends)
#friends.sort(reverse=True)
#print(friends)
#friends.reverse() 
#print(friends)
#print(min(cars))
#print(max(cars))
#print(sum(cars))

#add and remove
#friends.append('TerryG') #add to end
#friends.insert(1,'TerryG') #add midlle
#friends[2]='TerryG'
#friends.extend(cars) #add to list
#friends.remove('Terry')
#friends.pop()
#friends.clear() #empty
#del friends #delete
#del friends[2]
#print(friends)

#copy
#new_friends = friends[:]
#new_friends = friends.copy()
#new_friends = list(friends)
#print(new_friends)

#sales_w1 = [7,3,42,19,15,35,9]
#sales_w2 = [12,4,26,10,7,28]
#sales = []
#new_day = input('Enter #of lemonades for new day: ')
#sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
#sales = sales_w1 + sales_w2
#sales.sort()
#print(sales)
#worst_day_prof = sales[0] * 1.5
#best_day_prof = sales[-1] * 1.5
#or worst_day_prof = min(sales) * 1.5
#or best_day_prof = max(sales) * 1.5
#print(f'Worst day profit:$ {worst_day_prof}')
#print(f'Best day profit:$ {best_day_prof}')
#print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

#msg ='Welcome to Python 101: Split and Join'
#csv = 'Eric,John,Michael,Terry,Graham'
#friends_list = ['Eric','John','Michael','Terry','Graham']
#print(list(msg))
#print(msg.split())
#print(msg.split(' '))
#print(msg.split(','), type(msg.split(' ')))
#print(csv.split(','))
#print(str(friends_list))
#print('-'.join(friends_list))
#print('-'.join(friends_list+friends_list))
#print(''.join(friends_list))
#print(''.join(msg.split()))
#print(''.join(friends_list))
#print(''.join(msg.split()))

#csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
#friends_list = ['Exercise: fill me with names']
#print(friends_list)
#print('replace', csv.replace(';',',').replace(':',',').split(',')) 

#Tuples - faster Lists you can't change it is immutable and string secret can not use sum method like append remove pop 
#friends_tuple = ('John','Michael','Terry','Eric','Graham')
#print(friends_tuple)
#print(friends_tuple[2])

#Sets - blazingly fast unordered Lists remove duplicate     
#friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
#my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
#print(friends_set)
#print(friends_set.intersection(my_friends_set))
#print(friends_set.difference(my_friends_set))
#print(friends_set.union(my_friends_set)) # with on dupplicate
#Sets - blazingly fast unordered Lists 
#empty Lists
#empty_list = []
#empyt_list = list()

#empty Tuple
#empty_tuple = ()
#empty_tuple = tuple()

#empty Set
#empty_set = {} # this is wrong, this is a dictionary
#empty_set = set()

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print(friends.union(my_friends))
print(friends.intersection(my_friends))
print(friends.difference(my_friends))

'''
#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates


friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print('Eric' in friends and 'John' in friends)

print(friends.union(my_friends))
print(friends | my_friends)

print(friends.intersection(my_friends))
print(friends & my_friends)

print(friends.difference(my_friends))
print(friends - my_friends)

print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)

cars_no_dupl =set(cars)
print(cars_no_dupl) 
print(friends_set.intersection(my_friends_set))

'''
