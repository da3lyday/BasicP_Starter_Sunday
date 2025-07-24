x = str(input("Member type: "))
y = int(input("Total cost: "))
z = int(input("Date of the order: "))
if x == "gold" :
    if y >= 1000 :
        print("Discount 15% off: ", y * 15/100)
        print("Total cost: ", y - (y * 15/100))
    else :
        print("Discount 10% off: ", y * 10/100)
        print("Total cost: ", y - (y * 10/100))
        s = (y - (y * 10/100))
            if s > 500 :
            print("")
        
elif x == "Silver" :
    if y >= 1000 :
        print("Discount 10% off: ", y * 10/100)
        print("Total cost: ", y - (y * 10/100))
    else :
        print("Discount 5% off: ", y * 5/100)
        print("Total cost: ", y - (y * 5/100))
else :
    print("No discount")
