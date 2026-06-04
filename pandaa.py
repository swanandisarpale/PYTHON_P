import pandas as pd
data={
    "name":["a","b","c"],
    "salary":[11,12,13]
}
    
df=pd.DataFrame(data)
print(df)

avg_salary=df["salary"].mean()
print("avg salary",avg_salary)
