#1
n1 = int(input("Son kiriting "))
n2 = int(input("Son kiriting "))

a = (n1**2 - n2**2)
b = (n1 - n2) * (n1 - n2)

if a > b:
    print(f"Kvadratni  minusi katta {a} > {b}")
elif b > a:
    print(f"minusi kvadratini katta {a} < {b}")
else:
    print(f"Ikalasi bir xil {a} = {b}")

print("-------------------------------------------------------------")
#2
pul = 1000000
name = input("Assolomu aleykum ismingiz nima ").title()
print(f"Salom {name} nechi ildan beri ishlisiz? (2 yildan 10 yilgacha)")
y = int(input(" "))
if y < 5 and y >= 2:
    foiz = (pul / 100 * 2)
    print(1000000 + foiz,"Sizning pulingiz")

elif y >= 5 and y <=10:
    foiz2 = (pul / 100 * 5)
    print(1000000 + foiz2,"Sizning pulingiz")






