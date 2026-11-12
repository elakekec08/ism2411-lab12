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

# ---Exercise 3---
print("\nExercise 3: Skip Header")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)


# ---Exercise 4---
print("\nExercise 4: Compute Totals")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")