import sys
sys.path.append('mnist')
from load_mnist import *
dataset = load_mnist_whole(PATH='mnist/', scale=1.0 / 255.0)
batchsize_ul = 64
print(dataset.images_train)
# x_u, _ = dataset.sample_minibatch(batchsize_ul)
# print(dataset.image_train)