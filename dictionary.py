'''
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['budget'] = 250000
print(movie)

movie['cast'].append('Terry')
print(movie)

movie['cast'].remove('Eric')
print(movie)

del movie['cast']
print(movie)   

#movie.clear()
print(movie)

print(movie.keys())

print(movie.values())

print(movie.items())  #tuple

for key, value in movie.items():
    print(key, value)
'''

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
#membership test
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here!')

people = {}
people1 = {}
people2 = {}
#method 1 update
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(sorted(people.items()))
#method 2 comprehension
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(sorted(people1.items()))
#method 3 unpacking 3.5 later
people2 = {**python,**holy_grail,**life_of_brian}
print(sorted(people2.items()))
print('The sum of the ages: ', sum(people.values()))






