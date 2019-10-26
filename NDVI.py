"""

The normalized difference vegetation index (NDVI) is a simple graphical indicator that can be used to analyze remote
sensing measurements, typically, but not necessarily, from a space platform, and assess whether the target being
observed contains live green vegetation or not.


"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os

LST_dataset = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')
another = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')

B08_2019 = np.array(LST_dataset.variables['B8'])
B08_2017 = np.array(another.variables['B8'])

B04_2019 = np.array(LST_dataset.variables['B4'])
B04_2017 = np.array(another.variables['B4'])

ndvi_2019 = (B08_2019 - B04_2019) / (B08_2019 + B04_2019)
ndvi_2017 = (B08_2017 - B04_2017) / (B08_2017 + B04_2017)

print("NDVI 2017 : "+ndvi_2017)
print("NDVI 2019 : "+ndvi_2019)
