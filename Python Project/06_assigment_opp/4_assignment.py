
class Bank():
    bank_name = "Default Bank"

    def __init__(self, accout_holder):
        self.accout_holder = accout_holder

    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name

    def display(self):
        print(f"Account holder: {self.accout_holder}, Bank name: {self.bank_name}")

    
bank1 = Bank("Ahmed")
bank1.display()


bank1.change_bank_name("State Bank of pakistan")
bank1.display()

