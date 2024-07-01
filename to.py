print("*****WELCOME TO THE SHOP*****")
print("What would you like to buy?")
print("1.Dell laptop")
print("2.Lenovo Laptop")
print("3.Mac Book")
choice=int(input("Enter your choice:"))
if choice==1:
    product='Dell_laptop'
    print("Price of laptop is 120000")
    quant=int(input("How many do you want to buy?:"))
    price=120000*quant
elif choice==2:
    product='Lenovo_laptop'
    print("Price of laptop is 150000")
    quant=int(input("How many do you want to buy?:"))
    price=150000*quant
elif choice==3:
    product='Mac_Book'
    print("Price of laptop is 200000")
    quant=int(input("How many do you want to buy?:"))
    price=200000*quant

tax=0

print("Delivery option: \n 1. Home Delivery in Kathmandu(Rs.500) \n 2. Pickup(Rs.0)")
opt=int(input("Enter your delivery choice:"))
if opt==1:
    delivery_price=500
    print("Location: \n 1. Kathmandu(13% tax) \n 2. Lalitpur(0% tax) \n 3.Bhaktapur(0% tax) ")
    opt=int(input("Enter your location :"))
    if opt==1:
        tax=price*0.13
elif opt==2:
    delivery_price=0

print("Packing option: \n 1. Plastic bag(Rs.500) \n 2.Bag(Rs.1000) \n 3. Gift boz(Rs.2500))")
opt=int(input("Enter your choice:"))
if opt==1:
    packing_price=500
elif opt==2:
    packing_price=1000
elif opt==3:
    packing_price=2500

total=price+delivery_price+packing_price+tax

name=input("What is your name? :")
phone=input("Your phone number:")
print("*****BILL FOR YOUR PURCHASE*****")
print("Name: ",name)
print("Contact: ",phone)
print("Product name: ",product)
print("Quantity: ",quant)
print("Total price: ",price)
print("Delivery price: ",delivery_price)
print("Packing Price: ",packing_price)
print("Tax amount: ",tax)
print("Grand total: ",total)
print("Thank you for visiting!!")















