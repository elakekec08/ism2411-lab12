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

# ---Exercise 5---
print("\nExercise 5: Filter and Write")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                cleaned_count += 1

print(f"Original Rows: {original_count}")
print(f"Cleaned Rows: {cleaned_count}")


# ---Exercise 6---
print("\nExercise 6: DictReader")

# csv.reader is useful when working with simple files using column positions.
# DictReader is better when using column names because the code is easier to read.

dict_total = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        dict_total += total

        print(f"{product}: ${total:.2f}")

print(f"Total Revenue: ${dict_total:.2f}")