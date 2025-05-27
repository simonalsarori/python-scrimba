msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title())

msg='Welcome to Python 101: Strings'
print(msg.find('Python'))
print(msg.replace('Python','C'))
print('Python' in msg) # or not in


name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)

name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')