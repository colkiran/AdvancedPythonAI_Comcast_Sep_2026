# Data Collection
import pandas as pd

data = {
    "Age": [25, 35, 45, 29, 50, 41, 23, 38, 52, 31,
            28, 46, 36, 40, 26, 55, 33, 48, 30, 43],

    "Income": [30000, 60000, 90000, 40000, 100000, 75000,
               25000, 65000, 120000, 55000, 35000, 85000,
               70000, 80000, 28000, 110000, 50000, 95000,
               45000, 72000],

    "Credit_Score": [620, 720, 780, 650, 800, 740, 580, 710,
                     810, 690, 630, 760, 730, 750, 590, 820,
                     680, 790, 640, 700],

    "Loan_Amount": [200000, 300000, 400000, 250000, 500000,
                    350000, 150000, 300000, 600000, 250000,
                    200000, 450000, 300000, 400000, 180000,
                    550000, 280000, 450000, 220000, 350000],

    "Loan_Term": [5, 10, 15, 5, 20, 15, 5, 10, 20, 10,
                  5, 15, 10, 15, 5, 20, 10, 15, 5, 10],

    "Existing_Loans": [2, 1, 0, 2, 0, 1, 3, 1, 0, 2,
                       2, 0, 1, 0, 3, 0, 1, 0, 2, 1],

    "Employment": ["Self", "Salaried", "Salaried", "Self",
                   "Salaried", "Salaried", "Self", "Salaried",
                   "Salaried", "Self", "Self", "Salaried",
                   "Salaried", "Salaried", "Self", "Salaried",
                   "Salaried", "Salaried", "Self", "Salaried"],

    "Dependents": [2, 1, 0, 3, 0, 2, 2, 1, 0, 2,
                   3, 1, 2, 0, 2, 0, 1, 0, 3, 1],

    "Loan_Status": [0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
                    0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
print(df)

# Data Processing and Cleaning
print("Total Null Values :", df.isnull().sum())

# we can fill the missing values with the medians
numeric_columns = [
    "Age", "Income", "Credit_Score", "Loan_Amount", "Loan_Term", "Existing_Loan", "Dependents" ]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

df['Employment'] = df["Employment"].fillna(df["Employment"].mode()[0])

# check for duplicates
print("Duplicate Rows :", df.duplicated().sum())
