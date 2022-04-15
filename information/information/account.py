class Main_account :
    def __init__(self, account = "", name = "", money = 0) :
            self.account = account
            self.name = name
            self.money = int(money)
    
    def deposit(self, charge) :
        self.money = self.money + charge

    def withdraw(self, withdrawal) :
        self.money = self.money - withdrawal