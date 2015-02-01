import random

class Bicycle(object):
  def __init__(self, name, weight, cost):
    self.name = name
    self.weight = weight
    self.cost = cost
         

class Shop(object):
  
  def sell(self,customer):
    self.bikeToSell = random.choice(self.canAfford(customer.fund))
    self.bikeToSell['number'] = self.bikeToSell['number'] -1
    self.retail = self.getRetail(self.bikeToSell)
    
    self.profit = self.profit + (self.retail - self.bikeToSell['bike'].cost)
    return {"bycycle":self.bikeToSell,"cost":self.retail}
    
  
  def getRetail(self,bicycle):
    cost = bicycle['bike'].cost + (bicycle['bike'].cost * self.markup)
    return cost

  def canAfford(self,amount):
    bikes = []
    for item in self.inventory:
      if self.getRetail(item) < amount: 
        bikes.append(item)
    return bikes
  
  def printProfit(self):
    print "Total profit: $" + str(self.profit)
  
  def printInventory(self):
    print "Inventory for: " + self.name
    for item in self.inventory:
      print item['bike'].name + " number:" + str(item['number'])
  

  def __init__(self, name, inventory, markup):
    self.name = name
    self.inventory = inventory
    self.markup = markup
    self.profit = 0
    

class Customer(object):
  def buyBike(self, bikeshop):
    self.mybike = bikeshop.sell(self)
    self.fund = self.fund - self.mybike['cost']    

    print self.name + " has purchased a " + self.mybike['bycycle']['bike'].name
    print "For: $" + str(self.mybike['cost']) 
    print "and has $" + str(self.fund) + " left"
    print ""
    
  
  def __init__(self, name, fund):
    self.name = name
    self.fund = fund
    
if __name__ == '__main__':
  bikes = [{"bike":Bicycle("Schwimm",100,250),"number":2},
          {"bike":Bicycle("Valdemort",75,1800),"number":4},
          {"bike":Bicycle("Skipper",112,350),"number":8},
          {"bike":Bicycle("Zapp",80,1500),"number":3},
          {"bike":Bicycle("George",100,800),"number":2},
          {"bike":Bicycle("Crud",200,100),"number":17}]
  bikeshop = Shop("Big Bikes",bikes,0.20)
  
  customers = [Customer("Billy",2000),Customer("Sally",1000),Customer("Joey",750)]
  
  for customer in customers:
    print customer.name + " can afford these bikes:"
    bikechoices = bikeshop.canAfford(customer.fund)
    for bike in bikechoices:
      print(bike['bike'].name)
    print ""
    
  print bikeshop.name + " Inventory:"
  for item in bikeshop.inventory:
    print item['bike'].name + "     number: " + str(item['number'])
    
  for customer in customers:
    customer.buyBike(bikeshop)
    
  bikeshop.printInventory()
  bikeshop.printProfit()
  
 