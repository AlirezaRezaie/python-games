import numpy as np
import math


class NueralNetwork:
    def __init__(self, input_num, hidden1_num, hidden2_num, output_num):
        self.input_num = input_num
        self.hidden1_num = hidden1_num
        self.hidden2_num = hidden2_num
        self.output_num = output_num

        self.w1, self.w2, self.w3 = self.gen_new_weights()
        self.b1 = np.random.uniform(-400, 400)
        self.b2 = np.random.uniform(-400, 400)
        self.learning_rate = 0.1

    def predict(self, input):
        try:
            input[0] = math.fabs(math.log(input[0], 2)) * 100
        except Exception as e:
            print(e)
            print("error on", input)
        hidden1 = np.dot(input, self.w1) + self.b1
        hidden2 = np.dot(hidden1, self.w2) + self.b2
        output = np.sin(np.dot(hidden2, self.w3))
        return output

    def backward_propagation(self, input, target, hidden_activation, output_activation):
        output_error = (target - output_activation) * self.activation_derivative(
            output_activation
        )
        hidden_error = np.dot(output_error, self.w2.T) * self.activation_derivative(
            hidden_activation
        )

        delta_w2 = self.learning_rate * np.outer(hidden_activation, output_error)
        delta_w1 = self.learning_rate * np.outer(input, hidden_error)

        self.w2 += delta_w2
        self.w1 += delta_w1

    def gen_new_weights(self):
        return (
            np.random.uniform(low=-1, high=1, size=(self.input_num, self.hidden1_num)),
            np.random.uniform(
                low=-1, high=1, size=(self.hidden1_num, self.hidden2_num)
            ),
            np.random.uniform(low=-1, high=1, size=(self.hidden2_num, self.output_num)),
        )

    def activation_derivative(self, output):
        return output * (1 - output)

    def activation_function(self, input):
        print(input)
        return 1 / (1 + np.exp(-input))
