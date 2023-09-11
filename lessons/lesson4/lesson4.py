#a,e,o,i,u,o'

word = input("Soz yozing man unli harf topaman ").lower()
a = word.count("a")
e = word.count("e")
o = word.count("o")
i = word.count("i")
u = word.count("u")
print(f"""Sizning sozizda 
{a}-ta a 
{e}-ta e 
{o}-ta o 
{i}-ta i 
{u}-ta u""")                   



text = "Man talabaman"
print(text.replace("man"," "))
print(text[4:9])
#(text[start : end : step])
#text[start: ] если в в енде нет ничего то он просто добавляет до конца слова

text1 = "Chegarachilarimizdagilardanmisiz"
print(text1[0:7])
print(text1[17:24])
print(text1[27:])

sonlar = '123456789'
print(sonlar[::2])#какую цифру вы пишите если напишите 2 то он отступает 1 шаг потом 2 пишет
print(sonlar[::-1]) # делает наоборот
