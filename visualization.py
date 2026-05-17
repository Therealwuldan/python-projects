import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

plt.plot(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.savefig("line.png")
plt.show()