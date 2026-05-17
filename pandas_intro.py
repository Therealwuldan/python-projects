import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Toronto", "New York", "London"]
}

df = pd.DataFrame(data)
print(df["Age"])
print(df["Age"].mean())
print(df[df["Age"] > 2])


df = pd.read_csv("data.csv")
print(df["Salary"].max())
print(df["Salary"].mean())
print(df[df["City"] == "Toronto"])
df["Salary_USD"] = df["Salary"] * 0.73
print(df["Salary_USD"])

df.to_csv("data.csv", index=False)
print(df.iloc[1])
