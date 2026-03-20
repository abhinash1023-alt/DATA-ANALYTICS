import pandas as pd

# 1. Create Data 
data = {
    "Name": ["Abhi", "Akshay", "Gupta", "Priya", "Kiran"],
    
    "Age": [20, 21, 22, 43, 12],

    "Marks": [85, 45, 67, 78, 87],

    "Dept": ["CSE", "IT", "CSE", "IT", "CSE"]

}

df = pd.DataFrame(data)

print("=== Original Data ===")
print(df)

# 2. Basic Info
print("\n=== Info ===")
print(df.info())

print("\n=== Describe ===")
print(df.describe())

# 3. Select Column
print("\n=== Select Name Column ===")
print(df["Name"])

print("\n=== Select Name & Marks ===")
print(df[["Name", "Marks"]])

# 4. Filtering
print("\n=== Marks > 80 ===")
print(df[df["Marks"] > 80])

# 5. Add Result Column
df["Result"] = "Pass"

# 6. Create Grade Column

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"
   
df["Grade"] = df["Marks"].apply(grade)

print("\n=== After Adding Columns ===")
print(df)

# 7. Update Value
df.loc[0, "Marks"] = 95

# 8. Sorting
print("\n=== Sorted by Marks ===")
print(df.sort_values(by="Marks", ascending=False))

# 9. Group By
print("\n=== Dept Wise Avg Marks ===")
print(df.groupby("Dept")["Marks"].mean())

# 10. Save CSV
df.to_csv("output.csv", index=False)

# 11. Read CSV
df2 = pd.read_csv("output.csv")

print("\n=== Read from CSV ===")
print(df2.head())

# 12. Handle Missing Values (example)
df2.fillna(0, inplace=True)

print("\n=== Final Data ===")
print(df2)