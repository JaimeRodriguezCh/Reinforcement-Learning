import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import RNA
net = RNA.RNA([784, 30, 10])

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)