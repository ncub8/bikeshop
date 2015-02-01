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
