#print(10 > 8)
#print(10 < 11)

# num1 = int(input("Введите 1 число "))
# num2 = int(input("Введите 2 число "))

# print(num1 > num2) #больше
# print(num1 < num2) #меньше
# print(num1 >= num2) #больше или равно
# print(num1 <= num2) #меньше или равно
# print(num1 == num2) #равно
# print(num1 != num2) #не равно

#zadaniye
print("Assolomu aleykum siz kalkulator ga keldiz")
s1 = int(input("1 sonni yozing "))
s2 = int(input("2 sonni yozing "))
op = input("Iltimos deystviani yozing (+,-,*,/,//,%)")
if op == '+':
    print("Sizning javobingiz",s1 + s2)
elif op == "-":
    print("Sizning javobingiz",s1 - s2)
elif op == "*":
    print("Sizning javobingiz",s1 * s2)
elif op == '/':
    print("Sizning javobingiz",s1 / s2)
elif op == '//':
    print("Sizning javobingiz",s1 // s2)
else:
    print("Sizning javobingiz",s1 % s2)


