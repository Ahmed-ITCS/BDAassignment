import pandas as pd
import matplotlib.pyplot as plt

def plot_graph4(data_subset):
	plt.figure(figsize=(8, 6))
	plt.hist(data_subset['Global_active_power'], bins=30, color='orange', edgecolor='black')
	plt.title('Global Active Power Frequency Distribution')
	plt.xlabel('Global Active Power (kW)')
	plt.ylabel('Frequency')
	plt.grid(True)
	plt.tight_layout()
	plt.savefig('plot4.png', dpi=100)
	plt.close()
