#!/usr/bin/python

from keras.utils.np_utils import to_categorical


def onehot(x):
    return to_categorical(x)
