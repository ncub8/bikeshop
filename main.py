from bicycles import Customer
from bicycles import Bicycle
from bicycles import Shop

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
    
  bikeshop.printInventory()
  print ""
    
  for customer in customers:
    customer.buyBike(bikeshop)
    
  bikeshop.printInventory()
  bikeshop.printProfit()