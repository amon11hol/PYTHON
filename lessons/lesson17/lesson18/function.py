# function
"""Functions
Funksiya bu biror bir amalni bajaruvchi kod bloki.

Funksiyalarni yaratish uchun def kalit so'zi va funksiya nomi yoziladi.
def funksiya_nomi():
    funksiya_tanasi

Funksiyalarni chaqirish uchun funksiya nomi yoziladi va () qo'yiladi.

funksiya_nomi()

"""
# Функция в python - объект, принимающий аргументы и возвращающий 
# значение. Обычно функция определяется
# с помощью инструкции def. Инструкция 
# return говорит, что нужно вернуть значение. В 
# нашем случае функция возвращает сумму x и y.
'''
Как писать функции:
def my_func(fname):
    print(fname + " Salam")

my_func()
'''

def salom():
    print("Hello, Welcome!")

salom()

a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))
c = int(input("Son kiriting: "))
def maxnum():
    if a > b and a > c:
        print(f"{a} eng katta son")
    elif b > a and b > c:
        print(f"{b} eng katta son")
    elif c > a and c > b:
        print(f"{c} eng katta son")
    else:
        print(f"{a},{b},{c} teng")
maxnum() # тоже самое как max(a,b,c)

# 2. Ro'yxatdagi sonlarni yig'indisini topadigan funksiya yozing.
# 3. Ro'yxatdagi sonlarni ko'paytmasini topadigan funksiya yozing.
# 4. Matnni teskari tartibda chiqaruvchi funksiya yozing.
# 5. x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# 6. Biror son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
#2
list = [4,6]
def summa():
    total = 0
    for i in list:
        total += i
        print(f" Summa {total}")
summa()
#3
total2 = 1
def mult():
    total = 1
    for i in list:
        total *= i
        print(f" Qopytmasi {total}")
mult()

#4
def text():
    tex = input("Text yozing ")
    print(tex[::-1])
text()

#5
def daraja():
    x = int(input("Son yozing "))
    y = int(input("Darajani yozing "))
    print(x**y)
daraja()

#6
def son():
    num = int(input("Son yozing "))
    if num % 2 == 0:
        print(f"{num} Juft son")
    else:
        print(f"{num} Toq son")
son()

