import pandas as pd
emp = {
    'name': ['Pandu', 'Nayak', 'Rashmi', 'Mallya', 'Prad', 'Prabhu', 'Sai', 'Vinod', 'John'],
    'dept': ['HR', "Sale", "Marketing", 'HR', "Sale", "Marketing", 'HR', "Sale", "Marketing"],
    'salary': [100, 200, 300, 400, 500, 600, 150, 250, 350]
}

df = pd.DataFrame(emp)
df1 = df.groupby("dept").agg({"salary": "min"})
df2 = df.groupby("dept").apply(lambda x: x[x["salary"] == x["salary"].min()])

print(df1)
print(df2)

#2nd highest salary
df["rank"] = df.groupby("dept")["salary"].rank(ascending=False, method='dense')
print(df)
print(df[df["rank"] == 2.0])
