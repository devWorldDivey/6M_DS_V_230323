class Atm:
    # constructor - special method which executes automatically once class object is called
    # instances Variable - 
    # Reference Variable
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()
        
    def __menu(self):
        user_input = input("""
                           Hello, how wounld you like to proceed?
                           1. Enter 1 to create __pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check __balance
                           5. Enter 5 to exit
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")
    
    def create_pin(self):
        self.__pin = input("Enter your __pin")
        print("__pin set successfully")
    def deposit(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            amount = int(input("ENter the amount"))
            self.__balance = self.__balance +amount
            print("Deposit Successfully")
        else:
            print("Invalid __pin")
    def withdraw(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Successfully")
            else:
                print("Insuficient funds")
        else:
            print("invalid __pin")
    def check_balance(self):
        temp = input("Enter your __pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid __pin")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("Pin changed")
