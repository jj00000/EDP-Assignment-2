import pandas as pd
import argparse
import re


dataframe = pd.read_csv('result.csv', encoding = 'ISO-8859-1')

population = dataframe['EstimatedResidentPopulationInJune'].values

growthrate = [0]
i = 1
while i < len(population):
    temp = ((population[i] - population[i-1]) / population[i-1]) * 100
    growthrate.append(float("{:.3f}".format(temp)))
    i += 1
    

dataframe.insert(2, "growth rate(%)", growthrate)
print(dataframe)
dataframe.to_csv('population and growth rate.csv', index = False)