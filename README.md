# 🧹 Data Cleaning Project — SyntecxHub Internship Task

### 📋 Project Overview
This project focuses on *data cleaning using Python (pandas)*.  
The goal is to read a dataset, remove duplicate records, handle missing values, correct data formats, and save a cleaned dataset for further analysis.

---

### 📂 Files in this Project
| File Name | Description |
|------------|--------------|
| input.csv | Raw dataset before cleaning |
| data_cleaning.py | Python code used to clean the data |
| cleaned_output.csv | Final cleaned dataset |
| README.md | Documentation for this project |

---

### ⚙ Software and Tools Required
- Python 3.x  
- Pandas library  
- Visual Studio Code or Jupyter Notebook  
- CSV file (dataset)

---

### 🧠 Steps Performed
1. Import necessary libraries (pandas).
2. Load dataset from input.csv.
3. Check for missing values and fill them with suitable values.
4. Remove duplicate rows.
5. Standardize date formats.
6. Save cleaned data to cleaned_output.csv.
7. Print final cleaned data.

---

### 📊 Example Raw Dataset (Before Cleaning)

| Name | Age | Gender | City | Date_of_Joining | Department | Salary |
|------|-----|---------|------|----------------|-------------|--------|
| Ravi | 25 | M | Hyderabad | 2021-02-15 | IT | 55000 |
| Anjali |  | F | Delhi | 2022-08-05 | Sales | 50000 |
| Kiran | 30 | M | Hyderabad | 2021/03/15 | IT | 60000 |
| Priya | 29 | F | Chennai | 2020-11-10 | HR | 48000 |
| Ravi | 25 | M | Hyderabad | 2021-02-15 | IT | 55000 |

---

### ✅ Cleaned Dataset (After Cleaning)

| Name | Age | Gender | City | Date_of_Joining | Department | Salary |
|------|-----|---------|------|----------------|-------------|--------|
| Ravi | 25 | M | Hyderabad | 2021-02-15 | IT | 55000 |
| Anjali | 28 | F | Delhi | 2022-08-05 | Sales | 50000 |
| Kiran | 30 | M | Hyderabad | 2021-03-15 | IT | 60000 |
| Priya | 29 | F | Chennai | 2020-11-10 | HR | 48000 |

---

### 💻 How to Run the Project

1. Open VS Code.
2. Save your dataset as input.csv in the same folder as the Python file.
3. Open the terminal and run:
   ```bash
   pip install pandas
   python data_cleaning.py
---
## Conclusion
This project shows how to perform data cleaning efficiently using Python and Pandas.

---
## 👨‍💻 Author

Name: Kukkapalli Satish Babu

Internship: SyntecxHub - Data Science

Task: Data Cleaning Using Python
