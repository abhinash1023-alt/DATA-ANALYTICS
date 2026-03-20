# used to show multiple chart in one figure

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
plt.ylabel("USer2")
