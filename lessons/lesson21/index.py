#2
mevalar ={
        'apple' : 'qizil',
        'banan' : 'sariq',
        'qivi'  : 'yashil',
        'pineapple' : 'sariq',
        'orange' : 'orange'    
}
meva = input('Mevani nomini yozing ')

def ranglar(nom):
    if nom in mevalar.keys():
        print(f"Bu {nom} {mevalar[nom]} ")
    else:
        print("Bunday meva yoq")
ranglar(meva)

#3
films = {
    'Forrest Gump' : 8.8,
    'Yulduzlari urushlar' : 8.7,
    'Batman' : 9.5,
    'Marvel:Final' : 10,
    'Orgimchaq odam' : 9.4
}
inter_film = input("Film yozing uni reytingni qorish uchun ")



