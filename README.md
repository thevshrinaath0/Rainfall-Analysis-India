# 🌦️ India Rainfall Analysis & Prediction (2010–2024)

**A data-driven project analyzing and predicting rainfall patterns across Indian states from 2010 to 2024.**

---

## 📖 Overview

This project focuses on **analyzing rainfall trends across Indian states** using historical data (2010–2024) and building a **machine learning model** to understand rainfall deviation and predict future rainfall patterns.

It is designed with an **end-to-end MLOps-style workflow** — including **data fetching, preprocessing, exploratory data analysis (EDA), model training**, and **automated testing** — all streamlined through a `Makefile` and GitHub CI pipeline.

---

## 🧩 Project Structure

India-Rainfall-Analysis/
├── data/
│ ├── raw/ # Original rainfall datasets
│ ├── processed/ # Cleaned data after preprocessing
│
├── src/
│ ├── fetch_data.py # Fetches or loads rainfall data
│ ├── preprocess.py # Cleans and prepares data
│ ├── train_model.py # Trains regression model on rainfall data
│ ├── predict.py # (Optional) Generates predictions
│
├── tests/
│ ├── test_fetch_data.py # Tests for data fetching
│ ├── test_preprocess.py # Tests for preprocessing pipeline
│ ├── test_model.py # Tests for model training and validation
│
├── requirements.txt # Python dependencies
├── Makefile # Automates commands (install, test, lint, etc.)
├── .github/workflows/CI.yml # Continuous integration pipeline
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/india-rainfall-analysis.git
cd india-rainfall-analysis b
```
### 2️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # For Linux / macOS
# OR
.venv\Scripts\activate       # For Windows
```
### 3️⃣ Install Required Packages
```bash
make install
```

---
## 🚀 Running the Pipeline
### Fetch Raw Data
```bash
make fetch
```
### Preprocess Data
```bash
make preprocess
```
### Train Model
```bash
make train
```
### Run Tests
```bash
make test
```
---

## 🧠 Dataset Details

Column Name	Description
id	Unique record identifier
date	Observation date
state_code	Numeric code of the Indian state
state_name	Name of the Indian state
actual	Actual observed rainfall (in mm)
rfs	Rainfall so far in the season
normal	Normal rainfall expected for the period
deviation	% deviation of actual rainfall from normal
category	Rainfall classification (e.g., excess, normal, deficient)

Data Period: 2010 – 2024
Coverage: All Indian states and union territories
Source: IMD / open rainfall datasets (for project-based learning)

##🧩 Model Details

- Algorithm: Linear Regression (baseline model)
- Features Used:
  - rfs — Rainfall so far
  - normal — Normal rainfall
  - deviation — Rainfall deviation %
- Target Variable: actual — Actual rainfall observed
The model predicts actual rainfall based on seasonal rainfall and deviation data.

---

## 📊 Exploratory Data Analysis (EDA)

During EDA, we explored:

  - Yearly rainfall trends (2010–2024)

  - State-wise rainfall deviation

  - Distribution of actual rainfall

  - Correlation between rainfall variables

### Key Insights

  - States like Kerala and Assam show high seasonal variation.

  - Noticeable deviation growth post 2015, indicating climate shift patterns.

  - Northern and central India show inconsistent rainfall vs normal averages.

(Visualizations can be added later under /notebooks or /eda folder.)

---
## Testing & Code Quality

This project follows best coding practices using:

  - ✅ Pytest for unit testing

  - ✅ Pylint and Black for linting and formatting

  - ✅ CI/CD via GitHub Actions (.github/workflows/CI.yml)


### Run Checks Manually
  ```bash
make lint
make format
make test
```
