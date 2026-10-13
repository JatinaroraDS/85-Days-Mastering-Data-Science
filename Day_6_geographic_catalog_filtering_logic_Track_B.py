
#==============================================================
# DAY 6: GEOGRAPHIC OPTIMIZATION - NETFLIX CATALOG SPRINT
# Public POrtfolio Matrix: https://github.com
#==============================================================

import numpy as np
import pandas as pd

print("=======================================================")
print("    TRACK B: GEOGRAPHIC CATALOG FILTERING LOGIC        ")
print("=======================================================")


# 1. Define a sample global user dataset streaming from different markets
user_data = {
    "User_ID": [1, 2, 3, 4, 5],      # Explicitly added the user IDs here!
    "User_Name": ["Amit","John", "Priya", "Sarah", "Rahul" ],
    "Country_Node": [ "India", "United States", "India", "United States", "India"],
}
df = pd.DataFrame(user_data)

# 2. Apply Pandas Conditional Mapping (Vectorized If/Else Logic)
# Scenario: 'The Office' is streamed in the US market but restricted
df["Available_Steaming_Catalog"] = np.where(
    df["Country_Node"] == "United States",
    "Full Catalog + 'The Office'",                  # IF True
    "Standard Regional Catalog (Restricted)"        # IF False
)

# 3. Print out the structured operational table
print(df.to_string(index=False))
print("--------------------------------------------------------")
print("💡Tech Insght for Operational Leaders:")
print("Using 'np.where' acts as an instantanous vector query inside your system.")
print("Instead of running a slow, heavy loop over millions of database accounts,")
print("Pandas evaluates and remaps geographic streaming limit globally in milliseconds.")
print("========================================================")

