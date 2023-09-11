# Uy ishi (file handling mavzusi uchun)

# 1. Nomiga ism yozilgan fayl yarating va ichidagi ma'lumotlarni 'r' orqali o'qib ekran chiqaring
# 2. info.txt nomli fayl yarating va ichiga o'z haqingizda 10 qator ma'lumotlarni 'w' orqali yozing
# 3. info.txt nomli faylga o'z haqingizdagi qiziqishlaringizni 'a' orqali qo'shing
# 4. info.txt nomli faylidagi barcha a harflarini A ga o'zgartiring
# 5. info.txt nomli fayl ichida necha qator va nechta so'zdan iborat ekanligini toping

#1
open2 = open('lessons\lesson23\hw.py','r')
open2.read()
open2.close()

#2
info = open('lessons\lesson23\info.txt','w')
info = open('lessons\lesson23\info.txt','w')
info = open('lessons\lesson23\info.txt','w')
info.write('Man 7 sinf')
info.write('\nMaktabda oqiyman')
info.write('\nMars')
info.write('\nIt ga boraman')
info.write('\nPython organaman')
info = open('lessons\lesson23\info.txt','r')
print(info.read())
info.close()


info = open('lessons\lesson23\info.txt','r')
print(info.read())



#3
info2 = open('lessons\lesson23\info.txt','a')
info2.write('\nNimadir')
info2.close()

#4
op = open('lessons\lesson23\info.txt','r')
#for i in op:
 #   if 
    