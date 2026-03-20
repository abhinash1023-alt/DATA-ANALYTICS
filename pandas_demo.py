
#data frame : the structured data
# create data frame
 
import pandas  as pd
df = pd.DataFrame([1,2,3], columns=['column_name'])
print(df)


import pandas as pd
data = {
    'Name': ['Abinash', 'Arti', 'Anushka', 'Raja', 'Priyanshu', 'Jayant'],
    'Age':  [12,22,33,45,55,65],
    'Salary' : [1000, 1200, 1300, 1400, 1500, 1600]
    
}
df = pd.DataFrame(data)
print(df)
print(df.shape) # to know column and rows in a data
print(df.columns)
print(df.rename(columns={'salary': 'payment'}))
print(df.rename(columns={'salary': 'payment'}, inplace =  True))
print(df)
print(df)


print(df.describe()) # for stastical summary'''

# create a co. where you have  name, employee id, age, sallary, doj, min = 15 rows

# sae and load data frame from csv


import pandas as pd
from datetime import datetime, timedelta

# Create company data with 15 rows
data = {
    'name': ['abi', 'raja', 'priyam', 'priyanshu', 'nadeem', 'gupta', 'yadav', 'riya', 'chintu', 'jayant', 'priya', 'pushkar', 'rohan', 'sourab', 'akshay'],
    'employee_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'age': [28, 35, 42, 31, 26, 38, 45, 33, 29, 41, 36, 39, 27, 44, 32],
    'salary': [50000, 65000, 75000, 58000, 48000, 72000, 85000, 62000, 52000, 80000, 68000, 71000, 55000, 90000, 61000],
    'doj': ['2022-01-15', '2020-06-20', '2018-03-10', '2021-08-25', '2023-02-14',
            '2019-11-05', '2017-09-30', '2022-05-12', '2021-12-01', '2018-07-18',
            '2020-04-22', '2019-10-08', '2022-09-15', '2016-01-20', '2021-03-10']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('new_data.csv', index=False)
print("Data saved to 'new_data.csv")
print(df)

# Load from CSV
df_loaded = pd.read_csv('new_data.csv')
print("\nData loaded from CSV:")
print(df_loaded)

print(df[['name', 'age']]) #for multiple column

# select rows
# index name based
print(df.loc[df.name=='rohan']) 

print(df.loc[(df.name== 'rohan')]) #multiple Row filteration data

# iloc - index value based
print(df.iloc[3])

print(df.iloc[0:5]) #* lasat value never include in iloc


print(df['age']>=20)  # value always find in boolean

print(df[df['age'] >= 20])  

# df_age_filter

print(df[(df['age'] >= 24)& (df['salary']>=10000)])


print(df.where(df['age'] >= 24))


# rows and columns - operations (add, update, delete)
print(df)

# add new column
#df['Team'] =['ceo', 'Hr', 'cto', 'accountant', 'developer', 'Marketing', 'Boss']
#print(df)

df['Bonus'] = df['salary']*0.2
print(df)

# add news rows 
df.loc[len(df)] = ['xyz', 116, 21, 21000, '2023-01-01', 4200]
print(df)


len(df)


# update value - using index name
df.loc[6, 'salary'] = 50000
df

#df.drop(1, axis = 0) # by index number

print(df.drop('Bonus',axis=1))

print(df.drop('Bonus', axis=1,inplace=True))
df

