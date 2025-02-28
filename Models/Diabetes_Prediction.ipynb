import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



# Load the dataset
diabetes_ds = load_diabetes()
df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
df["diabetes_progression"] = diabetes_ds.target

# Split dataset
X = df.drop(columns=["diabetes_progression"])
y = df["diabetes_progression"]


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Load, train and make predictions
model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

# Evaluate
print(r2_score(y_test,predictions))
