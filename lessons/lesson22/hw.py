'''
total = 0
a1 = int(input('Son yozing '))
b2 = int(input('Son yozing '))
c1 = int(input('Son yozing '))
d1 = int(input('Son yozing '))
e1 = int(input('Son yozing '))
#1
i = 0
while i <= 10:
    for b in range(1,11):
        print(b)
        i +=1
#2
for i in range(1,101):
    if i % 3 == 0:
        print(i)
#3
print(f"Eng katta son {max(a1,b2,c1,d1,e1)}")
#4
print(f"Eng katta son {min(a1,b2,c1,d1,e1)}")
#5
toq_sonlar = []
juft_sonlar = []
for i in range(1,101):
    if i % 2 == 0:
        juft_sonlar.append(i)
    elif i % 2 == 1:
        toq_sonlar.append(i)
print(toq_sonlar)
print(juft_sonlar)
#6
qwer = int(input("Qaysi songcha zifrani chiqarmoqchisisz "))
for i in range(1 , qwer + 1):
    print(i)

#7
x = int(input('Sonni qiriting '))
y = int(input('Sonni qiriting '))

for i in range(x,y + 1):
    if i % 2 == 0:
        total += i
        print(f'Juftlarni summasi {total}')

#8
for i in range(x,y + 1):
    if i % 2 == 1:
        total += i
        print(f'Toqlarni summasi {total}')
'''#9
odamlar = {
    'Asilbek' : {
        'yosh' : 22,
        'weight' : 98,
        'height' : 183,
    },
    'Abdulloh' : {
        'yosh' : 8,
        'weight' : 30,
        'height' : 152,
    },
    'Abdurahmon' : {
        'yosh' : 12,
        'weight' : 49,
        'height' : 157,
    },
    'Maksim' : {
        'yosh' : 54,
        'weight' : 100,
        'height' : 189,
    }
}
asking_dict = input("ISm yozing ")
if asking_dict in odamlar:
    print(odamlar.values())
#12
s_dict = {
    'Abdurahmon' : 7,
    'Abdulloh' : 8,
    'Behruz' : 9,
    'Said' : 8,
    'Asilbek' : 10,
    'Kozim' : 11
}
for i in s_dict.keys():
    if 'A' in i[0]:
        s_dict = list(s_dict)
        s_dict.remove(i)
        print(s_dict)
#13

a, b, c = 10,50,20

result = lambda son1, son2, son3: son1 + son2 + son3
print(result(a, b, c))

a, b, c = 10,50,20

result = lambda son1, son2, son3: son1 * son2 * son3
print(result(a, b, c))