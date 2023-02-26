class Atm:
    def __init__(self):
        self.pin = ""
        self.amount = 0
        self.interface()


    def interface(self):
        user = int(input('''
        1. press 1 for create pin.
        2 .press 2 to deposit money
        3. press 3 to withdraw money
        4.press 4 to check remaining balance
        5.press 5 to exit'''))
        if user == 1:
            self.create_pin()
            self.interface()
        elif user == 2:
            self.deposit()
            self.interface()
        elif user == 3:
            self.withdraw()
            self.interface()
        elif user == 4:
            self.checkbalance()
            self.interface()
        else:
            print("exit")
            self.interface()

    def create_pin(self):
        self.pin = input("enter your pin")
        print("pin successfully set")

    def deposit(self):
        pin = input("enter your pin")
        if pin == self.pin:
            amount = int(input("enter your amount"))
            self.amount += amount
            print("amount set successfully")
        else:
            print("invalid pin")

    def withdraw(self):
        l = input("enter your pin: ")
        if l == self.pin:
            withdraw_money = int(input("enter your withdrawing amount: "))
            if withdraw_money < self.amount:
                self.amount -= withdraw_money
                print("money_withdraw")
            else:
                print("insufficient money")
        else:
            print("invalid pin")

    def checkbalance(self):
        l = input("enter yourt pin:")
        if l == self.pin:
            print(self.amount)
        else:
            print("invalid pin")


sbi = Atm()
