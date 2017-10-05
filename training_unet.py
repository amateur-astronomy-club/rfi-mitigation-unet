from scripts.radio_util import DataProvider
from tf_unet import unet
import glob
files = glob.glob('/home/aditi/bgs_example_data/seek_cache/*')
data_provider = DataProvider(600, files)

net = unet.Unet(channels=data_provider.channels, 
                n_class=data_provider.n_class, 
                layers=3, 
                features_root=64,
                cost_kwargs=dict(regularizer=0.001),
                )
trainer = unet.Trainer(net, optimizer="momentum", opt_kwargs=dict(momentum=0.2))
path = trainer.train(data_provider, "./unet_trained_bgs_example_data", 
                     training_iters=32, 
                     epochs=5, 
                     dropout=0.5, 
                     display_step=2)