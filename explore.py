"""
ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
Author: Ahraya Dalaq
Run with: python explore.py

Self-Assessment
---------------
1. It checks every row against a condition (like "region is South"), 
gets True or False for each row and keeps only the rows that are True.
   

2. Single brackets return a Series. Double brackets return a dataframe 
that happens to have one column. It matters when the next step needs a dataframe, 
for example selecting several columns, merging, or saving with column headers. 
It also matters for methods that only work on one of the two types, like .unqiue() on a Series.
   

3. It's repeatable. The script reruns the same analysis on new or bigger data in seconds, 
with every step written down, instead of redoing clicks and formulas by hand.
   
"""

import pandas as pd

# Exercise 1: Load it
df = pd.read_csv('data/retail_sales.csv')
print("=== Exercise 1 ===")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2: Filter by region
south = df[df['region'] == 'South']
print("\n=== Exercise 2 ===")
print(len(south))
print(south.head())

# Exercise 3: Top 5 by revenue
top5 = df.sort_values('revenue', ascending=False).head(5)
print("\n=== Exercise 3 ===")
print(top5)

# Exercise 4: Two-condition filter
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print("\n=== Exercise 4 ===")
print(len(big_south))
print(big_south.head())

# Exercise 5: A new column
df['per_unit'] = df['revenue'] / df['quantity']
print("\n=== Exercise 5 ===")
print(df.head())
print(df['per_unit'].mean())

# Exercise 6: Unique values
print("\n=== Exercise 6 ===")
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7: Select columns
subset = df[['region', 'product', 'revenue']]
print("\n=== Exercise 7 ===")
print(subset.shape)

# Exercise 8: Save
df.to_csv('data/explored.csv', index=False)
print("\n=== Exercise 8 ===")
print("Saved data/explored.csv")