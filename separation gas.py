import pandas as pd
import argparse
import re


df = pd.read_csv('DWGM Prices and Demand 2021.csv', encoding = 'ISO-8859-1')
dfpopulation = pd.read_csv('population and growth rate.csv', encoding = 'ISO-8859-1')

df.replace(r'[0-9]{2}/[0-9]{2}/([0-9{4}])', r'\1', regex = True, inplace = True)
df.replace(r'([0-9]),([0-9]{3}.[0-9]{3})', r'\1\2', regex = True, inplace = True)


df['Total Demand'] = pd.to_numeric(df['Total Demand'], downcast='float', errors = 'ignore')
grouped = df.groupby(['ï»¿Gas_Date']).agg({'Total Demand': 'sum'})
dfpopulation = dfpopulation.loc[dfpopulation['Year'] > 2006]
grouped.reset_index(inplace = True)

gasused = grouped['Total Demand'].values
growthrategas = [0]
i = 1
while i < len(gasused):
    temp = ((gasused[i] - gasused[i-1]) / gasused[i-1]) * 100
    growthrategas.append(float("{:.3f}".format(temp)))
    i += 1
    
grouped.insert(2, "growth rate g(%)", growthrategas)
grouped.rename(columns={"ï»¿Gas_Date": "Year"}, inplace = True)
grouped['Year'] = grouped['Year'].astype(int)
grouped = grouped.loc[grouped['Year'] < 2021]

dfmerged = pd.merge(dfpopulation, grouped, on = 'Year')
dfmerged.rename(columns={"EstimatedResidentPopulationInJune": "estimated population(June)", "growth rate(%)": "growth rate p(%)","Total Demand": "gas used"}, inplace = True)

print(dfmerged)
dfmerged.to_csv('population and gas.csv', index = False,  float_format='%.3f')
