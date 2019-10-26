from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os

from PIL import Image



def valueOfBandInPixel(band):
    #print(bandName)
    #print("Vrijednost od {0}, na pixelu(225,90) je: {1}".format(, band[90,225]))
    return band[90,225], band[88, 220], band[85, 220]


dataset = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')
dataset4 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL1C_20150728T095006_N0204_R079_T33TXJ_20150728T095006_resampled.nc')
dataset5 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL1C_20161206T094402_N0204_R036_T33TYL_20161206T094529_resampled.nc')
#onaj iz 2018 nije dobar format....
dataset2 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20171015T095031_N0205_R079_T33TXJ_20171015T095357_resampled.nc')
dataset3 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')


rad =[]
rad2 = []
rad3 = []
rad4 = []
rad5 = []
##rad.append(valueOfBandInPixel("B1", np.array(dataset.variables['B1'])))


#print(rad)


rad.append(valueOfBandInPixel(np.array(dataset.variables['B1'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B2'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B3'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B4'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B5'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B6'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B7'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B8'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B8A'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B9'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B11'])[8070:8250, 1200:1600]))
rad.append(valueOfBandInPixel(np.array(dataset.variables['B12'])[8070:8250, 1200:1600]))

rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B1'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B2'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B3'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B4'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B5'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B6'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B7'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B8'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B8A'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B9'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B11'])[8070:8250, 1200:1600]))
rad2.append(valueOfBandInPixel(np.array(dataset2.variables['B12'])[8070:8250, 1200:1600]))

rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B1'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B2'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B3'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B4'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B5'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B6'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B7'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B8'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B8A'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B9'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B11'])[8070:8250, 1200:1600]))
rad3.append(valueOfBandInPixel(np.array(dataset3.variables['B12'])[8070:8250, 1200:1600]))

rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B1'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B2'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B3'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B4'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B5'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B6'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B7'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B8'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B8A'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B9'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B11'])[8070:8250, 1200:1600]))
rad4.append(valueOfBandInPixel(np.array(dataset4.variables['B12'])[8070:8250, 1200:1600]))

rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B1'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B2'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B3'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B4'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B5'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B6'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B7'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B8'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B8A'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B9'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B11'])[8070:8250, 1200:1600]))
rad5.append(valueOfBandInPixel(np.array(dataset5.variables['B12'])[8070:8250, 1200:1600]))



x = [1,2,3,4,5,6,7,8,8.1,9,11,12]
print(rad)

plt.plot(x, rad4, 'y', label='28.7.2015.')
plt.plot(x, rad5, 'm', label='6.12.2016.')
plt.plot(x, rad, 'r', label='6.8.2017.')
plt.plot(x, rad2, 'g', label='15.10.2017.')
plt.plot(x, rad3, 'b', label='17.2.2019.')


plt.legend()


# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - values')

# giving a title to my graph
#plt.title('6.8.2017.')
#plt.title('2.6.2018.')
#plt.title('17.2.2019.')
plt.title("Values of pixel 225, 90")

plt.savefig('graph/graph.pdf')

# function to show the plot
plt.show()

