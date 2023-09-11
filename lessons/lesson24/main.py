with open('lessons\lesson24\info.txt','r') as file:
    print(file.read())
with open('lessons\lesson24\info.txt','w') as file:
    file.write("Yangi yozildi\n")
with open('lessons\lesson24\info.txt','a') as file:
    file.write("Yangi qoshildi\n")
with open('lessons\lesson24\info.txt','x') as file:
    file.write('Yangi yaratildi\n')
with open('lessons\lesson24\info.txt','r+') as file:
    print(file.read())
    file.write("Yangi yozildi\n")
with open('lessons\lesson24\info.txt','w+') as file:
    file.write('Yangi yozildi\n')
    print(file)
    