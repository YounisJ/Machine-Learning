import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,r2_score


# Load Dataset
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
df = pd.read_csv(url)
df = df.select_dtypes(exclude=['object'])
# df.isna().sum()

df_cleaned = df.dropna()
X = df_cleaned.drop(columns= ["mag"])
y = df_cleaned["mag"]

# Spliting dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Training and testing
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
# y_pred

# Accuracy
r2_scoring = r2_score(y_test,y_pred)
print("Accuracy: ",r2_scoring)