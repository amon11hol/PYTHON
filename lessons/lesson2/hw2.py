print("Welcome to Coffe Shop!!!")
Amer = 8000
Latte = 9000
Kapuch = 8500
print("We have Americano, Latte,Kapuchino")
print("press 1 for Americano(8000som)")
print("press 2 for Latte(9000som)")
print("press 3 for Kapuchino(8500som)")

shtuk = int(input("How many cup of coffee do you want?  "))

choice = int(input("What cofe do you want(Americano, Latte,Kapuchino)?  "))
if choice == 1:
    print("You should pay",Amer,"som for 1 cup")

    narx_A = shtuk * Amer
    print("You should pay: ",narx_A,"som")
elif choice == 2:
    print("You should pay",Latte,"som for 1 cup")
    narx_L = shtuk * Latte
    print("You should pay: ",narx_L,"som")
else:
    print("You should pay",Kapuch,"som for 1 cup")
    narx_k = shtuk * Kapuch
    print("You should pay: ",narx_k,"som")


name = input("Ismingiz nima? ").title()
print(f"Assolomu aleykum, {name} Bizani kofega xush kelibsiz!")

kofe1 = "Americano"
kofe2 = "Latte"
kofe3 = "Kapuchino"

narx1 = 10000
narx2 = 15000
narx3 = 20000

print(f"""Kofe nomlari va narxi:
      {kofe1} - {narx1} som
      {kofe2} - {narx2} som
      {kofe3} - {narx3} som""")

zakaz = input("Buyurtmani yozing: ").title()

if zakaz == kofe1:
    print(f"{zakaz}ni narxi {narx1}som")
elif zakaz == kofe2:
    print(f"{zakaz}ni narxi {narx2}som")
else:
    print(f"{zakaz}ni narxi {narx3}som")