import matplotlib.pyplot as plt
import numpy as np

y = np.array([20,80, 3, 100])
x = np.array([1, 2, 3, 4])

plt.plot(x,y)

plt.xlabel("tourism in people")
plt.ylabel("money in £")

plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 20, 50])

fig, (graph1, graph2, graph3, graph4) = plt.subplots(4)

fig.suptitle('Graph with stuff')

graph1.plot(x, y, label="line 1")
graph2.plot(x, y, label="line 2")
graph3.plot(x, y, label="line 3")
graph4.plot(x, y, label="line 4")

plt.legend()
plt.show()