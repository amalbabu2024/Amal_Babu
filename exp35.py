class bank:
    def __init__(self,accno,name,accty):
        self.accn=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("Account Holder Name= ",self.name)
        print("AccountNumber= ",self.accn)
        print("Account type=",self.accty)
        print("Your Balance Amount= ",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("Enter your name= ")
t=input("Enter your account type= ")
a=input("Enter your account number= ")
o=bank(a,n,t)
print("Your Account details are= ")
o.showamt()
d=0
while(True):
    print("\n Menu")
    print("\n 1.Deposit")
    print("\n 2.Withdrawl")
    c=int(input("Enter your choice: "))
    #d=0
    if(c==1):
        d=int(input("Enter the ammount to deposit: "))
        print("Your Total Balance Amount is:",o.dep(d))
    elif(c==2):
        w=int(input("Enter the amount to be withdrawn: "))
        if(w>d):
            print("Insufficient Balance")



        else:
            print("Your Total Balance Amount is: ",o.withd(w))
    else:
        print("Invalid Choice.")
