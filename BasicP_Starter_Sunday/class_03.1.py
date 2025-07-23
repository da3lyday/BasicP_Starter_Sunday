print("Fat Usagi Monster(20 HP)")
x = str(input("Choose your path 1.Fight 2.Run : "))
if x == "Fight" :
    y = int(input("Choose your weapon 1.Claymore(-5 HP) 2.Pocket knife(-2 HP) 3. Whip(-3 HP) : "))
    # z = int(input("How many time you wan to hit the monster: "))
    if y == 1 : 
            z = int(input("How many time you wan to hit the monster: "))
            i =  20
            while z == 0 :
                  print(f"Hit {i} time(s)")
                  i = i - 5




