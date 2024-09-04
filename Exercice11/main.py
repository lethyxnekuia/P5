## Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder: str = account_holder
        self.balance: float = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("On ne peut pas déposer un nombre négatif ou nul")
        self.balance += amount
        print(f"Montant déposé : {amount}. Nouveau solde : {self.balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("On ne peut pas retirer un nombre négatif ou nul")
        if amount > self.balance:
            raise ValueError("Solde Insuffisant")
        self.balance -= amount
        print(f"Montant retiré : {amount}. Nouveau solde : {self.balance}")

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"solde : {self.balance}")
