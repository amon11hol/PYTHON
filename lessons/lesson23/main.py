fayl = open('lessons\lesson23\info.txt','w+')
fayl.write('Qiziqishlarim IT,Futbol,Oyin')
fayl = open('lessons\lesson23\info.txt','a+')
fayl.write('\nOta onam ni ishi bughalter')
a = input('Narsa yozing ')
print(fayl.read())
fayl = open(a,'a')
fayl.write(a)
fayl.close()