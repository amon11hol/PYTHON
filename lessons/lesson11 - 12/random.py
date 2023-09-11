import random
my_list = []
#random
i = 0
while i < 10:
    my_list.append(random.randint(1,100))
    i+=1
print(my_list)

#random choice
nl = [93,19,78,54,76,78,54]
son = random.choice(nl)
print(son)