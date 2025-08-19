
count = 0
balance = 1000
code = "*556#"


print(
'''
|==========================|
|  ++++++++++              |
|WELCOME! TO MTN SERVICES! |
|                          |
| Everywhere you go!       |  
|    ++++++++++            |
|                          |
|==========================|
 '''
)
user = input("Enter the pin here:")
if user == code:
    while True:
        #user = input("Enter the pin here:")
        print(
        '''
	AVAILABLE SERVICES
	1 :Buy Airtime
	2 :Buy Data
	3 :Borrow AIrtime/Data
	4 :Check Balance
	5 :Stop
        ''')
        user_option = int(input("Enter option:"))
        if user_option == 1:
            print("Enjoy our airtime bundle at a minimum rate")
            print("")
            user = float(input("Enter the amount you wish to buy:₦"))
	 
            if balance >= user:
                balance -= user 
                print(f"you have been credited with : ₦{user}")
            else:
                print("Insufficient funds!")
        elif user_option == 2:
            print(
	    '''
	    Buy our cheap Data Bundles
	    1 :500MB = ₦200
	    2 :700MB = ₦250
	    3 :1GB = ₦300
            4 :2GB = ₦600
            5 :3GB = ₦900
            '''
	    )
            user = int(input("Enter option:"))
            if user == 1:
                balance -= user
                print("succesfully recieved 500MB")
            elif user == 2:
                balance -= user
                print("successfully credited with 1GB")
            elif user == 3:
                balance -= user
                print("successfully recieved 2GB!")
            elif user == 4:
                balance -= user
                print("successfully recieved 3GB!")
            elif user == 5:
                balance -= user
                print("successfully recieved 3.5GB!")
            else:
                print("Invalid command")
            
        elif user_option == 3:
	    
            print('''
            ENTER OPTION:
            1.Borrow Airtime
            2.Borrow Data
            ''')
            user = int(input("Choose option:"))
            print("")
            if user == 1:
                
                print("Enjoy cheap airtime as low as 15% rate")
                user = float(input("Enter your amount:"))
                if balance >= user:
                    balance -= user
                    percent = (15 / 100) * user
                    user -= percent
                    print(f"you account have been credited with:  ₦{user}")
                    print(f"Remaining balance is : {balance}")
                else:
                    print("Insufficient funds")
            elif user == 2:
                print("Borrow Data as low as %15 rate ")
                print('''
                1 :500MB = ₦200
                2 :700MB = ₦250
                3 :1GB = ₦300
                4 :2GB = ₦600
                5 :3GB = ₦900
                ''') 
                user = int(input("select plan:"))
                if user == 1:
                    percent = (15 / 100) * 200
                    percent += 200
                    balance -= percent
                    print("Suceesfully recieved:500MG")
                    print(f"remaining balance is {balance}")

                elif user == 2:
                    percent = (15 / 100) * 250
                    percent += 250
                    balance -= percent
                    print("Suceesfully recieved: 700MG")
                    print(f"remaining balance is {balance}")

                elif user == 3:
                    percent = (15 / 100) * 300
                    percent += 300
                    balance -= percent
                    print("Suceesfully recieved: 1GB")
                    print(f"remaining balance is {balance}")

                elif  user == 4:
                    percent = (15 / 100) * 600
                    percent += 600
                    balance -= percent
                    print("Suceesfully recieved: 2GB")
                    print(f"remaining balance is {balance}")

                elif user == 5:
                    percent = (15 / 100) * 900
                    percent += 900
                    balance -= percent
                    print("Suceesfully recieved: 3GBG")
                    print(f"remaining balance is {balance}")
                
                else :
                    print("Invalid option")
            else:
                print("Invalid option")

        elif user_option == 4:
            print(f"Your balance is: {balance}")
        elif user_option == 5:
            print("transaction stopped!")
            break
        else:
            print("Invalid option")
           
else:
    print("Invalid pin")


