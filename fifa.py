from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("male_players (legacy).csv", low_memory=False)
df = df.dropna(subset=["passing","shooting","pace","dribbling","defending","physic","overall"])


x = df[["passing","shooting","pace","dribbling","defending","physic"]]
y =df["overall"]

train_x,test_x,train_y,test_y =  train_test_split(x,y, test_size= 0.2, random_state=42)

model = LinearRegression()
model.fit(train_x, train_y)

predictions = model.predict(test_x)
print(mean_absolute_error(test_y,predictions))
