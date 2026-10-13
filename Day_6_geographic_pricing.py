#======================================================
# DAY 6 : GEOGRAPHIC PRICE DISCRIMINATION & MARGIN ANALYSIS ( FMCG CASE STUDY)
# Public Portfolio Matrix: https://github.com
#======================================================
import pandas as pd

print("=================================================")
print("   DAY 6: GEOGRAPHIC PRICING & MARGIN ANALYSIS   ")
print("=================================================")

# 1. define the localized operational data from your feld observations
ice_cream_data = {
    "Location" : ["Sector 37C Gurugram", "Connaught Place Delhi"],
    "Brand Name" : [" Mother Dairy Vending Cart", "Cream Bell Premium Outlet"],
    "Retail_Price_INR" : [35.0,50.0],
    "Estimated_Base_Cost_INR" : [22.0,22.0], # Production cost remains uniform
    "Location_Premium_Overhead_INR" : [2.0,8.0], # High distribution premiums in CP

 }

df = pd.DataFrame(ice_cream_data)

# 2. Automatically calculate total cost and net profit margins via Pandas vector loops
df ["Total_Cost_INR"] = df ["Estimated_Base_Cost_INR"] + df ["Location_Premium_Overhead_INR"]
df ["Net_Profit_INR"] = df ["Retail_Price_INR"] - df ["Total_Cost_INR"]
df ["Profit_Margin_Percent"] = ( df ["Net_Profit_INR"] / df ["Retail_Price_INR"]) * 100

# 3. Print outthe structures operational table
print(df.to_string(index= False, columns= ["Location", "Brand Name", "Retail_Price_INR", "Net_Profit_INR", "Profit_Margin_Percent"]))
print("----------------------------------------------------")
print("💡Enterprise Insight for FMCG Operations:")
print("Even though base manufacturing costs are identical, location-based premiums")
print("allow the CP distribution channel to extract a significantly higher profit margin (40%)")
print("compares to the suburban Gurugram sector track (31.4%). This is geographical optimization live.")
print("=====================================================")



