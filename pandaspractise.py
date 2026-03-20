import numpy as np
import pandas as pd

dict1 = {
    "name": ['harry', "rishi", "rohan", "riya"],
    "marks":[23,45,67,86],
    "city":['hyd', 'ngp', 'bhr', 'bhs']
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv('friends.csv')
df.to_csv('friends_index_false.csv', index=False)
print(df.head(2))


