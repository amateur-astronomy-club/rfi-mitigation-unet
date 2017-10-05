"""
    Name: Ayush Kumar, Kaushik S Kalmady
    Date: 5/10/2017

    Ref : https://github.com/jakeret/tf_unet/blob/master/demo/demo_radio_data.ipynb
    Processing downloaded files using SEEK Package

    Download the Bleien Survey Data
    Run the following command in your terminal
    $ wget -q -r -nH -np --cut-dirs=2 http://people.phys.ethz.ch/~ast/cosmo/bgs_example_data/

    Make sure you save a copy of this folder in case you need the original files.
    Original files will be deleted after processing.

    You will also need to have SEEK installed.
    For installation instructions: seek.readthedocs.io, https://github.com/cosmo-ethz/seek


"""

import glob
import os
from subprocess import Popen
from __future__ import print_function

# Create output directory
os.makedirs("bgs_example_data/seek_cache")

# Get a list of all files that match the regex
files = glob.glob('bgs_example_data/2016/03/21/HIMap_RSG7M_A1_24_MP_PXX_Z0_C0*')
list.sort(files) # Sort files by name

# For some reason SEEK only processes the first file in the folder (no idea why)
# So we'll just process one file, delete it, run SEEK again, and process the next and so on
for i in range(len(files)):
    # Process first file in the folder
    os.system("seek --file-prefix='./bgs_example_data' --post-processing-prefix='bgs_example_data/seek_cache' --chi-1=20 --overwrite=True seek.config.process_survey_fft")
    # Remove this file so that in next iteration, the second file is processed
    os.remove(files[i])

print("Done. Check bgs_example_data/seek_cache/ for processed .h5 files")
