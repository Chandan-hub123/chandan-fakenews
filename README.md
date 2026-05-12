Fake News Prediction System

Overview

The **Fake News Prediction System** is a Machine Learning mini project that classifies news content as **REAL** or **FAKE** using Natural Language Processing (NLP) techniques.

This project helps in detecting misinformation and understanding how ML models can be applied to text classification problems.

---

 Objectives

* Predict whether a news article is **Real or Fake**
* Reduce misinformation spread
* Learn practical implementation of NLP & ML

---

 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLP (TF-IDF Vectorization)

---

 Project Structure

```
Fake-news-prediction-system/
│── data/
│   └── news.csv
│── model/
│   └── model.pkl
│── train.py
│── predict.py
│── main.py
│── README.md
```

---

 Working Process

1. Load dataset with news text
2. Clean and preprocess the data
3. Convert text into numerical features using TF-IDF
4. Train model using Machine Learning algorithm
5. Predict news as REAL or FAKE

---

 How to Run

 1. Install Requirements

```
pip install pandas numpy scikit-learn
```

2. Train Model

```
python train.py
```

3. Run Project

```
python main.py
```

---

 Example

**Input:**

```
India successfully launched Chandrayaan-3 mission to the Moon to study the lunar surface and demonstrate safe landing technology for future space missions..
```

**Output:**

```
 Real News
```

---

**Input:**

```
NASA confirmed that aliens are living inside the Moon and are secretly communicating with selected humans on Earth.
```

**Output:**


 Fake News

Author
 Fake News Prediction System- poornima M
