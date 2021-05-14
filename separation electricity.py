import pandas as pd
import argparse
import re


dataframe = pd.read_csv('PRICE_AND_DEMAND_VIC1.csv', encoding = 'ISO-8859-1')
dfpopulation = pd.read_csv('population and growth rate.csv', encoding = 'ISO-8859-1')

electricity = dataframe['ElectricityUsed(MW)'].values

growthrate = [0]
i = 1
while i < len(electricity):
    temp = ((electricity[i] - electricity[i-1]) / electricity[i-1]) * 100
    growthrate.append(float("{:.3f}".format(temp)))
    i += 1
    

dataframe.insert(2, "growth rate(%)", growthrate)
dfpopulation = dfpopulation.loc[dfpopulation['Year'] > 1999]
dfmerged = pd.merge(dfpopulation, dataframe, on = 'Year')

dfmerged.rename(columns={"EstimatedResidentPopulationInJune": "estimated population(June)", "growth rate(%)_x": "growth rate p(%)", "growth rate(%)_y": "growth rate e(%)"}, inplace = True)
print(dfmerged)
dfmerged.to_csv('population and electricity.csv', index = False,  float_format='%.3f')
