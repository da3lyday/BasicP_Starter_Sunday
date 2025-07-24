print("Fat Usagi Monster(20 HP)")
x = str(input("Choose your path 1.Fight 2.Run : "))
if x == "Fight" :
    y = int(input("Choose your weapon 1.Claymore(-7 HP) 2.Pocket knife(-2 HP) 3. Whip(-3 HP) : "))
    a = 7
    b = 2
    c = 3
    if y == 1 : 
            z = int(input("How many time you want to hit the monster: "))
            i =  0
            while i < z :
                i = i + 1
                print(f"You have hitted THE monster {i} time(s)")
            H = 20 - (7 * z)  # H จะเป็นค่าที่คำนวณได้
            print("The monster HP: ", H)
            if H == 0 :
                 print("YOU WIN")
            elif H < 0 :
                 print("BRO YOU CHOPPED IT TOT")
            else :
                 print("NEXT ROUND")
    if y == 2 : 
            z = int(input("How many time you want to hit the monster: "))
            i =  0
            while i < z :
                i = i + 1
                print(f"You have hitted THE monster {i} time(s)")
            H = 20 - (2 * z)  # H จะเป็นค่าที่คำนวณได้
            print("The monster HP: ", H)
            if H == 0 :
                 print("YOU WIN")
            elif H < 0 :
                 print("BRO YOU CHOPPED IT TOT")
            else :
                 print("NEXT ROUND")
    if y == 3 : 
            z = int(input("How many time you want to hit the monster: "))
            i =  0
            while i < z :
                i = i + 1
                print(f"You have hitted THE monster {i} time(s)")
            H = (20 - 3 * z)  # H จะเป็นค่าที่คำนวณได้
            print("The monster HP: ", H)
            if H == 0 :
                 print("YOU WIN")
            elif H < 0 :
                 print("BRO YOU CHOPPED IT TOT")
            else :
                 print("NEXT ROUND")

                    


                
