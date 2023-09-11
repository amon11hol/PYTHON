
#O'tiladigan mavzular:

#- Funksiya mavzusini takrorlash
#- Argument va parametrlar


# Masalalar:

#1. Ikkita parametr qabul qiladigan funksiya yozing ikka parametr ham int bolsin
#   u funksiya usha ikkala sonni 2-darajaga oshirib bir birga qoshib qayytarib bersin
a,b = 5,6
sonlar = lambda num1,num2 :num1 ** 2 + num2 ** 2
print(f"Javob: {sonlar(a,b)}") 

    

#2. Ikkita parametr qabul qiladigan funksiya yozing. Birinchisi int ikkinchisi str bolsin
#   u funksiya str ni ichidagi unli harflar sonini topib 1-parametrga kopaytirib natijani
#   qaytarish
def kopaytirsh():
    a = 6
    b = 0
    savol = input("Soz yozing ").lower()
    soz = 'aeuoi'
    for i in savol:
        if i in soz:
         b += 1
    print(a*b)
kopaytirsh()
#3. 3 ta parametr qabul qiladigan funksiya yozing. Uchchalasi ham int bolsin.
#   U funksiya 3 ta sondan eng kattasini qaytarib bersin.
a,b,c = 8,3,2
sonlar_2 = lambda num1,num2,num3 : max(num1,num2,num3)
print(sonlar_2(a,b,c))
#4. Ikkita parametr qabul qiladigan funksiya yozing. 1-int 2-str bolsin.
#   str ni ichidagi undosh harflar sonidan unli harflar sonini ayiring va
#   1-parametrga qoshib qaytarib bering.
a = 8
b = 'Abdurahmon'
total = 0

soz = 'aeuoi'
for i in b:
    if i in soz:
        total += 1
undosh = len(b) - total
function = lambda num,string : undosh - a
print(function(a,b))
#5. 5 ta parametr qabul qiladigan funksiya yozing. Barchasi int bo'lsin.
#   Ularni ichidan eng katta va eng kichkinasini list ichiga solib qaytarib bering,

a,b,c,d,e = 1,2,3,4,5
sonlar_3= lambda num1,num2,num3,num4,num5 : max(num1,num2,num3,num4,num5)
sonlar_3= lambda num1,num2,num3,num4,num5 : min(num1,num2,num3,num4,num5)
print(sonlar_2(a,b,c,d,e))
print(sonlar_3(a,b,c,d,e))
a = []
a.append()