# 🐍 Python – Complete Introduction and Basics for AI/ML

This repository contains a comprehensive guide and examples for learning **Python**, focusing on its applications in **Artificial Intelligence (AI)** and **Machine Learning (ML)**. It includes explanations, code snippets, and beginner-friendly examples covering everything from basic syntax to real-world model building using `scikit-learn`.

## 📚 Table of Contents
1. What is Python?
2. Why Python for AI/ML?
3. How is Python Different?
4. Applications of Python
5. Arithmetic and Variables
6. Comments & Variables
7. CSV to Python (Pandas)
8. Functions
9. Data Types
10. Conditional Statements
11. Lists
12. Introduction to Machine Learning
13. Building a Model (Decision Tree & Random Forest)
14. Project Flow
15. Requirements
16. How to Run
17. License

## 🧠 What is Python?
Python is a **high-level, interpreted** programming language known for its **simple and readable syntax**.

- Created by **Guido van Rossum** (1991)
- Dynamically typed – no explicit variable types
- Uses **indentation instead of braces `{}`**
- Cross-platform: Works on Windows, Linux, macOS
- Fewer lines of code than C++ or Java

## 🤖 Why Python for AI/ML?
- Massive library ecosystem: `NumPy`, `Pandas`, `TensorFlow`, `PyTorch`
- Clean syntax → focus on **logic**, not boilerplate
- Excellent community support
- Perfect for **prototyping** and **experimentation**
- Works seamlessly with **Jupyter Notebooks**

## ⚖️ How is Python Different?
| Feature | Python | Java/C++ |
|----------|---------|-----------|
| Syntax | Indentation | Braces `{}` |
| Typing | Dynamic | Static |
| Code Length | Shorter | Verbose |
| Libraries | Huge for AI/ML | Limited |
| Platform | Cross-Platform | Platform-dependent |

## 🌍 Applications of Python
- **AI & Machine Learning** → Chatbots, Predictive Models  
- **Data Science & Analytics** → Visualization, Statistics  
- **Web Development** → Django, Flask  
- **Automation & Scripting** → Bots, Testing  
- **Game Development** → Pygame, Panda3D  
- **IoT & Robotics** → Raspberry Pi  
- **Cybersecurity** → Malware Analysis, Scripts  

## ➕ Arithmetic and Variables
```python
print("Hello, world!")
a, b = 5, 3
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
```

Use **PEMDAS** for operation order:  
`Parentheses → Exponents → Multiplication/Division → Addition/Subtraction`

## 💬 Comments & Variables
```python
# Multiply 3 by 2
print(3 * 2)

test_var = 4 + 5
print(test_var)
```

## 🧾 CSV to Python (Pandas)
```python
import pandas as pd
titanic_data = pd.read_csv("train.csv")
titanic_data.head(3)
```

## ⚙️ Functions
```python
def add_three(x):
    return x + 3
```

Example – calculate paint cost:
```python
import math

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    return cost_per_gallon * gallons_to_buy
```

## 🔢 Data Types
| Type | Example | Description |
|------|----------|-------------|
| `int` | 14 | Integer |
| `float` | 3.14159 | Decimal number |
| `bool` | True / False | Logical values |
| `str` | "Hello" | Text |
| `list` | [1,2,3] | Sequence of elements |

## 🔁 Conditional Statements
```python
def evaluate_temp(temp):
    if temp > 38:
        return "Fever!"
    elif temp < 35:
        return "Low temperature."
    else:
        return "Normal temperature."
```

## 🌸 Lists
```python
flowers = ["rose", "lily", "orchid"]
print(flowers[0])          # rose
print(flowers[-1])         # orchid
flowers.append("sunflower")
print(len(flowers))        # 4
```

## 🤖 Introduction to Machine Learning
**Machine Learning (ML)** teaches computers to learn from data and improve performance automatically.

**Key steps:**
1. Load and clean data (`pandas`)
2. Split into **train/test**
3. Build model (`DecisionTree`, `RandomForest`)
4. Predict
5. Evaluate with **Mean Absolute Error (MAE)**

## 🧩 Building a Model (Decision Tree & Random Forest)
```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv("melb_data.csv")
data = data.dropna(axis=0)

# Target and features
y = data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[features]

# Split data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Decision Tree
dt_model = DecisionTreeRegressor(random_state=1)
dt_model.fit(train_X, train_y)
dt_mae = mean_absolute_error(val_y, dt_model.predict(val_X))

# Random Forest
rf_model = RandomForestRegressor(random_state=1, n_estimators=100)
rf_model.fit(train_X, train_y)
rf_mae = mean_absolute_error(val_y, rf_model.predict(val_X))
```

## 🔄 Project Flow
```
CSV → pandas DataFrame → Clean/Preprocess → Split → Train Model → Predict → Evaluate
```

## ⚙️ Requirements
```bash
pip install pandas scikit-learn numpy
```

## ▶️ How to Run
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python filename.py
```