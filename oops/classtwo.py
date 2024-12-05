class Bankaccount:
    def __init__(self,customername,balance,account_no):
        self.customername=customername
        self.balance=balance
        self.account_no=account_no
        
    def __str__(self):
        return self.customername
        
customer1=Bankaccount("siva",60000,12345)
print(customer1.customername,customer1.balance,customer1.account_no)
customer2=Bankaccount("saran",500000,456)
print(customer2.customername,customer2.balance,customer2.account_no)
print(customer1)