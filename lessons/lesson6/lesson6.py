"""
1. number = "112233" ushbu string formatdagi raqamni ikkichi va oxirgi o'rindagi raqamlarini yig'indisini toping
2. Odamdan string formatda text so'rang agar usha so'zni ichida ikkita unli harf bor bo'lsa "Hello" chiqsin
    agar udan oz bo'lsa "Hayr" chiqsin.
3. for orqali 1-200 gacha 7 va 9 va 11 ga bo'linadigan sonlarni print qiling
4. for va range orqali 1-100 gacha 3 va 5 ga bo'linadigan sonlar nechta ekanligini toping
"""
#1
num = '123233'
a = int(num[1])
b = int(num[5])
print(a + b)
#2
name = input("Ismingiz nima? ").lower()
c = 0
for i in name:
    if i == 'a' or 'e' or 'i' or 'o':
        c += 1
if c >= 2:
    print("Hello")
else:
    print("Hayr")


#for i in range(1, 11):
#    if i % 2 == 0:
#       print(i)
#3
for i in range(1,2000):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print(i)



