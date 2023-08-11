# import stuff
import matplotlib.pyplot as plt
import numpy as np

# settings axis titles
plt.xlabel("Year")
plt.ylabel("People in thousands")

# setting graph title
plt.title("Impact of Covid with Travel in Northern Ireland (Made in Python)")

# setting year axis
x = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

# setting y-axis variables for tourist attractions
y_titanic = np.array([60.4, 63.3, 62.1, 66.7, 76.0, 81.4, 82.2, 15.0])
y_giants = np.array([75.4, 78.8, 85.1, 94.4, 101.1, 103.9, 98.8, 13.8])
y_lagan = np.array([139.6, 125.7, 129.6, 137.4, 142.6, 132.7, 132.7, 19.3])
y_fea = np.array([0, 9.9, 10.4, 10.4, 10.8, 12.3, 20.1, 10.1])
y_blk = np.array([0, 11.4, 20.4, 20.5, 20.5, 17.0, 18.1, 21.5])
y_roevalley = np.array([22.6, 24.1, 25.0, 17.0, 20.5, 20.5, 17.0, 18.1])
y_dungannon = np.array([22.4, 33.1, 29.1, 26.8, 34.7, 38.2, 39.1, 10.2])
y_antrimcastle = np.array([16.8, 22.1, 34.3, 45.1, 44.3, 43.7, 44.1, 11.6])

# trim x points to remove decimals
x_point = np.asarray(x).astype(str)

# plot each point
plt.plot(x_point, y_giants, label="Giants Causeway")
plt.plot(x_point, y_titanic, label="Titanic Belfast")
plt.plot(x_point, y_lagan, label="Lagan Valley")
plt.plot(x_point, y_fea, label="Lough Fea")
plt.plot(x_point, y_blk, label="Divis and the Black Mountain")
plt.plot(x_point, y_roevalley, label="Roevalley")
plt.plot(x_point, y_dungannon, label="Dungannon Park")
plt.plot(x_point, y_antrimcastle, label="Antrim Castle Gardens")

# show legend
plt.legend()

# plot graph
plt.show()