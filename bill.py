print("*****WELCOME TO THE SHOP*****")
print("What would you like to buy?")
print("1.laptop")
print("2.mobile")
print("3.desktop")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Price of laptop is 120000")
    opt=input("If you want to buy type yes and if u don't type no: ")
    if opt=='yes':
        q=int(input("How many do you want to buy?"))
        total=120000*q
        print("Your total bill will be" ,total)
    else:
        print("Thank you for visiting!!")
elif choice==2:
    print("Price of mobile is 50000")
    opt=input("If you want to buy type yes and if u don't type no: ")
    if opt=='yes':
        q=int(input("How many do you want to buy?"))
        total=50000*q
        print("Your total bill will be" ,total)
    else:
        print("Thank you for visiting!!")
elif choice==3:
    print("Price of desktop is 100000")
    opt=input("If you want to buy type yes and if u don't type no: ")
    if opt=='yes':
        q=int(input("How many do you want to buy?"))
        total=100000*q
        print("Your total bill will be" ,total)
    else:
        print("Thank you for visiting!!")
else:
    print("Invalid choice.")

print("1.Payment through Cash")
print("2.Payment through Card")
pay=int(input("Enter your choice:"))
if pay==1:
    b='Cash'
else:
    b='Card'
name=input("What is your name? :")
phone=input("Your phone number:")
print("*****BILL FOR YOUR PURCHASE*****")
print("Name: ",name)
print("Contact: ",phone)
print("Total amount:",total)
print("Payment through",b)
print("Thankyou for visiting!!")



# loop while for


