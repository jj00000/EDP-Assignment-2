import pandas as pd
import argparse
import re


dfpopulation = pd.read_csv('population and growth rate.csv', encoding = 'ISO-8859-1')
dfelectricity = pd.read_csv('electricity used.csv', encoding = 'ISO-8859-1')
dfwater = pd.read_csv('water used.csv', encoding = 'ISO-8859-1')


dfpopulation = dfpopulation.loc[dfpopulation['Year'] > 1999]
dfwater = dfwater.loc[dfwater['Year'] > 1999]

dfmerged = pd.merge(dfpopulation, dfelectricity, on = 'Year')
dfmerged = pd.merge(dfmerged, dfwater, on = 'Year')
dfmerged.rename(columns={"EstimatedResidentPopulationInJune": "estimated population(June)", "growth rate(%)_x": "growth rate p(%)", "growth rate(%)_y": "growth rate e(%)", "volume_ML": "volume used(ML)", "growth rate of volume used(%)": "growth rate v(%)"}, inplace = True)
dfmerged['volume used(ML)'] = pd.to_numeric(dfmerged['volume used(ML)'], downcast='signed')
print(dfmerged)

dfmerged.to_csv('final.csv', index = False, float_format='%.3f')


