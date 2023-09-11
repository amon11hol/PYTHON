

# list va dict metodlarini def qilib yaratish
reverse_ist = [1,2,3,4]
# 1. listni parametr qilib olib, listni o'zini teskari tartibda qaytaruvchi funksiya yarating


# 2. Lis uchun element qo'shish, o'chirish, tahrirlash funksiyalarini yarating. Ularning nomlari add_element, remove_element, edit_element deb nomlangan bo'lsin.
#    Buning uchun listni o'zini va qo'shiladigan o'chiriladigan yoki tahrirlanadigan elementni parametr qilib oling.
#    Misol uchun def add_element(mylist, element):, def remove_element(mylist, element):, def edit_element(mylist, element, new_element): bo'lsin.
def add_element(sonlar: list, yangi_son):
    return sonlar.append(yangi_son)
juftlar = [4,6,8]
add_element(juftlar,111111111111)
print(juftlar)

def remove_element(sonlar: list, remove_son):
    return sonlar.remove(remove_son)
juftlar = [4,6,8]
remove_element(juftlar,4)
print(juftlar)

def edit_element(sonlar: list, edit_son):
    return sonlar.extend(edit_son)
juftlar = [4,6,8]
edit_element(juftlar,'hi')
print(juftlar)
# 1. Dictni parametr qilib olib, "dict[key] ning qiymati - dict[value]" ko'rinishida qaytaruvchi funksiya yarating
dictionary = {
    '5' : 7,
    '3' : 9,

}

# 2. Davlat nomi-poytaxt-aholi soni lug'atini yarating. Keyin funksiya yaratasiz u funksiyaga foydalanuvchi input orqali davlat nomini kiritganda
#    shu davlat haqida ma'lumotlarini chiqarib bersin. Misol uchun "O'zbekiston poytaxti Toshkent shahri, aholisi 34 000 000" bo'lsin.

s_dictionary = {
    'Uzbekiston' : 'poytaxti Tashkent',
    'USA' : 'poytaxti Vashington',
    'China' : 'Eng kop odam mamlakat',
}
input_p = input("Mamalakat yoznig ")
def mamlakat():
    if input_p in s_dictionary.keys():
        print(f"{input_p}ni {s_dictionary[input_p]}")
    else:
        print('Mamlakat yoq')
mamlakat()