
# used to show part-to-part whole relationships/data

# data
'''import matplotlib.pyplot as plt
categories = ['A', 'B', 'C','D','D','E']
sales = [20, 25, 30, 35, 40, 45]

plt.pie(sales, labels=categories, autopct = '%1.1f%%', startangle=90)
plt.title("Pie chart Example")
plt.show()'''

# Scatter Plot Example

'''import matplotlib.pyplot as plt
#data
y1 = [10, 20, 30, 40, 50]
y2 = [25, 35, 45, 55, 65]
plt.scatter(y1, y2)
plt.title("scatter Examples")
plt.show()'''

'''# used to show multiple chart in one figure
import matplotlib.pyplot as plt
# dara-1-bar chart
categories = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [10, 20, 30, 40, 50]

# data-2 - scatter plot
y1 = [10, 20, 30, 40, 50]
y2 = [5, 10, 15, 20, 25]

plt.figure(figsize=(10,4))

# first plot- bar chart
plt.subplot(1,2,1) # row, column, position
plt.bar(categories, sales)
plt.title("Daily Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")

# seacond plot-scotter chart
plt.subplot(1,2,2) # row, column, position
plt.scatter(y1, y2)
plt.title("User Example")
plt.xlabel("User1")
plt.ylabel("USer2")'''

# create df 
import pandas as pd

# data
data = {
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales' : [ 1500, 1400, 1600, 1300],

    

}
df = pd.DataFrame
