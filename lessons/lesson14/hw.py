#1
numbers = (15, 30, 10, 5, 40, 20)

maxnum = max(numbers)
minnum = min(numbers)

print(maxnum)
print(minnum)
#2
my_tuple = (1, "hello", 3.14, False)

my_tuple = list(my_tuple)
my_tuple[1] = 'world'
my_tuple = tuple(my_tuple)
print(my_tuple)
#3
# Tuple пишеться в круглых скобках то есть () и его невозможно изменять 
# если только не изменить его тип и команды у него другие
# Set пишеться как {}.Set  не выводит елементы которые одиннаковые он просто 
# их удаляет и ещё TSet работает на принципе рандома.
#4

myset = {True, 'mars', 1, 'bir narsa', 2, 3, "salom"}

setlist = list(myset)
for i in setlist:
    if str(i).isdigit():
        print(i)
#5
'''
5. Hafta kunlarini malumot sifatida saqlang va odamdan bitta
input sorang, odam inputda oziga yoqgan hafta kunini kiritadi,
sizning vazifangiz usha hafta kunini toq kun yoki juft
kun ekanligini ayting.'''
#          0            1           2           3             4         5           6          
week = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
c = input("Bitta hafta kuni nomini yozing: ").title()

if week.index(c) % 2 == 1:
    print("Bu hafta kuni juft")
else:
    print("Bu hafta kuni toq")


#6
'''
6. Odamlarni ismlarini saqlaydigan dastur yozing. Hech qaysi ism ikki 
martta takrorlanmasligi kerak. Odamdan ism kiritishini sorang. Agar u ism bor bolsa bunaqa ism bor 
desin agar yoq bolsa qoshib qoysin
'''

names = {'Abdurahmon','Jasur','Bexruz','Abdulloh','Asilbek','Saidazim'}
while True:
    input_name = input("Ismingizni kiriting: ").title()
    if input_name in names:
        print("В списке есть такое имя")
    else:
        names.add(input_name)
        print("Имя успешно  добавлено!!!")
    conbr = input("Вы хотите добавить имя?(Yes or No) или можете посмотресть список(Show) ").title()
    if conbr == 'Yes':
        continue
    elif conbr == 'No':
        break
    elif conbr == "Show":
        for i in names:
            print(i)
    else:
        print("Errooooooooooooor")
        break