def openw():
    with open('lessons\lesson24\index.txt','a') as file:
        ask = input('Ismingiz nima ').title()+'\n'
        ask2 = input("Yoshiz nechi ")+'\n'
        ask3 = input('Qaysi qiz yoqtirasiz ').title()+'\n'
        file.write(f"Ism: {ask}")
        file.write(f"Yosh: {ask2}")
        file.write(f"Yoqqan qiz: {ask3}")
openw()

import os

print(os.getcwd())
