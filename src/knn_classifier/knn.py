import random
import numpy as np
from lzw import lzw_train, lzw_test
import glob
random.seed(1234)


# returns predicted label, a value between 1-40
def predict(trained_data, x):
    compressed_sizes = []
    for dictio in trained_data:
        size = lzw_test(dictio["dictionary"], x)
        compressed_sizes.append([size, dictio["label"]])
    compressed_sizes = np.array(compressed_sizes)
    return compressed_sizes[np.argmin(compressed_sizes[:,0])][1]

directories = glob.glob("data/*")
train = [[] for _ in range(len(directories))]
x_test = []
y_test = []

# populate data
for i, dir in enumerate(directories):
    images = glob.glob(dir + "/*")
    # randomize test samples
    random.shuffle(images)
    # define dirname as label
    label = dir.split("/")[1]
    # append train data
    for img in images[:9]:
        train[i].append(img)
    # append test data
    x_test.append(images[9])
    y_test.append(label)

# train
trained_data = []
for train_sample in train:
    trained_data.append(lzw_train(train_sample))

# prediction
predictions = [predict(trained_data=trained_data, x=x) for x in x_test]
print("predictions")
print(predictions)
print("y_test")
print(y_test)

predictions = np.array(predictions)
y_test = np.array(y_test)
accuracy = np.sum(predictions == y_test) / len(y_test)

print("accuracy")
print(accuracy)