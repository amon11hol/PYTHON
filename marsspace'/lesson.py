
new_list = []
new_list.append(4)
new_list.append(5)
new_list.append(3)
new_list.append(1)
new_list.append(2)
total = 0

print(new_list)
for i in new_list:
    total += i
    print(f"Summa {i}")

names_list = ['Sasha', 'MAsha','Dasha','Dima','Sam']
print(names_list[2])

color_list = ['Красный',"Желтый","Синий","Розовый","Фиолетывый"]
color_list.extend(2,'Оранжывый')
print(color_list)
