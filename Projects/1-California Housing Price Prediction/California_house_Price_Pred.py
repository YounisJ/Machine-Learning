# Import Neccessory Libararies
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load Dataset
california_housing = fetch_california_housing()
df = pd.DataFrame(california_housing.data, columns=data.feature_names)
df['House_Value'] = california_housing.target

# Splict dataset into X and y , 80% and 20%
X = df.drop(columns=["House_Value"])
y = df["House_Value"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Load and Train the model
model = LinearRegression()
model.fit(X_train,y_train)

# Accuracy
y_pred = model.predict(X_test)
print(r2_score(y_test,y_pred))
