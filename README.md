# 🏥 Insurance Premium Category Prediction

A full-stack Machine Learning web application that predicts an individual's **Insurance Premium Category** (**Low**, **Medium**, or **High**) based on health, lifestyle, and demographic information.

The application combines a trained Machine Learning model with a FastAPI backend and an interactive frontend to provide real-time insurance premium predictions.

---

## 🚀 Features

* Predicts insurance premium category (Low, Medium, High)
* Interactive and responsive frontend
* FastAPI-based REST API
* Machine Learning model integration
* Input validation using Pydantic
* Automatic feature engineering before prediction
* Serialized model using `pickle`

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

---

## 📊 Model Features

The prediction model uses engineered features including:

* BMI (Body Mass Index)
* Age Group
* Lifestyle Risk
* City Tier
* Annual Income
* Occupation

These features are processed through a Scikit-learn `Pipeline` with `ColumnTransformer` and a Random Forest Classifier.

---

## 📁 Project Structure

```text
Insurance-Premium-Prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── templates/
├── static/
├── README.md
└── ...
```

---
## 🚀 Live Demo

Frontend: https://insurance-premium-category-prediction-h89qz7jj6crorvlukw6nyn.streamlit.app/

Backend API Docs: https://insurance-premium-category-prediction-1.onrender.com/predict

## ▶️ Running the Project

1. Clone the repository.

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server.

```bash
uvicorn app:app --reload
```

4. Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## 📈 Model Performance

* Algorithm: Random Forest Classifier
* Feature Engineering: BMI, Age Group, Lifestyle Risk, City Tier
* Model Serialization: Pickle (`model.pkl`)
* Approximate Test Accuracy: **90%**

---

## 🙏 Credits

### Machine Learning Model

The machine learning model, feature engineering, model training, and evaluation were developed by **Kuldeep**.

### Application Development

The **FastAPI backend**, **API integration**, **frontend development**, and deployment of the machine learning model into a complete web application were developed by **Yuvraj Choudhary**.

---

## 📄 License

This project is intended for educational and learning purposes.
