# 🏦 AI Customer Churn Prediction Dashboard

An end-to-end **Deep Learning + Data Science project** that predicts whether a bank customer will leave the bank using an **Artificial Neural Network (ANN)** and provides **interactive analytics through a Streamlit dashboard**.

This project demonstrates a **production-style machine learning workflow** including data preprocessing, model training, explainable analytics, and a web-based prediction interface.

---

# 📌 Project Overview

Customer churn is a major problem in banking and telecom industries. Companies lose revenue when customers leave their services.

This project solves that problem by:

* Predicting **customer churn probability**
* Visualizing **churn patterns**
* Providing an **interactive dashboard**
* Allowing **real-time predictions**

The model is built using the deep learning framework **TensorFlow** and deployed with **Streamlit**.

---

# 🚀 Features

### 🔹 Machine Learning Model

* Artificial Neural Network (ANN)
* Dropout regularization
* Batch normalization
* Early stopping

### 🔹 Interactive Dashboard

* Customer churn rate
* Churn distribution by country
* Churn by gender
* Age vs churn analysis
* Balance vs churn insights

### 🔹 Prediction System

* Enter customer information
* Predict churn probability
* Risk classification (Low / Medium / High)

---

# 📂 Project Structure

```
churn_ann_project
│
├── app.py                # Streamlit dashboard
├── train_model.py        # ANN model training script
├── model.h5              # Trained neural network
├── scaler.pkl            # Feature scaler
├── Churn_Modelling.csv   # Dataset
└── requirements.txt      # Project dependencies
```

---

# 📊 Dataset Information

Dataset contains **bank customer information** including:

| Feature         | Description             |
| --------------- | ----------------------- |
| CreditScore     | Customer credit score   |
| Geography       | Customer country        |
| Gender          | Male / Female           |
| Age             | Customer age            |
| Tenure          | Years with bank         |
| Balance         | Bank balance            |
| NumOfProducts   | Number of bank products |
| HasCrCard       | Credit card status      |
| IsActiveMember  | Activity status         |
| EstimatedSalary | Customer salary         |
| Exited          | Target variable (Churn) |

Target:

```
Exited
0 → Customer stays
1 → Customer leaves
```

---

# 🧠 Model Architecture

```
Input Layer (11 features)
        ↓
Dense Layer (64 neurons) + ReLU
        ↓
Batch Normalization
        ↓
Dropout (0.3)
        ↓
Dense Layer (32 neurons) + ReLU
        ↓
Batch Normalization
        ↓
Dropout (0.3)
        ↓
Dense Layer (16 neurons)
        ↓
Output Layer (Sigmoid)
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/churn-ann-dashboard.git
```

Navigate into the project

```
cd churn-ann-dashboard
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Train the Model

Run the training script:

```
python train_model.py
```

This will generate:

```
model.h5
scaler.pkl
```

---

# 🖥 Run the Dashboard

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser.

---

# 📈 Dashboard Preview

The dashboard includes:

* Churn overview metrics
* Customer churn visualizations
* Interactive prediction interface

Users can input customer details and instantly get churn predictions.

---

# 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* **TensorFlow**
* **Streamlit**
* Plotly
* Matplotlib

---

# 🎯 Future Improvements

Possible enhancements:

* Explainable AI using SHAP
* Model comparison (XGBoost vs ANN)
* Customer segmentation using clustering
* Cloud deployment (AWS / Docker)
* Real-time API integration

---

# 👨‍💻 Author

B.Tech Computer Science Graduate
Aspiring Data Scientist

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
