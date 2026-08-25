from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
        self.transaction=[]
    @abstractmethod
    def account_type(self):
       pass
    def deposit(self,amount):
        if amount<=0:
            print("deposit amount must be greater than 0.")
            return False
        self.__balance +=amount
        self.transaction.append(f"deposited: Rs.{amount}")
        print(f"Rs.{amount} deposited successfully!")
        return True
    def withdraw(self, amount):
     if amount <= 0:
        print("❌ Withdrawal amount must be greater than 0.")
        return False
     if amount > self.__balance:
        print("❌ Insufficient balance.")
        return False
     self.__balance -= amount
     self.transaction.append(
        f"Withdraw: Rs.{amount}")
     print(f"✅ Rs.{amount} withdrawn successfully.")
     return True
        
    def get_balance(self):
        return self.__balance
    def show_transaction(self):
        print("\n ======== Transaction History: ========")
        if not self.transaction:
            print("No transcation yet.")
            return
        for number,transaction in enumerate(self.transaction,start=1) :
            print(f"{number}.{transaction}")
    def show_details(self):
        print("\n ======= Account Details =======")
        print(f"Owner : {self.owner}")
        print(f"Account Type : {self.account_type()}")
        print(f"Balance : Rs.{self.get_balance()}")
class SavingsAccount(BankAccount) :
    def account_type(self) :
        return "SAVING ACCOUNT"
class CurrentAccount(BankAccount):
    def account_type(self):
        return "CURRENT ACCOUNT"    
def bank_menu(account):
    while True:
        print("\n==============================")
        print("          Bank Account System")
        print("=================================")
        print("1. Deposit Money")
        print("2. Withdraw Money") 
        print("3. Check Balance") 
        print("4. Transaction History") 
        print("5. Account Details") 
        print("6. Account Type") 
        print("7. Exit") 
        print("========================================") 
        choice = int(input("Enter your choice: "))
        if choice==1:
            try:
                amount=float(input("Enter deposit amount :"))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")  
        elif choice==2:
            try:
                amount=float(input("enter withdrawl amount:"))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice==3:
            print(f"Current Balance: Rs.{account.get_balance()}")
        elif choice==4:
            account.show_transaction() 
        elif choice==5:
            account.show_details() 
        elif choice==6:
            print(f"\n Account Type: {account.account_type()}")
        elif choice==7:
            print("\n Thank you for using bank account system.")
            break
        else:
            print("Invalid choice.Please select 1-7.")
print("========================================") 
print(" WELCOME TO BANK SYSTEM") 
print("========================================") 
owner = input("Enter account owner's name: ") 
print("\nSelect Account Type:") 
print("1. Savings Account") 
print("2. Current Account") 
account_choice = int(input("Enter your choice: ")       )           
try:
    initial_balance=float(input("Enter initial balance:"))
except ValueError:
    print("Invalid balance.")
    initial_balance=0
if account_choice==1:
    account=SavingsAccount(owner,initial_balance)
elif account_choice==2:
    account=CurrentAccount(owner,initial_balance)
else:
    print("Invalid account type.")
    exit()
bank_menu(account) 
