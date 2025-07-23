x = int(input("Enter your score: "))
if 50 <= x <= 100 :
    print("Pass")
    if x >= 80 :
        print("A")
    elif x >= 70 :
        print("B")
    elif x >= 60 :
        print("C")
elif x < 50:
    print("F")
else :
    print("Eror")