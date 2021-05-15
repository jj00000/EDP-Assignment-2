import pandas as pd
import matplotlib.pyplot as plt

pop_water = pd.read_csv('pop_water.csv', encoding = 'ISO-8859-1')

plt.scatter(pop_water.estimated_population_June, pop_water.WaterUsed_ML, s = 2, color = 'b')
plt.title("pop_water", size = 20)
plt.ylabel("WaterUsed_ML")
plt.xlabel("estimated_population")
plt.savefig('pop_water.png', dpi = 150)
plt.show()