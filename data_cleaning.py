import pandas as pd

# Step 1: Read the dataset
df = pd.read_csv('input.csv')
print("Original data:")
print(df.head())  # shows first few rows

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Fill missing Age values with average (mean)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Step 4: Convert 'Date_of_Joining' to proper date format
df['Date_of_Joining'] = pd.to_datetime(df['Date_of_Joining'], errors='coerce')

# Step 5: Save cleaned data into new file
df.to_csv('cleaned_output.csv', index=False)
print(df)

print("\n✅ Cleaning completed! Cleaned data saved to 'cleaned_output.csv'")