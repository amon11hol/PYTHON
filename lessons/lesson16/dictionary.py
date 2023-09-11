odam= {'name': 'Asilbek',
        'age': 22,
        'weight' : 98,
        'cars' : ['Matiz','Lacetti','BYd']
}
print(odam.keys()) # он показывает что находиться в коючах который в словаре
print(odam.values()) # это то что находиться в ключе
print(odam['weight']) # он выводит ключ
# change
odam['age'] = 23 # изменение 1 способ
print(odam)
odam.update(age=25,cars='Malibu') # изменение 2 способ
print(odam)

# add
odam['height'] = 180
print(odam)
odam.update(familiya = 'Mirolimov')
# remove

odam.pop('age')
print(odam)
odam.popitem()
print(odam)
del odam['cars']
print(odam)
# Loop
for i in odam.items(): # он берёт и keys и value
    print(i)
for i,j in odam.items():
    print(f'{i} degan keyda {j} value bor')


phone = {
    'phone1': {
        'nomi' : 'Iphone',
        'pamyat' : '126 gb',
        'rangi' : 'qora'},
    'phone2' : {
        'nomi' : 'Samsung',
        'pamyat' : '256gb',
        'rangi' : 'oq'},
    'phone3' : {
        'nomi': 'Xiaomi',
        'pamyat': '64gb',
        'rangi':'qora'
        },
    'phone4' : {
        'nomi' : 'LG',
        'Pamyat' : '32Gb',
        'rangi' : 'qizil'
    },
    'phone5' : {
        'nomi' : 'Honor',
        'Pamyat' : '1tb',
        'rangi' : 'aqua'
}}
"phone4 ni rangi qizil"
for i,j in phone.items():
    print(f"{i} ni rangi {j['rangi']}")
print(f'Phone4 ni ')