# Name : BankAccount
# para : acc_holder, balance, branch, type
# func : deposit or withdraw
# data privacy! ----> private : access within classes ---> protected : access within the classes
# which has relationship (inheritance), public : access everywhere! (default)
# Encapsulation: private data (properties) and access them through a function
# Setting default!
# auto generate  account ID?
class BankAccount:
    __Generator = 0
    def __init__(self, acc_holder, branch, type = "Saving", balance = 0):

        self.id = self.__Generator + 1
        self.__acc_holder = acc_holder
        self.__branch = branch
        self.__type = type
        self.__balance = balance # making the parameters private!
        BankAccount.__Generator += 1

    def __str__(self):
        return f'Bank Account ID : {self.id}--> Branch : {self.__branch}, Type : {self.__type}' \
               f'\nAccount Name : {self.__acc_holder}, Balance : {self.__balance}'

    def widthraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('insufficient fund!')

    def getBalance(self): return self.__balance

acc1 = BankAccount('Hesam', "TD", "Saving", 1000)
# acc2 = BankAccount( 'Tony', "Scotia", "Chequing", 1260)
print(acc1)
# print(acc2)
# print(acc1)
acc1.widthraw(10)
print(acc1)

# acc3 = BankAccount('Adam',"TD", "saving")
# print(acc3)

# alist = []
# for i in range(4, 10):
#     alist.append(BankAccount("Dummy {i}", "TD","chequing"))

# print(alist)

# for acc in alist : print(acc)
