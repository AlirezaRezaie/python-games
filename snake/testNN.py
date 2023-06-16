from nn import NueralNetwork
import numpy as np


network = NueralNetwork(1, 5, 5, 4)
prediction = network.predict([373])
print(np.argmax(prediction))
prediction = network.predict([379])
print(np.argmax(prediction))
prediction = network.predict([386])
print(np.argmax(prediction))
prediction = network.predict([390])
print(np.argmax(prediction))
prediction = network.predict([400])
print(np.argmax(prediction))
prediction = network.predict([411])
print(np.argmax(prediction))
prediction = network.predict([421])
print(np.argmax(prediction))
prediction = network.predict([430])
print(np.argmax(prediction))

# critical issue network not sensetive to slight changes
# resolved : using sin function and normalizing input with log
