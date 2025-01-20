import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
import random

# Load the MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist['data'], mnist['target'].astype(int)

# Flatten the images to 51 features
X = X / 255.0 * 2 - 1  # Scale to [-1, 1]
X = X[:, :51]  # Take the first 51 features

# Convert labels to binary (0 or 1) for classification
y_bin = np.zeros((len(y), 10))
for i, label in enumerate(y):
    y_bin[i, label] = 1

# Split the data into training and validation sets
X_train, y_train = X[:60000], y_bin[:60000]
X_val, y_val = X[60000:], y_bin[60000:]

# Initialize the binary neural network classifier
clf = MLPClassifier(hidden_layer_sizes=(150,), max_iter=200, alpha=1e-4,
                    solver='sgd', verbose=10, random_state=1,
                    learning_rate_init=.1)

# Train the classifier on the training data
clf.fit(X_train, np.argmax(y_train, axis=1))

# Output the weights of the perceptron nodes
weights = clf.coefs_[0]
for i in range(150):
    for j in range(51):
        print(int(np.sign(weights[i][j])))