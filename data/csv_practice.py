# ISM2411 Lab 12
# Ela Kekec

import csv
from datetime import datetime


# ---Exercise 1---
# sales.csv is located inside the data folder.


# ---Exercise 2---
print("Exercise 2: Raw Rows")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
