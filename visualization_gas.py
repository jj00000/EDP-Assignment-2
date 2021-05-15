import pandas as pd
import matplotlib.pyplot as plt

pop_gas = pd.read_csv('pop_gas.csv', encoding = 'ISO-8859-1')

plt.scatter(pop_gas.estimated_population_June, pop_gas.GasUsed_TJ, s = 2, color = 'b')
plt.title("pop_gas", size = 20)
plt.ylabel("GasUsed_TJ")
plt.xlabel("estimated_population")
plt.savefig('pop_gas.png', dpi = 150)
plt.show()