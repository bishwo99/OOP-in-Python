from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Bkash(Payment):
    def pay(self,amount):
        print(f'Paid {amount} taka by Bkash.')

class Card(Payment):
    def pay(self,amount):
        print(f"Paid {amount} taka by Card.")

class PayPal(Payment):
    def pay(self,amount):
        print(f"Paid {amount} taka by PayPal.")

bkash = Bkash()
card = Card()
paypal = PayPal()

bkash.pay(1000)
card.pay(2000)
paypal.pay(5000)
