import pandas as pd
import matplotlib.pyplot as plt

def plot_graph1(data_subset):
	plt.figure(figsize=(8, 6))
	plt.plot(data_subset.index, data_subset['Global_active_power'], color='blue')
	plt.title('Global Active Power over Time')
	plt.xlabel('Time')
	plt.ylabel('Global Active Power (kW)')
	plt.grid(True)
	plt.tight_layout()
	plt.savefig('plot1.png', dpi=100)
	plt.close()