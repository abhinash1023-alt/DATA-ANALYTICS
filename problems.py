# Q1 Print numbers from 1 to 10 using a for loop.
# Q2 print numbers from 10 down to 1 using a while loop. 
# Q3 print the multiplication table of using a for loop.
# Q4 write a program that prints only even numbers between 1 and 20 using a while loop.
# Q5 print a pattern using anested for loop.

# Ans:1
for i in range(1, 10):
    print(i)

# ans:2
i = 10
while i >= 1:
    print(i)
    i -= 1

# Ans:3
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

# Ans:4
i = 2
while i <= 20:
    print(i)
    i += 2
    
# Ans:5
rows = 10 
for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()