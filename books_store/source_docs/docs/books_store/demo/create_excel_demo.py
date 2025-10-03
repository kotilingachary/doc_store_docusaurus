#!/usr/bin/env python3
import csv
import sys

# Convert CSV to Excel-like format for demo
csv_content = """name,author,price
"Kotlin in Action","Dmitry Jemerov",45.99
"Learning Python","Mark Lutz",59.99
"JavaScript: The Good Parts","Douglas Crockford",29.99"""

# Since we don't have pandas/openpyxl, let's create a properly formatted CSV that demonstrates Excel compatibility
with open('excel_demo_books.csv', 'w', newline='') as f:
    f.write(csv_content)

print("Excel-compatible CSV file created: excel_demo_books.csv")