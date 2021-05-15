import pandas as pd
import matplotlib.pyplot as plt

pop_electricity = pd.read_csv('pop_electricity.csv', encoding = 'ISO-8859-1')

plt.scatter(pop_electricity.estimated_population_June, pop_electricity.ElectricityUsed_MW, s = 2, color = 'b')
plt.title("pop_electricity", size = 20)
plt.ylabel("ElectricityUsed_MW")
plt.xlabel("estimated_population")
plt.savefig('pop_electricity.png', dpi = 150)
plt.show()