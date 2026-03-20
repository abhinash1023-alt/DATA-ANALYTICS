import pandas as pd

# --------- Basic DataFrame ---------
df = pd.DataFrame([1,2,3], columns=['column_name'])
print(df)

data = {
    'Name': ['Abinash', 'Arti', 'Anushka', 'Raja', 'Priyanshu', 'Jayant'],
    'Age':  [12,22,33,45,55,65],
    'Salary' : [1000, 1200, 1300, 1400, 1500, 1600]
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.columns)

# ✅ Correct rename
print(df.rename(columns={'Salary': 'payment'}))
df.rename(columns={'Salary': 'payment'}, inplace=True)

print(df)

print(df.describe())


# --------- Company Data ---------
data = {
    'name': ['abi', 'raja', 'priyam', 'priyanshu', 'nadeem', 'gupta', 'yadav', 'riya', 'chintu', 'jayant', 'priya', 'pushkar', 'rohan', 'sourab', 'akshay'],
    'employee_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'age': [28, 35, 42, 31, 26, 38, 45, 33, 29, 41, 36, 39, 27, 44, 32],
    'salary': [50000, 65000, 75000, 58000, 48000, 72000, 85000, 62000, 52000, 80000, 68000, 71000, 55000, 90000, 61000],
    'doj': ['2022-01-15', '2020-06-20', '2018-03-10', '2021-08-25', '2023-02-14',
            '2019-11-05', '2017-09-30', '2022-05-12', '2021-12-01', '2018-07-18',
            '2020-04-22', '2019-10-08', '2022-09-15', '2016-01-20', '2021-03-10']
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv('new_data.csv', index=False)
print("Data saved to 'new_data.csv'")  # ✅ fixed

print(df)

# Load CSV
df_loaded = pd.read_csv('new_data.csv')
print("\nData loaded from CSV:")
print(df_loaded)

# --------- Selection ---------
print(df[['name', 'age']])

print(df.loc[df.name == 'rohan'])
print(df.iloc[3])
print(df.iloc[0:5])

# --------- Filtering ---------
print(df[df['age'] >= 20])
print(df[(df['age'] >= 24) & (df['salary'] >= 10000)])

print(df.where(df['age'] >= 24))

# --------- Column Operations ---------
df['Bonus'] = df['salary'] * 0.2
print(df)

# Add new row
df.loc[len(df)] = ['xyz', 116, 21, 21000, '2023-01-01', 4200]
print(df)

# Update value
df.loc[6, 'salary'] = 50000

# Drop column
df.drop('Bonus', axis=1, inplace=True)
print(df)

# Drop row with name 'xyz'
df = df.drop(df[df.name == 'xyz'].index)  # drop row (axis=0)  6412 Q0
print(df)

