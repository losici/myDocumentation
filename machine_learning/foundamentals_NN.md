# Activation functions
For complex problems, you need to use non-linear functions.

## Sigmoid function
## Tanh
## ReLU (Rectified Linear Unit)
Piecewise linear, the derivative is a step, and it is good to train big networks.

Different layers can have different activation functions.

The input layer does not have activation functions.
Hidden layers use ReLU.
The output layer uses something that bounds the output.

Why do we need more than one layer?
To learn complex non-linear functions.

To perform the AND operator with a sigmoid activation function, you can use the weights w1, w2, w3 as -10, 7, 7 or -30, 20, 20.

Doing the same exercise with XOR is not possible. In that case, we need a non-linear activation function. With XOR, you can use two hidden layers and combine one layer for AND and one layer for OR.

Practical stuff:
- The dimension of inputs is the number of neurons.
- The dimension of weights is the matrix of neurons in one layer times the number of neurons in the next layer.
- There is one bias connected to each neuron.

How many total parameters does this network have?

Deep Neural Network:
- A neural network with more than one hidden layer.
- In most applications, it is more efficient to have one more hidden layer rather than a bigger layer.

How to train a neural network?
Training the network involves tweaking the parameters of the model to improve predictions.

Types of splitting:
- Random sampling
- Stratified sampling
- K-fold cross-validation

Mean Squared Error (MSE) penalizes larger errors more heavily than Mean Absolute Error (MAE) or Mean Error because the errors are squared. Squaring the errors amplifies the impact of larger errors, making MSE more sensitive to outliers. This is why MSE is often used when you want to emphasize minimizing larger deviations.

# Initialization of parameters
When all weights and biases are the same, all activations will be the same in the forward pass.

TensorFlow and PyTorch

No activation function means linear output