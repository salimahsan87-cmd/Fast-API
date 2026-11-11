# 🚀 Machine Learning & FastAPI Projects

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

> 💡 Building Machine Learning models and turning them into practical applications using FastAPI.

---

## 👨‍💻 About This Repository
## 🙋‍♂️ Independent Project Development

All projects in this repository have been independently developed by me, from initial dataset acquisition to final API implementation.

I personally handled the complete development lifecycle of each project, including:

- 📥 Finding and downloading datasets.
- 🔍 Data exploration and analysis.
- 🧹 Data cleaning and preprocessing.
- ⚙️ Feature engineering and preparation.
- 🧠 Designing, building, and training Machine Learning and Deep Learning models.
- 📈 Evaluating model performance.
- 💾 Saving and uploading trained models and datasets to GitHub.
- ⚡ Developing FastAPI applications.
- 🔗 Integrating trained models into REST APIs.
- 🧪 Testing prediction endpoints and validating outputs.

**These projects represent my own practical work, independent implementation, and hands-on experience in developing end-to-end Machine Learning applications.**

Welcome to my Machine Learning and FastAPI projects repository!

This repository contains practical Machine Learning and Deep Learning projects developed using Python.

My goal is to build complete AI applications, covering the entire development process:

- 📊 Dataset collection and exploration
- 🧹 Data preprocessing and feature engineering
- 🧠 Machine Learning and Deep Learning model development
- 📈 Model training and evaluation
- 💾 Saving and uploading trained models
- ⚡ Integrating models with FastAPI
- 🌐 Building REST APIs for real-time predictions

Unlike simple notebook experiments, these projects also include trained models, datasets, and API implementations.

---

# 📂 Projects

## 🩺 1. Diabetes Prediction API

A Machine Learning application designed to predict diabetes risk based on patient health-related information.

### ✨ Features

- 📊 Dataset exploration and preprocessing
- 🧹 Data cleaning and feature preparation
- 🧠 Deep Learning model development using TensorFlow/Keras
- 📈 Model training and evaluation
- 💾 Saving and uploading the trained model
- ⚡ FastAPI integration
- 🛡️ Input validation using Pydantic
- 🔗 REST API prediction endpoints

### 🛠️ Technologies

`Python` `TensorFlow` `Keras` `Pandas` `NumPy` `FastAPI` `Pydantic`

### 📁 Project Files

- `Diabetes-1.ipynb` — Data analysis, preprocessing, and model development.
- `fastapi_diabetes.py` — FastAPI application.
- `diabetes_kaggle.h5` — Trained Deep Learning model.
- Dataset files — Data used for model development and evaluation.

---

## 🏠 2. Canadian House Price Prediction API

A Deep Learning application designed to predict Canadian housing benchmark prices using property-related and market information.

### ✨ Features

- 📊 Dataset exploration and analysis
- 🧹 Data preprocessing and feature engineering
- 🏷️ Target Encoding for categorical features
- 📐 Feature scaling and transformation
- 🔍 Missing-value handling and missing indicators
- 🧠 Deep Learning model development
- 📈 Model training and evaluation
- 💾 Saving trained models and preprocessing objects
- 🏘️ Support for multiple property categories
- ⚡ FastAPI integration for housing price predictions

### 🛠️ Technologies

`Python` `TensorFlow` `Keras` `Scikit-learn` `Pandas` `NumPy` `Joblib` `FastAPI`

### 📁 Project Files

- `Price_Home_Canada-1.ipynb` — Data analysis, preprocessing, and model development.
- `fastapi_price_home.py` — FastAPI application.
- Model files — Trained Deep Learning model.
- Preprocessing files — Saved encoders and scalers.
- Dataset files — Data used for training and evaluation.

---

# 📦 Datasets & Trained Models

One of the important aspects of this repository is that the datasets and trained models are included alongside the source code.

### 📊 Datasets

- The datasets used in the projects have been uploaded to this repository.
- Data preparation and preprocessing steps are documented in the notebooks.
- The datasets allow developers to inspect the data used during model development.

### 🧠 Trained Models

- The trained Machine Learning and Deep Learning models are uploaded to the repository.
- Saved preprocessing objects are included where required.
- The FastAPI applications load the trained models directly for prediction.
- There is no need to retrain the models just to run the prediction APIs.

### 🔄 Complete Machine Learning Workflow

```text
📊 Dataset Collection
        |
        ▼
🔍 Data Exploration
        |
        ▼
🧹 Data Preprocessing
        |
        ▼
⚙️ Feature Engineering
        |
        ▼
🧠 Model Development & Training
        |
        ▼
📈 Model Evaluation
        |
        ▼
💾 Save & Upload Trained Model
        |
        ▼
⚡ FastAPI Integration
        |
        ▼
🌐 Prediction API
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Programming Language |
| 🧠 TensorFlow / Keras | Deep Learning |
| 📊 Scikit-learn | Machine Learning & Preprocessing |
| 🐼 Pandas | Data Manipulation |
| 🔢 NumPy | Numerical Computing |
| ⚡ FastAPI | API Development |
| 🛡️ Pydantic | Input Validation |
| 💾 Joblib | Saving Preprocessing Objects |
| 📓 Jupyter Notebook | Data Analysis & Experiments |
| 🔧 Git & GitHub | Version Control |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/salimahsan87-cmd/Fast-API.git
```

## 2️⃣ Navigate to the Repository

```bash
cd Fast-API
```

## 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn tensorflow pandas numpy scikit-learn joblib
```

## 4️⃣ Run the Diabetes Prediction API

```bash
uvicorn fastapi_diabetes:app --reload
```

## 5️⃣ Run the House Price Prediction API

```bash
uvicorn fastapi_price_home:app --reload
```

## 6️⃣ Explore API Documentation

After starting an API, open the following address in your browser:

🔗 http://127.0.0.1:8000/docs

You can use Swagger UI to explore endpoints and send prediction requests.

---

# 🎯 What I Have Learned

Through developing these projects, I have gained practical experience in:

- 🧠 Building Machine Learning and Deep Learning models.
- 📊 Working with datasets and performing exploratory data analysis.
- 🧹 Data preprocessing and feature engineering.
- 📈 Evaluating model performance.
- 💾 Saving and loading trained models.
- 🔌 Integrating ML models into backend applications.
- ⚡ Developing REST APIs using FastAPI.
- 🛡️ Validating API inputs using Pydantic.
- 🔄 Connecting data processing pipelines with prediction services.

---

# 🔮 Future Improvements

I am continuously working on improving my projects and expanding my technical skills.

Planned improvements include:

- 🧪 Automated testing using Pytest.
- 🐳 Docker containerization.
- 🔄 CI/CD integration.
- ☁️ Cloud deployment.
- 📊 Model monitoring and performance tracking.
- 🏗️ Improving project architecture and code modularity.

---

# 👨‍💻 About Me

**Ehsan Salim**

🚀 Machine Learning & AI Developer

Interested in Artificial Intelligence, Machine Learning, Deep Learning, Data Science, and building practical AI-powered applications.

🔗 **GitHub:** [salimahsan87-cmd](https://github.com/salimahsan87-cmd)

---

<p align="center">

⭐ If you find this repository interesting, consider giving it a star!

**💡 Learn. Build. Improve. Repeat. 🚀**

</p>
