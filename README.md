# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the analysis and models for the B5W3 project, focusing on insurance risk analytics for AlphaCare Insurance Solutions (ACIS). The primary goal is to analyze historical insurance claim data to identify low-risk segments and build predictive models to optimize premium pricing.

## Business Objective

AlphaCare Insurance Solutions (ACIS) aims to leverage data analytics to refine its marketing and pricing strategies for car insurance in South Africa. This project involves:
1.  **Exploratory Data Analysis (EDA)** to understand data distributions and initial patterns.
2.  **A/B Hypothesis Testing** to statistically validate differences in risk across customer segments.
3.  **Predictive Modeling** to predict claim amounts and optimize premiums for different customer profiles.

## Project Structure

The repository is organized as follows:
```
.
├── data/               # Raw and processed data (tracked by DVC)
├── notebooks/          # Jupyter notebooks for exploration and analysis
│   ├── 01_EDA.ipynb
│   └── 02_Hypothesis_Testing.ipynb
├── src/                # Source code for data processing, modeling, and utilities
├── reports/            # Project reports and presentations
├── .github/workflows/  # CI/CD pipeline configuration
├── .gitignore          # Files to be ignored by Git
└── README.md           # This file
```

## Setup and Installation

To get the project running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/acis-insurance-risk-analytics.git
    cd acis-insurance-risk-analytics
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

- **Exploratory Data Analysis:** Open and run the notebooks in the `notebooks/` directory, starting with `01_EDA.ipynb`.
- **Data Versioning:** Data is versioned using DVC. To pull the data, run `dvc pull`.

## Key Tasks Overview

- **Task 1:** EDA & Stats
- **Task 2:** Data Version Control (DVC) Setup
- **Task 3:** A/B Hypothesis Testing
- **Task 4:** Predictive Modeling
