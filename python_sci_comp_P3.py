import math

class Category:
  category=''
  amount=0
  desp=""

  #ledger=list()
  def __init__(self,z):
    self.category=z
    self.ledger=list()
    #self.withdrawan=0
    self.total_withdraw=0 
    

  def deposit(self,amount,des=""):
    self.amount=amount
    self.desp=des
    obj=dict()
    obj["amount"]=self.amount
    obj["description"]=self.desp
    self.ledger.append(obj)
    
    
  def withdraw(self,amount,desp="",transfer=""):
    if self.amount<amount:
      return False
    else:
      self.desp=desp
      obj=dict()
      obj["amount"]=-amount
      obj["description"]=self.desp
      self.ledger.append(obj)
      self.amount=self.amount-amount
      if transfer=="":
        #self.withdrawan=self.withdrawan+amount
        self.total_withdraw=self.total_withdraw+amount
      return True

  def get_balance(self):
    return self.amount
  
  def get_ledger(self):
    return self.ledger
  
  def get_category(self):
    return self.category
  
  def get_withdrawan(self):
    return self.withdrawan
  
  def total_withdrawan():
    return Category.total_withdraw
    
  def transfer(self,amount,cat):
    str="Transfer to "+cat.get_category()
    if self.withdraw(amount,str,"transfer")==False:
      return False
    else:
      despp="Transfer from "+self.category
      cat.deposit(amount,despp)
      return True
    
  def check_funds(self,amount):
    if self.amount<amount:
      return False
    else:
      return True
    
  def __repr__(self):
    to_return=self.category.center(30,'*')
    k=0
    total=0
    for i,j in self.ledger:
      try:
        strr=str(self.ledger[k][i]).split('.')
        strrn=strr[0]+'.'+strr[1].ljust(2,'0')
      except:
        strrn=str(self.ledger[k][i])+'.00'
      
      to_return=to_return+'\n'+(self.ledger[k][j][:23].ljust(23)+strrn.rjust(7)).ljust(30)
      total=total+self.ledger[k][i]
      k=k+1
    total=str(total).split('.')
    tot=total[0]+'.'+total[1].rjust(2,'0')
    to_return=to_return+'\n'+"Total: "+str(tot)
    return to_return
    

def create_spend_chart(categories):
  to_return=""
  to_return=to_return+"Percentage spent by category"+'\n'
  length=len(categories)
  withdlist=list()
  withdlist=get_withdraw_distribution(categories)
  for i in reversed(range(11)):
    j=0 if i==0 else i*10
    to_return=to_return+str(j).rjust(3,' ')+'|' if i==10 else to_return+'\n'+str(j).rjust(3,' ')+'|'
    for k in range(length):
      val='   ' if withdlist[k]<j else ' o '
      to_return=to_return+val


  dashnum=length+1+2*length
  dash=''
  for i in range(dashnum):
    dash=dash+'-'
  to_return=to_return+'\n'+'    '+dash


  lenlist=list()
  for i in range(length):
    lenlist.append(len(categories[i].get_category()))
  max=lenlist[0]
  for i in lenlist:
    if max<i:
      max=i

  cat_names=list()
  for i in range(length):
    cat_names.append(categories[i].get_category())
  for i in range(max):
    value=''
    for j in range(length):
      try:
        value=value+' '+cat_names[j][i] if j==0 else value+'  '+cat_names[j][i]
      except:
        value=value+'  ' if j==0 else value+'   '
    to_return=to_return+'\n'+'    '+value
  return(to_return)
    
def get_withdraw_distribution(categories):
  total_withdraws = 0
  distibution = {}
  to_returnn=[]
  for categoryy in categories:
    total_withdraws += categoryy.total_withdraw
  for categoryy in categories:
    exact_dis = (categoryy.total_withdraw *100 / total_withdraws)
    distibution[categoryy.category] = (exact_dis // 10) * 10

  for key,value in distibution.items():
      to_returnn.append(value)
    
 
  return to_returnn

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business,food,entertainment]))

