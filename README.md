# Customer Support AI System

# 🎫 AI Incident Management & Service Desk Assistant

An intelligent workflow assistant built with Python, FastAPI, and Streamlit. This system utilizes a machine learning model to analyze service desk ticket descriptions and predict key metrics, streamlining incident management and queue triaging.

## 📁 Project Structure

```text
├── api/                  # FastAPI backend serving the ML model
│   └── main.py           # API endpoints and logic
├── app/                  # Streamlit frontend UI
│   └── app.py            # Web interface for user input
├── data/                 # Contains datasets used in training the model (.csv files)
│   └── SaaS_Tech_data.csv
│   └── faq_saas.csv
├── models/               # Contains the trained ML model (.pkl files)
│   └── saas_category_model.py
│   └── saas_resolution_model.py
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ✨ Features
- **Predictive Ticket Triaging:** Analyzes textual incident descriptions using scikit-learn to forecast resolution metrics.
- **REST API Backend:** Fast, robust, and asynchronous backend built with FastAPI to serve predictions.
- **Interactive Web UI:** User-friendly frontend built with Streamlit for manual ticket entry and evaluation.
- **Decoupled Architecture:** Clean separation of concerns between the frontend user interface and the backend ML processing.

## 🚀 Local Setup Instructions

To run this project locally, please follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/omarilzz/Customer-Support-AI-System.git
cd Customer-Support-AI-System
```

### 2. Install dependencies
*(Optional but recommended: Create and activate a virtual environment first)*
```bash
pip install -r requirements.txt
```

### 3. Start the Backend API (FastAPI)
Open a terminal and run the following command to start the API server on `localhost:8000`:
```bash
uvicorn api.main:app --reload
```
*Tip: Interactive API documentation automatically generates at `http://127.0.0.1:8000/docs`*

### 4. Start the Frontend UI (Streamlit)
Open a **second** terminal window and run the Streamlit application:
```bash
streamlit run app/app.py
```
*The Streamlit web app will open in your default browser at `http://localhost:8501`*

---
*Developed for efficient incident handling and advanced support queue analytics.*
