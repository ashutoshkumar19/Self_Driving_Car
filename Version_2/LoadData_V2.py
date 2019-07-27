from __future__ import division
import cv2
import os
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt
from itertools import islice

LIMIT = None

DATA_FOLDER = '../datasets/dataset_2'
TRAIN_FILE = os.path.join('../datasets', 'dataset_2.txt')

def preprocess(img):
    resized = cv2.resize((cv2.cvtColor(img, cv2.COLOR_RGB2HSV))[:, :, 1], (100, 100))
    return resized

def return_data():

    X = []
    y = []
    features = []

    with open(TRAIN_FILE, 'r') as fp:
        for line in fp.readlines():
            path, angle = line.strip().split(' ')
            print(path)
            full_path = os.path.join(DATA_FOLDER, path)
            X.append(full_path)
            # using angles from -pi to pi to avoid rescaling the atan in the network
            y.append(float(angle) * scipy.pi / 180)
        print("\nPath and angle extraction done")

    # with open(TRAIN_FILE) as fp:
    #     for line in islice(fp, LIMIT):
    #         path, angle = line.strip().split()
    #         full_path = os.path.join(DATA_FOLDER, path)
    #         X.append(full_path)
    #         # using angles from -pi to pi to avoid rescaling the atan in the network
    #         y.append(float(angle) * scipy.pi / 180)

    for i in range(len(X)):
        img = plt.imread(X[i])
        features.append(preprocess(img))
        print(i)

    features = np.array(features).astype('float32')
    labels = np.array(y).astype('float32')

    with open("features", "wb") as f:
        pickle.dump(features, f, protocol=4)
    with open("labels", "wb") as f:
        pickle.dump(labels, f, protocol=4)

    print("\n...DONE...")

return_data()