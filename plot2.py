import pandas as pd
import matplotlib.pyplot as plt

def plot_graph2(data_subset):
	plt.figure(figsize=(8, 6))
	plt.plot(data_subset.index, data_subset['Voltage'], color='red')
	plt.title('Voltage over Time')
	plt.xlabel('Time')
	plt.ylabel('Voltage (V)')
	plt.grid(True)
	plt.tight_layout()
	plt.savefig('plot2.png', dpi=100)
	plt.close()
