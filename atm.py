import time

print("Please insert your card")

time.sleep(5)

password=1234

pin=int(input("enter your Atm pin"))

balance = 5000

if pin==password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit""")

        try:
            option=int(input("Please enter your choise "))
        except:
            print("Please enter valid option")

        if option==1:
            print(f"your current balance is {balance}")

            print("====================================================")
            print("====================================================")
            print("====================================================")

        if option==2:

            withdraw_amount=int(input("please enter withdraw_amount"))

            print("====================================================")
            print("====================================================")
            print("====================================================")

            balance=balance-withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print("====================================================")
            print("====================================================")

            print(f"your updated balance is {balance}")

            print("====================================================")
            print("====================================================")

        if option==3:

            deposite_amount=int(input("please enter deposit_amount"))

            balance=balance+deposite_amount

            print("====================================================")
            print("====================================================")
            print("====================================================")

            print(f"{deposite_amount} is credited to your account")

            print("====================================================")
            print("====================================================")

            print(f"your updated balance is {balance}")

            print("====================================================")
            print("====================================================")


        if option==4:
            break



else:
    print("wrong pin Please try again")