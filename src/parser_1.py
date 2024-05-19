import dask.dataframe as dd
import numpy as np
import matplotlib.pyplot as plt

# Load the data using dask
df = dd.read_csv('data/consumption/energy_consumption_by_country.csv')

# Extract the numeric columns
numeric_df = df[['Consumption MMBtu', 'Expenditure US Dollars']]

# Compute the mean values for a quicker overview
mean_values = numeric_df.mean().compute()

# Convert to a numpy array
data_array = numeric_df.compute().values

# Plot the heatmap
plt.figure(figsize=(10, 8))
plt.imshow(data_array, cmap='viridis', aspect='auto')
plt.colorbar(label='Values')
plt.title('Heatmap of Energy Consumption and Expenditure')
plt.xlabel('Features')
plt.ylabel('Data Points')
plt.xticks(ticks=np.arange(len(mean_values)), labels=mean_values.index, rotation=90)
plt.yticks(ticks=np.arange(data_array.shape[0]), labels=df['County Name'].compute())
plt.show()
