# Customer Churn Prediction – Machine Learning Pipeline with FastAPI

## 🧾 Overview

This project is an end-to-end machine learning solution for predicting customer churn using a synthetic dataset. It includes data preprocessing, model training with various classifiers, explainability with SHAP, model deployment using **FastAPI**, and a simple web interface powered by HTML templates.

The final model is trained using **AdaBoost**, selected after evaluating multiple classification algorithms. The application is containerized via Docker and can be pulled directly from Docker Hub.

---

## 🚀 Project Goals

- Predict which customers are likely to churn  
- Analyze feature impact on churn using SHAP  
- Provide a lightweight API (FastAPI) for real-time predictions  
- Build a simple web interface (`form.html`) for interactive input  
- Deployable via Docker for consistent environment management

---

## 🔍 Models Evaluated

This project explored and compared the following classification models:

- Logistic Regression  
- Random Forest  
- XGBoost  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- CatBoost  
- ✅ **AdaBoost** *(used for final deployment and serialized as `customer_churn.pkl`)*

AdaBoost was selected due to its consistent performance across accuracy, precision, recall, and generalization.

---

## 🧾 Features Used

The model was trained on the following input features:

- `Tenure` – Number of months the customer has stayed  
- `MonthlyCharges` – Monthly bill amount  
- `ContractType` – Type of contract (Month-to-month, One year, Two year)  
- `UsageMetrics` – Total data/minutes used by the customer  
- `SupportTickets` – Number of support issues/tickets raised

---

## 📁 Repository Structure

```

Customer-Churn-Prediction/
│
├── template/
│   └── form.html              # HTML input form for FastAPI interface
│
├── src/
│   └── image.png              
│
├── customer_churn.pkl         # Serialized AdaBoost model
├── main.py                    # FastAPI application entry point
├── customer_chrn.ipynb        # Jupyter notebook (EDA → Modeling → SHAP)
├── mock_churn_dataset.csv     # Synthetic customer data
├── requirements.txt           # Python dependencies
└── Dockerfile                 # Container configuration

````

---

## 🧪 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/vignesh4u4u/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

Then visit: [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the form-based UI (mention your correct port number)
API docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 Docker Deployment Options

### 🐳 1. Build & Run Locally

```bash
docker build -t churn-fastapi-app .
docker run -p 8080:8000 churn-fastapi-app
```

Then open: [http://localhost:8080](http://localhost:8080)

### 🐳 2. Pull Public Docker Image

```bash
docker pull vick4s5s/churn-predictor:v.1
docker run -p 8080:8000 vick4s5s/churn-predictor:v.1
```

---

## 📊 SHAP Analysis

Feature importance was interpreted using SHAP:

* Customers with short tenure and flexible (month-to-month) contracts were more likely to churn.
* More support tickets indicated higher dissatisfaction and risk.


---

## 💼 Use Cases

* **Telecoms**: Prevent subscriber loss through churn prediction
* **SaaS Platforms**: Track and retain customers with early warning
* **Subscription Businesses**: Target high-risk users with special offers

---

## 📬 Contact

**Author**: Vignesh
**GitHub**: [https://github.com/vignesh4u4u/Customer-Churn-Prediction](https://github.com/vignesh4u4u/Customer-Churn-Prediction)
**Email**: [vickys9715@gmail.com](mailto:vickys9715@gmail.com)
**Docker Hub**: [vick4s5s/churn-predictor\:v.1](https://hub.docker.com/r/vick4s5s/churn-predictor)

---

## 📄 License

This project is licensed under the **MIT License**.

