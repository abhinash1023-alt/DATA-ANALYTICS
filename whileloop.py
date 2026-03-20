'''# 1. for loop

# 2. while loop

# used when we don't know exact repetions

# 3. Loop control

# break exit loop immediately

# continue skip current iteration

# pass do nothing (placeholder)
for i in range(1, 6):
	if i == 3:
		continue
	if i == 5:
		break
	print(i)'''

# loop inside another looop.
for i in range(2):
    for j in range(3):
        print("i =", i, "j =", j)