import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

x = df[["Age"]]
y = df["Salary"]

model = LinearRegression()

model.fit(x,y)

print(model.predict([[20]]))
