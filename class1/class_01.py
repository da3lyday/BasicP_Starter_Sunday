x = int(input("enter your number: "))
if x < 5 :
    print("Free shiping")
elif 5 <= x <= 50 :
    print("Price 10 Baht")
    print("Included Fee",10 * 107/100)
elif 51 <= x <= 100 :
    print("Price 15 Baht")
    print("Included Fee",15 * 107/100)
elif 101 <= x <= 300 :
    print("Price 25 Baht")
    print("Included",25 * 107/100)
elif 301 <= x <= 500 :
    print("Price 35 Baht")
    print("Included Fee",35 * 107/100)
else :
    print("Price 45 Baht")
    print("Included Fee",45 * 107/100)