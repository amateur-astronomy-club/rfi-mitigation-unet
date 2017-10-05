RFI Mitigation using Unet
=====
Github Repo for the Image Segmentation project by AAC NITK as part of Astro
Committee, Engineer '16 - 17.

We will use Deep Learning for RFI mitigation.
[Unet](https://github.com/jakeret/tf_unet/)

_**THIS IS A WORK IN PROGRESS**_

## Roadmap

* **Step 1.** **`DONE`** Processing Bleien Survey Data Images using SEEK.
* **Step 2.** **`DONE`** Visualise processed data to ensure that we are
  dealing with the right type of data.
* **Step 3.** **[IN PROGRESS]** Train naive Unet on the data that has been
  processed. Analyse results. Predict. Visualise data.
* **Step 4.** **`DONE`** Generate more data using HIDE and process with
  SEEK.
* **Step 5.** Train on the extended dataset and observe results.
* **Step 6.** Train using the Keras model.


## References
* [RFI Example](https://github.com/jakeret/tf_unet/blob/master/demo/demo_radio_data.ipynb)
* [HIDE & SEEK](http://www.cosmology.ethz.ch/research/software-lab/hide---seek.html)
