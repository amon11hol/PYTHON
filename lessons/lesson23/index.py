# fayldan oq'ish uchun: 'r

#fayl = open('lessons\lesson23\mars2.txt','r') #mode = read
#print(fayl.read())
#fayl.close()

#yangi = open('lessons\lesson23\mars2.txt', 'r')
#print(yangi.readline())
#print(yangi.readline())
#print(yangi.readline())
#yangi.close()
#
#fayl2 = open('lessons\lesson23\mars2.txt' , 'r')
#for line in fayl:
   # print(fayl2.readline())

#fayl3 = open('lessons\lesson23\mars2.txt','r')
# print(fayl3.readlines) # list ga chiqarberadi
#faylga yozish uchun: 'w' - write() , agar fayl bor bolsa ochirib yangi yozadi

fayl_r = open('lessons\lesson23\mars2.txt','w')
fayl_r.write('Kamron etiborsiz bola darsga qaramapti')
fayl_r.write('\nqolini qirsilatib otiribdi')
fayl_r.close

#faylga yozish uchun: 'a' - append()  - agar bor bolsa yonida yozib ketadi, yoq bomasa yangi text fayl ochib yozib ketdi

fayl = open('lessons\lesson23\mars2.txt','r')
fayl.write('\nYangi Gap yozdim') 
fayl.close() 
print(type(fayl.read()))
'''

ser = input("Narsa yoz ")
fayl.
'''