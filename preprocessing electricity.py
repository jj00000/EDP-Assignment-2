import pandas as pd
import argparse
import re


dataframe = pd.read_csv('PRICE_AND_DEMAND_VIC1.csv', encoding = 'ISO-8859-1')

electricity = dataframe['ElectricityUsed(MW)'].values

growthrate = [0]
i = 1
while i < len(electricity):
    temp = ((electricity[i] - electricity[i-1]) / electricity[i-1]) * 100
    growthrate.append(float("{:.3f}".format(temp)))
    i += 1
    

dataframe.insert(2, "growth rate(%)", growthrate)
print(dataframe)
dataframe.to_csv('electricity used.csv', index = False)