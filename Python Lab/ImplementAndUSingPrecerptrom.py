# To implement AND function using Perceptron
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=10):
        # Initialize weights to zero (including bias) and set learning rate and epochs
        self.weights = np.zeros(input_size + 1)  
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        # Activation function: Step function
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        # Compute the weighted sum of inputs plus bias
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        # Apply the activation function to determine the output
        return self.activation(summation)

    def train(self, training_inputs, labels):
        # Train the Perceptron over the given number of epochs
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                # Make a prediction with the current weights
                prediction = self.predict(inputs)
                # Calculate the error
                error = label - prediction
                # Update the weights based on the error
                self.weights[1:] += self.learning_rate * error * np.array(inputs)
                self.weights[0] += self.learning_rate * error

# Define the training data for the AND function
training_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

labels = np.array([0, 0, 0, 1])  # Expected output of the AND function

# Initialize the Perceptron with 2 input features
perceptron = Perceptron(input_size=2)
# Train the Perceptron with the AND function data
perceptron.train(training_inputs, labels)

# Define test inputs
test_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Test the Perceptron on all possible inputs and print the results
for test in test_inputs:
    print(f"Input: {test}, Output: {perceptron.predict(test)}")
