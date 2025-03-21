from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score  

import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Specie'] = iris.target  

# Features
X = df.drop(columns=['Specie'])  
y = df['Specie']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Loading and training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predicting
y_pred = model.predict(X_test)
print(y_pred)

# Check Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
