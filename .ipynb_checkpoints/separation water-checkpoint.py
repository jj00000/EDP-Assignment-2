import pandas as pd
import argparse
import re


df = pd.read_csv('Water_Supply_-_Daily_Volume_observed_for_storage_dams_operated_by_Melbourne_Water.csv', encoding = 'ISO-8859-1')
dfpopulation = pd.read_csv('population and growth rate.csv', encoding = 'ISO-8859-1')

df.replace(r'([0-9{4}])/[0-9]{2}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', r'\1', regex = True, inplace = True)

grouped = df.groupby(['recorddate']).agg({'volume_ML': 'sum'})
grouped = grouped.iloc[32:,:]

volumeused = grouped['volume_ML'].values
growthratewater = [0]
i = 1
while i < len(volumeused):
    temp = ((volumeused[i] - volumeused[i-1]) / volumeused[i-1]) * 100
    growthratewater.append(float("{:.3f}".format(temp)))
    i += 1

grouped.insert(1, "growth rate of volume used(%)", growthratewater)
grouped.index.name = 'Year'

dfpopulation = dfpopulation.loc[dfpopulation['Year'] > 1970]
grouped.reset_index(inplace = True)
grouped['Year'] = grouped['Year'].astype(int)
dfmerged = pd.merge(dfpopulation, grouped, on = 'Year')

dfmerged.rename(columns={"EstimatedResidentPopulationInJune": "estimated population(June)", "growth rate(%)": "growth rate p(%)","volume_ML": "volume used(ML)", "growth rate of volume used(%)": "growth rate w(%)"}, inplace = True)
dfmerged['volume used(ML)'] = pd.to_numeric(dfmerged['volume used(ML)'], downcast='signed')
print(dfmerged)

dfmerged.to_csv('population and water.csv', index = False,  float_format='%.3f')