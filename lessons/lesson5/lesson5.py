import math
#dars
#n1= input("Iki xonali son yozing ")
#num = int(n1[0])

#num2 = int(n1[1])

#print(num +num2)


#topic of lesson
x = 10 
print(x > 10 and x<20)

print(x is 10) #true
print(x == 10) #true

color = input("Svetofor rangini kiriting: ")


if color == "yashil":
    print("GOOOO")
elif color == "sariq":
    print("Wait!")
elif color == "qizil":
    print("Stop!")
else:
    print("Faqat yashil,sariq va qizil ishlating")

word = input("Soz kiriting: ")
pal = word[::-1]
if pal != word:
    print("Bu soz palindrom emas")
else:
    print("Bu palindrom")

a=int(input("Son kiriting  "))
b=int(input("Son kiriting "))
c=int(input("Son kiriting   "))


# musbat x>0
# manfiy x<0

if a > 0 and b > 0 and c > 0:
    print(a**2)
    print(b**2)
    print(c**2)
else:
    print(a**3)
    print(b**3)
    print(c**3)

a1 = int(input("Son "))
b1 = int(input("Son "))
c1 = int(input("Son "))
per = (a1 + b1 + c1)/2
s1= per((per - a1)*(per - b1)*(per - c1))
s2 = math.sqrt(s1)



