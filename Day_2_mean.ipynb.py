# %%
#1. Pure Python (No Libraries Needed)
#A.Store the compensation number in a list
compensation = [800212,754871,1176526,791094,786382,2082985]

#B.Sum the list and divide by its length
mean_val = sum( compensation )/len(compensation)

print ("mean: ", mean_val)
# %%
#2. Using Pandas (Data Science Standard)
import pandas as pd
compensation = [800212,754871,1176526,791094,786382,2082985]

#Convert the list to a pandas Series and call. mean()
mean_val = pd.Series(compensation).mean()
print("Mean:", mean_val )