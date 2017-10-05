
import glob
import os
from subprocess import Popen

l = glob.glob('/Users/ayush/mypro/code/tf_unet/demo/bgs_example_data/2016/03/21/HIMap_RSG7M_A1_24_MP_PXX_Z0_C0*')
list.sort(l)

#subprocess.call(["mkdir -p /Users/ayush/mypro/code/tf_unet/demo/bgs_example_data/seek_cache"])

for i in range(len(l)):
    os.system("seek --file-prefix='./bgs_example_data' --post-processing-prefix='bgs_example_data/seek_cache' --chi-1=20 --overwrite=True seek.config.process_survey_fft")
    print i+1
    os.remove(l[i])

print "done"
