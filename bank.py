print("*****WELCOME TO ATM*****")
pin=int(input("Enter your pin:"))
if pin==1234:
    amount=50000
    print("1.withdraw")
    print("2.Balance enquiry")
    option=int(input("Enter your option:"))
    if option==1:
        new_amount=int(input("Enter the amount to withdraw: "))
        if new_amount>amount:
            print("Insufficient Balance")
        else:
            rem=amount-new_amount
            print("Withdraw amount is",new_amount)
            print("Remaining balance is",rem)
    elif option==2:
        print("Your balance is: ",amount)
    else:
        print("Invalid option")
else:
    print("Wrong pin")
exit()


