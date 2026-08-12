1. AI Data Classification Project (Iris Dataset)
📌 Project Overview & Problem Statement
Manual rules ya hardcoded if-else conditions likhna complex datasets ke liye impossible hota hai. Jab hamare paas multi-dimensional data hota hai (jaise phoolon ki alag-alag length aur width), toh human intelligence ke zariye exact boundaries set karna mushkil ho jata hai.
Is project ka goal Machine Learning ke Supervised Learning approach ko use karke ek automated predictive model banana hai jo historical data se pattern seekh kar naye samples ko sahi category me divide kar sake.
💡 Solution & Technical Workflow
Is problem ko solve karne ke liye humne ek Decision Tree Classification Model banaya hai. Ye workflow 4 main steps me kaam karta hai:
 * Data Ingestion: Scikit-Learn library se Iris dataset ko direct memory me load kiya gaya hai.
 * Train-Test Split: Dataset ko 80% Training Set aur 20% Testing Set me baanta gaya hai.
 * Model Training: Decision Tree Algorithm ka use karke model ko train kiya gaya hai.
 * Evaluation: Trained model ki Accuracy Score aur Classification Metrics calculate ki gayi hain.
⚙️ Step 1: Environment Setup & Library Installation
Project ko run karne ke liye sabse pehle zaroori Python libraries install karni hoti hain.
Installation Command:
pip3 install pandas scikit-learn
Explanation:
 * pandas: Data ko tabular form (dataframe) me handle aur view karne ke liye.
 * scikit-learn: Iris dataset load karne, train-test split karne aur Decision Tree classification algorithm run karne ke liye.
💻 Step 2: Main Python Source Code
Yeh hamari main Python file (week2_classification.py) ka source code hai:
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
 # 1. Dataset Load karna
print("--- Step 1: Loading Dataset ---")
iris = load_iris()
X = iris.data  # Features (Sepal/Petal Length & Width)
y = iris.target  # Labels (Setosa, Versicolor, Virginica)
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

# 3. Decision Tree Model Train karna
print("\n--- Step 3: Training the Classification Model ---")
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Model Evaluation & Prediction
print("\n--- Step 4: Model Evaluation ---")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

Code Explanation:
 * load_iris(): Scikit-Learn ke andar built-in dataset ko load karta hai.
 * train_test_split(): Data ko 80% training data aur 20% testing data me divide karta hai.
 * DecisionTreeClassifier(): Algorithm create karta hai jo decision boundaries banata hai.
 * fit(): Training data se model ko pattern sikhata hai.
 * predict(): Testing data ke upar predictions nikalta hai.
📊 Step 3: Execution & Output Results
Code ko run karne ke liye terminal me yeh command chalayein:
python3 week2_classification.py

Terminal Output:
--- Step 1: Loading Dataset ---
Dataset Head:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                5.1               3.5                1.4               0.2       0
1                4.9               3.0                1.4               0.2       0

--- Step 2: Splitting Data ---
Training Samples: 120, Testing Samples: 30

--- Step 3: Training the Classification Model ---

--- Step 4: Model Evaluation ---
Model Accuracy: 100.00%

Classification Report:
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

Output Explanation:
 * Accuracy (100%): Model ne test dataset ke saare 30 samples ko bilkul correct classify kiya hai.
 * Precision / Recall / F1-Score: Saari 3 species (setosa, versicolor, virginica) par 1.00 score yeh show karta hai ki model me 0% error margin hai.
Developed for DecodeLabs AI Industrial Internship (Batch 2026) 
