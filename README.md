# Project 1: CampusRide — Student Carpool Assistant CHATBOT 
## 📌 Executive Summary
CampusRide is a specialized, dual-role interactive terminal application designed to resolve daily commuting challenges for university students across Narowal, Shakargarh, and surrounding campus regions. Developed as part of the DecodeLabs Artificial Intelligence Internship Track (Project 1), the system connects student drivers and student passengers to facilitate automated route discovery, dynamic ride offering, structured seat booking, and conversation audit logging.
## 🎯 Problem Statement
University students face daily commuting obstacles, including rising fuel expenses, limited campus parking availability, and uncoordinated public transit schedules. While peer-to-peer carpooling offers an ideal solution, existing manual coordination lacks:
 * Dynamic Ride Offering: A structured method for student drivers to offer empty seats on the go.
 * Transparent Route Information: Clear visibility into fares, pickup stops, driver ratings, and credentials.
 * Safety & Verification Standards: Transparent verification protocols such as Student ID authentication, live GPS tracking, and SOS preparedness.
 * Audit & Activity Tracking: Maintaining a continuous interaction history for system optimization and security audit trails.
## 💡 System Architecture & Core Functional Modules
CampusRide operates as a stateful, rule-based conversational interface capable of managing dynamic runtime memory and multi-step interactive workflows:
1. 🚏 Dynamic Route Database & Discovery
 * Pre-configured with major student transit corridors (e.g., Shakargarh ➔ Campus, Narowal City ➔ Campus, Zafarwal ➔ Campus, Local Hostels Express).
 * Displays active route listings complete with driver department info, fare per seat, departure timings, and verified safety badges.
## 2. 🚗 Driver Module ("Offer a Ride")
 * Allows student drivers to publish new carpool options dynamically during runtime.
 * Interactively prompts drivers for essential credentials: Full Name, Department/Roll No, Contact/WhatsApp Number, Vehicle Details, Pickup Area, Destination, Fare, and Departure Time.
 * Automatically assigns a unique Route ID and integrates the newly offered ride into the active live database without needing a program restart.
 ## 3. 📝 Passenger Module ("Book a Ride")
 * Supports interactive route detail inspection (fare breakdown, specific pickup stops, driver ratings, and vehicle safety info).
 * Implements a state-managed booking flow that collects passenger details and issues an instant seat reservation confirmation.
## 4. 🛡️ Campus Safety Policy Engine
 * Enforces campus-only safety standards, including mandatory official Student ID authentication, peer rating visibility, and live GPS readiness.
## 5. 📄 Automated Conversation Audit Logger
 * Automatically captures all student queries, forms submitted, and system responses with precise timestamps into an audit log file (carpool_chat_history.log).
## 🔄 Operational Workflow
1. Student Input Ingestion**
   └── Student sends a query or command (e.g., `routes`, `offer`, `safety`, or `1`).

2. Intent Normalization & Keyword Matching**
   └── Text is cleaned (lowercased/trimmed) and mapped to system intents or active states.

3. Interactive Module Execution**
   ├── **Route Discovery**: Displays available rides and prompts for Route ID selection.
   ├── **Seat Booking**: Collects passenger details, confirms reservation, and shows receipt.
   ├── **Offer a Ride**: Prompts driver form and dynamically appends new route to live database.
   └── **Safety & Policy**: Responds with Student ID verification and tracking standards.

4. Audit Logging & State Update**
   └── Interaction details and timestamps are appended to `carpool_chat_history.log`.

## 📊 Interaction Summary & Use Cases
| Interaction Domain | Primary System Function | Workflow Executed |
| Route Discovery | Lists available student rides | Parses route database and displays options with driver names and fares. |
| Driver Registration | Dynamic ride publishing | Prompts driver form, collects ride attributes, and dynamically updates database. |
| Passenger Booking | Seat reservation | Captures student ID and pickup spot, then returns confirmed booking receipt. |
| Safety Inquiries | Security policy verification | Explains campus verification, driver ratings, GPS tracking, and SOS features. |
| Audit Logging | Historical record generation | Appends timestamped inputs and responses to carpool_chat_history.log. |
Developed by Ansa for DecodeLabs Artificial Intelligence Internship Track (Batch 2026) 


# Project 2: Machine Learning Data Classification Engine using AI 
## 📌 Project Overview & Problem Statement
Writing manual rules or hardcoded conditional statements (if-else blocks) becomes virtually impossible when dealing with complex, multi-dimensional datasets. When working with feature vectors—such as varying sepal and petal measurements in floral species—human analysis struggles to establish precise decision boundaries.
The primary objective of this project is to build an automated predictive pipeline using a Supervised Machine Learning approach. The model learns underlying feature patterns from historical training data to accurately categorize unseen samples into their respective target classes.
## 💡 Solution & Technical Workflow
To tackle this classification problem, a Decision Tree Classifier model was constructed. The end-to-end Machine Learning pipeline is executed in four main stages:
 * Data Ingestion: The standard Iris Dataset is loaded into memory directly via Scikit-Learn.
 * Train-Test Split: The dataset is partitioned into an 80% Training Set and a 20% Testing Set to ensure unbiased evaluation.
 * Model Training: A Decision Tree Algorithm is fitted on the training features and target labels.
 * Model Evaluation: The performance is validated on the unseen test set using Accuracy Score and Classification Metrics.
⚙️ Environment Setup & Dependencies
To execute this machine learning pipeline, the required Python packages can be installed using pip:
pip3 install pandas scikit-learn

## Dependency Breakdown:
 * pandas: Used for data manipulation, structured DataFrame representation, and viewing dataset heads.
 * scikit-learn: Provides built-in dataset utilities, train-test splitting modules, decision tree estimators, and evaluation metrics.
## 💻 Technical Implementation Details
The underlying source code (Project2_Dataclassification.py) executes the following operations:
 * load_iris(): Ingests the benchmark dataset containing 150 samples across 4 physical features.
 * train_test_split(): Splits 120 samples into training vectors and isolates 30 samples for model testing (test_size=0.2).
 * DecisionTreeClassifier(): Initializes the supervised tree algorithm to learn non-linear decision boundaries.
 * fit(): Trains the decision tree model on feature patterns.
 * predict(): Evaluates model generalizations against unseen testing feature sets.
## 📊 Performance Evaluation & Execution Output
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

## Metrics Analysis:
 * Accuracy (100.00%): The model correctly identified all 30 unseen test samples without a single misclassification.
 * Precision / Recall / F1-Score: Reached perfect 1.00 scores across all target species (setosa, versicolor, virginica), demonstrating a 0% error rate on the evaluation set.
Developed by Ansa for DecodeLabs Artificial Intelligence Internship Track (Batch 2026) 🚀
