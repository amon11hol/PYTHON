# 1. ichida 10 ta son bor list yarating va ularni faqat toqlarini print qiling
# 2. ichida 10 ta son bor list yarating va ularni faqat juftlarini print qiling
# 3. ichida 10 ta son bor list yarating va ularni teskari tartibda print qiling
# 4. bo'sh list yarating, range orqali 1 dan 100 gacha bo'lgan sonlarni ichidan 3 ga va 5 ga bo'linadiganlarini shu listga qo'shing
# 5. guruhdagi hamma bolani ismi bor bo'lgan list yarating, u listni uzunligini toping va o'zingiz yoqtirmagan ismingizni uni ichidan olib tashlang
# 6. guruhdagi bolalar listiga o'zingiz yoqtirgan biror qizni ismini listni oxiriga qo'shing
# 7. guruhdagi bolalar listiga o'zingiz yoqtirgan biror qizni ismini o'zingizni ismingizdan oldingi indexga qo'shing
'''
my_list = [6,2,1,6,9,10,27,35,13,75]
for i in my_list:
#значит оно чётное число
   if i % 2 == 0:
       print(i)
print(my_list[::-1]) 
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
number = []   
number.append(i)

clas = ['Misha','Masha','Sasha','Sanya','Senya','Jenya']
print(len(clas)


clas.pop(5)
print(clas)
'''
lit = ['Banan','Olma','Shafroli','olcha','oriq','tarvus','Qovun','Limon','klupnay']
lit.remove('olcha')  
print(lit)
new =[]
for i in lit:
    if i.islower():
         new.append(i.upper())
    else:
         new.append(i.lower())
print(new)