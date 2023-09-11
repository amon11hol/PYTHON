# lambda function
# lambda function - bu funksiya nomi yo'q, bir qatorlik funksiya

# avzalliklari:
# 1. bir qatorlik funksiya

# 2. return qilish shart emas

# 3. parametr sifatida *args va **kwargs qabul qilishi mumkin

# 4. lambda funksiyalarda if, else, elif operatorlari ishlatilmaydi

# 5. lambda funksiyalarda list comprehension ishlatilishi mumkin
#    list comprehension - bu listni qisqacha yaratish usuli. Misol uchun: mylist = [i for i in range(10)]


old_list = []
for i in range(1, 101):
    old_list.append(i)
print(old_list)
# тоже самое как
new_list = [i for i in range(1, 101)]
print(new_list)

a, *b , c = 10,50,20,13,61430,111,0
# а б и с он автомачитески распределяет цисла под переменные
print(a, b, c)

a, b, c = 10,50,20
# lambda args: code of function
result = lambda son1, son2, son3: son1 * son2 * son3
print(result(a, b, c))

name = 'Isfandiyor' 
age = 10
doc = lambda a, b: print(f"{a}ni yoshi {b}")
doc(name,age)