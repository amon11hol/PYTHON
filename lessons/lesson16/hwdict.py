"""
1. O'yinchilarni achkolarini hisoblaydigan
 dict yarating. Key ularni ismi bo'ladi value nechi
achkosi borligi.
odamdan 10 martta input sifatida ismini
 soraysiz va usha ismli o'yinchini ismi bilan 
 ochkosini print qilib chiqarib berasiz

"""
players = {
    'Abdurahmon' : 5,
    'Ali' : 6,
    'Behruz' : 7,
    'Asilbek' : 8,
    'Abdulaziz' : 9,
    'Aziz' : 20,
}

q = input("Ism yozing ").title()
print(f"{q}da {players[q]} ochko bor")
    



"""
2. Oila a'zolarini ismlarnikey qilib ular haqida quyidagi ma'lumotni dict qilib value qilib saqlang. Misol uchun:


family = {
    "Ravshan": {
        "bo'y": 175,
        "ism": "Ravshan",
        "familiya": "Oxunov",
        "yosh": 44
    },
    "Lola": {
        "bo'y": 165,
        "ism": "Lola",
        "familiya": "Oxunova",
        "yosh": 41
    }
}
"""

