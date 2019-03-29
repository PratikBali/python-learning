class BankAccount():
    ROI = 10.5

    def __init__(self):
        self.name = 'name'
        self.balance = 0

    def Deposit(self):
        amount = int(input('Enter amount to Deposit: '))
        self.balance += amount
        print('Balance:', self.balance)

    def Withdraw(self):
        amount = int(input('Enter amount to Withdraw: '))

        if self.balance and self.balance > amount:
            self.balance -= amount
            print('Remaining balance:', self.balance)
        else:
            print('Insufficient funds!')

    def CalculateInterest(self):
        interest = self.balance * BankAccount.ROI / 100
        print('interest', interest)

    def Display(self):
        print(self.name, 'balance:', self.balance)

    def Accept(self):
        # print('Deposit: 1' )
        # print('Withdraw: 2' )
        # mode = input('Enter mode number: ')
        name = input('Enter your name : ')
        self.name = name

        # if mode:
        # mode = int(mode)
        # if mode == 1 or mode == 2:
        # bank = BankAccount(name)
        # if mode == 1:

        # else:
        # bank.CalculateInterest()
        #     else:
        #         print('Invalid input Please type 1 or 2 and then hit enter!')
        # else:
        #     print('Invalid input Please type 1 or 2 and then hit enter!')


if __name__ == '__main__':
    bank = BankAccount()
    bank.Accept()
    bank.Deposit()
    bank.Withdraw()


    bank.Display()