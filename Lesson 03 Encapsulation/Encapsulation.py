class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposite(self,ammount):
        self.ammount = ammount
        if ammount>0:
            self.__balance += ammount
    def show_balance(self):
        print(f"Your account has {self.__balance}")

Grahok = BankAccount('Bishwojit',1000)
Grahok.deposite(500)

Grahok.show_balance()
