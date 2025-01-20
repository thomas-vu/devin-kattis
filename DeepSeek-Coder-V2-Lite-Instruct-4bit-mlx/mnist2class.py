import numpy as np

# Load training data
training_data = []
with open('training_data.txt', 'r') as file:
    for line in file:
        values = list(map(int, line.split()))
        x_values = values[:51]
        y_value = values[51]
        training_data.append((x_values, y_value))

# Initialize weights randomly
weights = [np.random.choice([-1, 1], size=51) for _ in range(30)]

# Training function
def train_perceptron(weights, x, y):
    for k in range(30):
        output = np.sign(np.dot(x, weights[k]))
        if output != y:
            weights[k] = np.where(weights[k] * x > 0, weights[k], -weights[k])
    return weights

# Train the network
for x, y in training_data:
    weights = train_perceptron(weights, np.array(x), y)

# Output the weights
for weight in weights:
    print(' '.join(map(str, weight)))