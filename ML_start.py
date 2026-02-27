# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 21:18:17 2026

@author: Anoop Kote
"""

"""
ml_start.py
-----------
The first ML script.
Reads your CSV data and learns to classify images
as BRIGHT or DARK based on pixel values.

That's it. Simple. This is how all ML starts.

Install first:
    pip install scikit-learn pandas

Usage:
    python ml_start.py
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

folder = input("Paste your image folder path: ").strip().strip('"')

csv_path = os.path.join(folder, "brightness.csv")

if not os.path.exists(csv_path):
    print("No brightness.csv found. Run brightness_batch.py first.")
    input("Press Enter to close.")
    exit()

# Load the data
df = pd.read_csv(csv_path)

print(f"\n  Loaded {len(df)} images worth of data")
print(f"\n  Sample:")
print(df.head())

# X = what the machine looks at (brightness number)
# y = what we want it to learn (dark or bright)
X = df[["avg_brightness"]]
y = df["assessment"]

if len(df) < 5:
    print("\n  Need more images. Run brightness_batch.py on a bigger folder first.")
    input("Press Enter to close.")
    exit()

# Split into training data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test it
predictions = model.predict(X_test)
accuracy    = accuracy_score(y_test, predictions)

print(f"\n  {'='*40}")
print(f"  Training images:  {len(X_train)}")
print(f"  Testing images:   {len(X_test)}")
print(f"  Accuracy:         {round(accuracy * 100, 1)}%")
print(f"  {'='*40}")

# Let it predict a new value
print(f"\n  Test it yourself:")
val = input("  Enter a brightness value (0-255): ").strip()
result = model.predict([[float(val)]])
print(f"\n  Model says: {result[0]}")

input("\nPress Enter to close.")