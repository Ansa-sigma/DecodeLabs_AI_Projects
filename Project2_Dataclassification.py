import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Dataset Load aur Explore karna
print("--- Step 1: Loading Dataset ---")
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels/Classes

df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print("Dataset Head:")
print(df.head())

# 2. Data ko Train aur Test sets me Split karna
print("\n--- Step 2: Splitting Data ---")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

# 3. Classification Algorithm (Decision Tree) Apply karna
print("\n--- Step 3: Training the Classification Model ---")
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Model Testing aur Evaluation
print("\n--- Step 4: Model Evaluation ---")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
