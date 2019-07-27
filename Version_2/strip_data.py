from __future__ import division
import cv2
import os
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt
from itertools import islice

LIMIT = None

DATA_FOLDER = '../datasets/dataset_3'
TRAIN_FILE = os.path.join('../datasets', 'dataset_3.txt')

with open(TRAIN_FILE, 'r') as fp:
    myfile = open('../datasets/dataset_3_new.txt', 'w')
    for line in fp.readlines():
        path, angle = line.strip().split(',')
        print(path, ', ', angle)
        myfile.write("%s\n" % path)
