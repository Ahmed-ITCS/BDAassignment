import pandas as pd
import matplotlib.pyplot as plt

def plot_graph3(data_subset):
	plt.figure(figsize=(8, 6))
	plt.plot(data_subset.index, data_subset['Sub_metering_1'], color='green', label='Kitchen')
	plt.plot(data_subset.index, data_subset['Sub_metering_2'], color='blue', label='Laundry room')
	plt.plot(data_subset.index, data_subset['Sub_metering_3'], color='red', label='Electric water-heater and air-conditioner')
	plt.title('Energy Sub Metering over Time')
	plt.xlabel('Time')
	plt.ylabel('Energy Sub Metering (Wh)')
	plt.legend(loc='upper right')
	plt.grid(True)
	plt.tight_layout()
	plt.savefig('plot3.png', dpi=100)
	plt.close()