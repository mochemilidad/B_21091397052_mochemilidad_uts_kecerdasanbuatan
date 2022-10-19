# mochemilidad
# 21091397052
import numpy as np
inputs = [1.0, 2.0, 3.0, 2.5, 4.5, 5.0, 6.2, 7.0, 8.4, 9.0]
weights = [0.2, 0.8,-0.5, 1.0, 2.2, 3.1, 3.3, 3.7, 4.2, -0.2]
bias = 2.0
outputs = np.dot(weights, inputs) + bias
print(outputs)