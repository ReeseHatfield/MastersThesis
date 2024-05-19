import dask.dataframe as dd
import matplotlib.pyplot as plt
import numpy as np


df = dd.read_csv('data/consumption/energy_consumption_by_country.csv')


numeric_df = df[['Consumption MMBtu', 'Expenditure US Dollars']]


summary_df = numeric_df.groupby(df['State Name']).mean().compute()


data_array = summary_df.values


plt.figure(figsize=(10, 8))
plt.imshow(data_array, cmap='viridis', aspect='auto')
plt.colorbar(label='Values')
plt.title('Heatmap of Summarized Energy Consumption and Expenditure by State')
plt.xlabel('Features')
plt.ylabel('States')
plt.xticks(ticks=np.arange(data_array.shape[1]), labels=['Consumption MMBtu', 'Expenditure US Dollars'], rotation=0)
plt.yticks(ticks=np.arange(data_array.shape[0]), labels=summary_df.index)
plt.show()
