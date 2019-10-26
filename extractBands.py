from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os


def valueOfBand(dataset, band, date):

    if not os.path.isdir("csv/"+band):
        os.mkdir(band)

    #if not os.path.isfile('csv/'+band+'.csv'):
    radiance = np.array(dataset.variables[band])
    radiance = radiance[8070:8250, 1200:1600]

    print("Spremam u "+"csv/"+band+"/"+date+".csv")
    np.savetxt("csv/"+band+"/"+date+".csv", radiance, delimiter=",")

    print("Jesam ga")


def valueOfBandInPixel(band):
    #print(bandName)
    print("Vrijednost na pixelu(225,90) je: {0}".format(band[90,225]))
    print("Vrijednost na pixelu(102,70) je: {0}".format(band[70,102]))
    print("Vrijednost na pixelu(167,52) je: {0}".format(band[52,167]))
    print("Vrijednost na pixelu(215,55) je: {0}".format(band[55,215]))
    print("Vrijednost na pixelu(262,90) je: {0}".format(band[90,262]))



dataset1 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')
dataset2 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')
dataset3 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20171015T095031_N0205_R079_T33TXJ_20171015T095357_resampled.nc')
#another3 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20180602T095031_N0208_R079_T33TXJ_20180602T122610_resampled.nc')
dataset4 = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL1C_20180403T095031_N0206_R079_T33TXJ_20180403T134051_resampled.nc')

rad1 = np.array(dataset1.variables['B8'])
rad2 = np.array(dataset2.variables['B8'])
rad3 = np.array(dataset3.variables['B8'])
#rad4 = np.array(another3.variables['B8'])
rad4 = np.array(dataset4.variables['B8'])

rad5 = np.array(dataset1.variables['B4'])
rad6 = np.array(dataset2.variables['B4'])
rad7 = np.array(dataset3.variables['B4'])
#rad4 = np.array(another3.variables['B8'])
rad8 = np.array(dataset4.variables['B4'])


rad2, rad1 , rad3, rad4= rad2[8070:8250, 1200:1600], rad1[8070:8250, 1200:1600],rad3[8070:8250, 1200:1600],rad4[8070:8250, 1200:1600]
rad5, rad6 , rad7, rad8= rad5[8070:8250, 1200:1600], rad6[8070:8250, 1200:1600],rad7[8070:8250, 1200:1600],rad8[8070:8250, 1200:1600]

print("----B8------")
print("2017. godina")
valueOfBandInPixel(rad1)
print("2019. godina")
valueOfBandInPixel(rad2)
print("2017")
valueOfBandInPixel(rad3)
print("2018")
valueOfBandInPixel(rad4)


print("----B4------")
print("2017. godina")
valueOfBandInPixel(rad5)
print("2019. godina")
valueOfBandInPixel(rad6)
print("2017")
valueOfBandInPixel(rad7)
print("2018")
valueOfBandInPixel(rad8)



f = plt.figure()

f.add_subplot(2, 2, 1)
plt.imshow(rad1,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 2, 2)
plt.imshow(rad2,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 2, 3)
plt.imshow(rad3,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(2, 2, 4)
plt.imshow(rad4,cmap='inferno', interpolation='sinc')
plt.colorbar()

plt.show()


f2 = plt.figure()

f2.add_subplot(2, 2, 1)
plt.imshow(rad1,cmap='inferno', interpolation='sinc')
plt.colorbar()

f2.add_subplot(2, 2, 2)
plt.imshow(rad2,cmap='inferno', interpolation='sinc')
plt.colorbar()

f2.add_subplot(2, 2, 3)
plt.imshow(rad3,cmap='inferno', interpolation='sinc')
plt.colorbar()

f2.add_subplot(2, 2, 4)
plt.imshow(rad4,cmap='inferno', interpolation='sinc')
plt.colorbar()

plt.show()









