"""
Name : Ayush Kumar
Date: 10/10/2017
Ref : https://github.com/jakeret/tf_unet/blob/master/demo/demo_radio_data.ipynb

Using the trained unet to perform predictions and vsisualizing them.

Make sure to give the correct path to load the parameters.
Follow all the instructions in the file : trained_unet.py

You need to have tf_unet installed to execute this file.
Install tf_unet by following the instructions at https://tf_unet.readthedocs.io


"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import glob
plt.rcParams['image.cmap'] = 'gist_earth'

from scripts.radio_util import DataProvider
from tf_unet import unet

files = glob.glob('bgs_example_data/seek_cache/*')

#data provider from tf_unet
# The parameter 600 can be changed but it behaves in a weird fashion it refers to the time axes
# in the RFI data
data_provider = DataProvider(600, files)
net = unet.Unet(channels=data_provider.channels,
                n_class=data_provider.n_class,
                layers=3,
                features_root=64,
                cost_kwargs=dict(regularizer=0.001),
                )


# Make sure that you use the correct path on your device.
#This is the path to the folder obtained after training the unet as per trained_unet.py
path = "./unet_trained_bgs_example_data/model.cpkt"
data_provider = DataProvider(600, files)
x_test, y_test = data_provider(96)

# We couldn't use data_provider directly to visulaize all the 96 predictions as it
# consumes too much memory, therefore we are performing the prediction on each file one by one.

# Matplotlib Plotting.
fig, ax = plt.subplots(1,3, figsize=(12,4))
j = 0

# Visualizing and predicting individually.
for i in x_test:
    # tf_unet source code expects 4 axes for the predict function to work
    # currently x_test only has 3 axes so we use expand_dims to add an additional axes.
    i = np.expand_dims(i,axis=0)
    # Couldn't find a way to not have to load all the parameters everytime.
    prediction = net.predict(path,i)
    ax[0].imshow(i[0,...,0], aspect="auto")
    ax[1].imshow(y_test[0,...,1], aspect="auto")
    ax[2].imshow(prediction[0,...,1], aspect="auto")

    #Saves The Images in the current directory.
    fig.savefig("pred"+str(j)+".png")
    j = j+1
