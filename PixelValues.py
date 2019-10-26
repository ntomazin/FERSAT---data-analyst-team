from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os



def valueOfBandInPixel(band):
    #print(bandName)
    print("Vrijednost na pixelu(225,90) je: {0}".format(band[90,225]))
    print("Vrijednost na pixelu(102,70) je: {0}".format(band[70,102]))
    print("Vrijednost na pixelu(167,52) je: {0}".format(band[52,167]))
    print("Vrijednost na pixelu(215,55) je: {0}".format(band[55,215]))
    print("Vrijednost na pixelu(262,90) je: {0}".format(band[90,262]))




LST_dataset = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')
another = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')
another2 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20171015T095031_N0205_R079_T33TXJ_20171015T095357_resampled.nc')
#another3 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20180602T095031_N0208_R079_T33TXJ_20180602T122610_resampled.nc')
another4 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL1C_20180403T095031_N0206_R079_T33TXJ_20180403T134051_resampled.nc')





rad2 = np.array(LST_dataset.variables['B8'])
rad1 = np.array(another.variables['B8'])
rad3 = np.array(another2.variables['B8'])
#rad4 = np.array(another3.variables['B8'])
rad5 = np.array(another4.variables['B8'])


rad2, rad1 , rad3, rad5= rad2[8070:8250, 1200:1600], rad1[8070:8250, 1200:1600],rad3[8070:8250, 1200:1600],rad5[8070:8250, 1200:1600]




print("2017. godina")
valueOfBandInPixel(rad1)
print("2019. godina")
valueOfBandInPixel(rad2)
print("2017")
valueOfBandInPixel(rad3)
print("")
print("2018")
valueOfBandInPixel(rad5)
#print("2018")
#valueOfBandInPixel(rad4)
#print("test")
#valueOfBandInPixel(rad5)

f = plt.figure()
f.add_subplot(2, 3, 1)
plt.imshow(rad1,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 3, 2)
plt.imshow(rad2,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 3, 3)
plt.imshow(rad3,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 3, 4)
plt.imshow(rad5,cmap='inferno', interpolation='sinc')
plt.colorbar()


plt.show()







