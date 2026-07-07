import pandas as pd

df = pd.read_csv("Data processing/retail_sales_dataset_100_rows.csv")

# First & Last Rows
print(df.head())
print()
print(df.tail())
print()

# Shape
print(df.shape)
print()

# Index
print(df.index)
print()

# Columns
print(df.columns)
print()

# Data Types
print(df.dtypes)
print()

# Information
df.info()
print()

# Statistical Summary
print(df.describe())
print()

# Missing Values
print(df.isnull().sum())
print()

# Duplicate Rows
print(df.duplicated().sum())
print()

# Size and Dimensions
print(df.size)
print(df.ndim)
print()

# Random Rows
print(df.sample(5))
print()

# Maximum, Minimum, Mean
print(df["Sales"].max())
print(df["Sales"].min())
print(df["Sales"].mean())
print()


# Unique Products
print(df["Product"].unique())
print()


print(df["Product"].nunique())
print()

# Sort by Sales
print(df.sort_values(by="Sales", ascending=False))
print()

# Filter Electronics
print(df[df["Category"] == "Electronics"])
print()

# Group By
print(df.groupby("Category")["Sales"].sum())
print()
print(df.groupby("Category")["Sales"].mean())
print()
# Value Counts
print(df["Category"].value_counts())
print()