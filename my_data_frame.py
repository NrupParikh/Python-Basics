# python3 -m pip install pandas

import pandas as pd

# Create DataFrame and save to CSV
data = [
    {"No": 1, "Name": "Amit", "Age": 30},
    {"No": 2, "Name": "Vijay", "Age": 25},
    {"No": 3, "Name": "Ravi", "Age": 35},
]

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Save to CSV
df.to_csv("people.csv", index=False)
print("Data saved to people.csv")
