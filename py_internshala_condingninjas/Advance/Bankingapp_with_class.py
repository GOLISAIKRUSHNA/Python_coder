class Bank:
    def __init__(self,init_amt):
        self.bal=init_amt
        

    def deposit(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
            self.bal=self.bal+amount
            self.Transaction(f"Deposited {amount}")
            print("Balance amt",self.bal)

    def withdraw(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
            self.bal=self.bal-amount
            self.Transaction(f"Withdrawal {amount}")
            print("Balance amt",self.bal)

    def Transaction(self,amount):
        try:
            amount=float(amount)
            
        except ValueError:
            amount=0
        with open("Bank_Transactions.txt","a")as file:
            file.write(f"{amount}\t\t\t\tBalance:{self.bal}\n\n")
            print("Balance Amount:",amount)
            exit()
    
    def insert(self):
        

        while True:
            
            try:
                if num in ["1","2","3"]:
                    if num=="1":
                        print("Enter the Deposit amount:")
                        hii.deposit(input("enter deposit amount:"))
                    elif num=="2":
                        print("Enter the withdraw  amount:")
                        hii.withdraw(input("enter withdraw amount:"))
                    else:
                        print("Your Balance is:")
                        hii.Transaction("1000")
                        break
            except KeyboardInterrupt:
                print("\n\n\n\n\nThanks for using virtual atm application")
                break


hii=Bank(0.00)
print("welcome to virtual Atm:")
print("============*****==========******===============")
try:
    print("Insert the number for Transaction: \n1.Deposit\n2.Withdraw\n3.Balance\n")
    num=input("Enter the Number:")
except KeyboardInterrupt:
    print("\n\n\Thanks for using virtual Bank")
    exit()

hii.insert()