import pandas as pd
import csv
from pandas import Series
from sklearn.datasets import make_s_curve
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import numpy as np


# """
# Constants
# """
variance = 0.01

CHECKERBOARD_SIZE = 0.2

def get_broken_swiss_roll_dataset_with_label2(n):
    t1 = (3 * math.pi / 2) * (1 + 2 * np.random.random(math.floor(n / 2)) * 0.4)
    t2 = (3 * math.pi / 2) * (1 + 2 * (np.random.random(math.ceil(n / 2)) * 0.4 + 0.6))
    t = np.append(t1, t2)
    height = 30 * np.random.random(n)
    X = np.array([t * np.cos(t), height, t * np.sin(t)]) + variance * np.random.normal(0, 1, n * 3).reshape(3, n)
    labels = np.fmod(np.around(t / 2) + np.around(height / 12), 2)
    return X.T.tolist(), labels.reshape(n, 1).tolist()


broken_swiss_dataset, broken_swiss_labels = get_broken_swiss_roll_dataset_with_label2(2000)

# 2000 broken swiss roll data within 2 classes
data = np.asarray(broken_swiss_dataset)
np.savetxt("2Brokendata2000_iso.csv",data,delimiter=',')

label = np.asarray(broken_swiss_labels)
np.savetxt("2Brokenlabel2000_iso.csv",label,delimiter=',')


