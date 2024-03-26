import numpy as np
import matplotlib.pyplot as plt

def square_root(x):
    return np.sqrt(x)

# Generate data
x_values = np.linspace(0, 10, 100)
y_values = square_root(x_values)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Square Root')
plt.xlabel('x')
plt.ylabel('Square Root of x')
plt.title('Square Root Function')
plt.legend()
plt.grid(True)
plt.show()