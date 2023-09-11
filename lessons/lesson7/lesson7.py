#bankomat
card_num = "0000000000000000"
card_pin = 0000

user_balans = 1000000
user_card = input("Cartizni nomerini bering ")
user_pin =  int(input("Cartizni pin-codni bering "))
if user_card == card_num and user_pin == card_pin:
    print("Xush kelsibsiz")
    print("1.Balans")
    print("2.Pul yechish")
    print("3.Kartadan kartaga")
    amal = int(input("Amalni kiriting" ))
    if amal == 1:
        print(f"Balansingiz:{user_balans}")
    elif amal == 2:
        yechish = ("Nech pul yechmohchisiz? ")
        if yechish > user_balans:
            print("Oops... Sizni mablahizda shuncha pul yo'q") 
        else:
            print(f"{yechish} pul yechtik.Xozir pulni sanapiz ",user_balans - yechish)
    elif amal == 3:
        user2_card = (input("Kimga tashamohchisizni kartasini bering: "))
        yechish3 = int(input("Nech pul tashamohchisiz? "))
        if yechish3 > user_balans:
            print("Oops... Sizni mablahizda shuncha pul yo'q")
        else:
            
            print(f"{yechish3} pul yechtik.Xozir pulni tashapiz.Sizni mablahizda ",user_balans - yechish3 )