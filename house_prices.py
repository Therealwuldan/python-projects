import  pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error



df = pd.read_csv("train.csv")


x = df[["GrLivArea", "BedroomAbvGr", "FullBath","YearBuilt", "OverallQual", "GarageArea"]]
y = df["SalePrice"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)


model = LinearRegression()

#Training the input of all random train_num%  to predict a price
model.fit(x_train,y_train)

#Creating a price prediction based on the trained data above
predictions = model.predict(x_test)

print(mean_absolute_error(y_test, predictions))


print(model.predict([[1500, 3, 2, 2005, 10, 400]]))