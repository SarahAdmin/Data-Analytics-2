import pandas as pd 
myData2 = { 
  'Customer_ID':[12,43,64,67,95,29],
  'Customer_Name':['Lee Cox','Matt Bond','Marcy Rogers','Lana Montana','Amy Adams','Marie Quinn'],
  'Product':['Desk','Desk','Chair','Shelf','Bookshelf','Lamp'],
  'Quantity':[2,1,4,2,1,2],
  'Order_ID':[1,2,3,4,5,6]
}
shop1 = { 
      'Price':[120.00,120.00,10.00,65.84,200.50,30.59], 
      'Delivery':[False,True,False,True,True,True]
}
myVariables = pd.DataFrame(myData2) 
MyVar2 = pd.DataFrame(shop1) 
dataFour = myVariables.join(MyVar2)
dataFour['Subtotal'] = dataFour.eval('Price * Quantity')
print(dataFour)
