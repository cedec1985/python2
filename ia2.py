import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.layers import Dense, Activation

inputs=keras.Input(shape=784,)
dense=layers.Dense(64,activation='relu')
x=dense(inputs)
x=layers(Dense(64,activation='relu'))(x)
outputs=layers.Dense(10)(x)
model=keras.Model(inputs=inputs,outputs=outputs,name="mnist_model")
keras.utils.plot_model(model,"my first_model.png")