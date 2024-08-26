# WHO Data Analysis, Modeling, and Deployment

## Overview

This project focuses on the analysis, modeling, and deployment of a dataset from the World Health Organization (WHO). The key steps include:

- **Exploratory Data Analysis (EDA)** to understand data structure and relationships.
- **Modeling** with various machine learning algorithms.
- **Deployment** of the best-performing model using Streamlit.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Dataset

The dataset used is from WHO, containing various health indicators. The data was cleaned, visualized, and prepared for modeling.
The link[https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who]

## EDA

Conducted extensive EDA to uncover patterns, correlations, and data distributions. The data was preprocessed, and missing values were handled appropriately.

## Modeling

Several models were built and evaluated, including:

- **Linear Regression**
- **Ridge**
- **ElasticNet**
- **Lasso**
- **SGDRegressor**
- **Decision Trees**
- **Random Forests**
- **Support Vector Machines (SVM)**
- **ExtraTree** (Best model)
- **Stacking**
- 

The ExtraTree model outperformed others based on evaluation metrics.

## Deployment

The best model was deployed using Streamlit. The app provides an interactive interface for real-time predictions.
(The link) [https://jejd7ldj4u3d2dzv99u7yk.streamlit.app/]

## Results

- **Best Model**: ExtraTree
- **Metrics**: (on test set 0.8955 for MAE, 0.9763 for r2).

## Usage

To run the app locally:

```bash
streamlit run Web.py
