# mochemilidad
# 21091397052
import numpy as np
inputs = [1.1, 2.2, 3.3, 2.4, 5.5, 5.6, 6.7, 7.8, 8.9, 9.9]
weights = [1.2, 2.8, -3.5, 4.0, 5.2, 6.1, 7.3, 8.7, 9.2, -9.2]
weights = [2.2, 2.3, -2.9, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3]
weights = [3.4, 3.5, 3.5, 3.6, 3.7, 3.8, 3.9, 4.1, 4.2, 4.3]
weights = [4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.1, 5.2, 5.3, 5.4]
weights = [5.6, 5.7, 5.8, 5.9, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
bias = [1.0, 2.0, 3.3, 4.3, 5.1]
output = np.dot(weights, inputs) + bias
print(output)
