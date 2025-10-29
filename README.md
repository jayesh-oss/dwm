# 🧠 Data Warehouse & Mining (DWM)

This project demonstrates key concepts of **Data Warehousing and Data Mining**, including **ETL operations, preprocessing, and machine learning algorithms** such as classification, clustering, association mining, and PageRank.

---

## 📁 **Project Structure**

```
dwm/
│
├── 1) data_warehouse_construction.sql      → SQL script for creating data warehouse schema
├── 2) ETL_operstion.sql                    → Extract, Transform, Load operations
├── 3) data_preprocessing.py                → Data cleaning & transformation
├── 4) classification_algo.py               → Classification algorithms (e.g., Decision Tree, Naive Bayes)
├── 5) clustering_algo.py                   → Clustering algorithms (e.g., K-Means, Hierarchical)
├── 6) association_mining_algo.py           → Association rule mining (Apriori / FP-Growth)
├── 7) page_rank_algo.py                    → PageRank algorithm implementation
├── 8) htts_algo.py                         → Example algorithm (check for typo: maybe “https_algo.py”)
└── README.md                               → Documentation file (this file)
```

---

## ⚙️ **Requirements**

Make sure you have the following installed:

- **Python 3.8+**
- **MySQL / PostgreSQL** (for SQL scripts)
- **Required Python libraries:**
  ```bash
  pip install pandas numpy scikit-learn matplotlib networkx
  ```

---

## 🚀 **How to Run**

### 🔹 1. Data Warehouse Construction
Run the SQL file to create database tables:
```sql
SOURCE data_warehouse_construction.sql;
```

### 🔹 2. ETL (Extract, Transform, Load)
Execute the ETL SQL script:
```sql
SOURCE ETL_operstion.sql;
```

### 🔹 3. Data Preprocessing
Clean and prepare data:
```bash
python data_preprocessing.py
```

### 🔹 4. Classification Algorithms
Run classification models:
```bash
python classification_algo.py
```
👉 Includes models like **Decision Tree**, **Naive Bayes**, or **KNN**.

### 🔹 5. Clustering Algorithms
Perform unsupervised learning:
```bash
python clustering_algo.py
```
👉 Includes **K-Means** and **Hierarchical Clustering**.

### 🔹 6. Association Mining
Generate association rules:
```bash
python association_mining_algo.py
```
👉 Example output: Support, Confidence, and Lift values.

### 🔹 7. PageRank Algorithm
Run the PageRank implementation:
```bash
python page_rank_algo.py
```

---

## 🧩 **Project Goals**

- Understand **Data Warehouse** design and ETL process  
- Perform **Data Mining** tasks using Python  
- Apply **ML algorithms** for classification and clustering  
- Implement **PageRank** and **Association Mining** from scratch  

---

## 📚 **Future Enhancements**

- Add **GUI** for visualization  
- Integrate **real datasets (CSV/SQL)**  
- Include **performance comparison** between algorithms  
- Improve **data preprocessing automation**

---

## 👨‍💻 **Author**

**Jayesh Wable**  
📘 GitHub: [jayesh-oss](https://github.com/jayesh-oss)
