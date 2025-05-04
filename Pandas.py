import pandas as pd
data={'Name':['Aditya','Dhruva','Yash','Ashu'],'Age':[18,19,18,18],'City':['London','NYC','Paris','Pune']}
df=pd.DataFrame(data)
age=df['Age']
print("Selected age column:\n",age)
filter=df[df['Age']>18]
print("Filtered age column:\n",filter)