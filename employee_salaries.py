import pandas as pd 

data = {'Name':['Lee Cox','Matt Bond','Pamela Adams','Alex Baxter','Jonah Parker','Jill Gates'], 'Position':['Junior Computer Scientist','Financial Analyst','Lawyer','Financial Analyst','Project Manager','Computer Scientist'],'Annual Salary':[35000,40000,65000,40000,80000,75000]} 

final_data = pd.DataFrame(data,index=[1,2,3,4,5,6])
salaryOne = final_data.where(final_data['Annual Salary'] < 60000).dropna()
print(salaryOne)
