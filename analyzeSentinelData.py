from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os

from PIL import Image


from cachetools import cached, TTLCache
cache = TTLCache(maxsize=100, ttl=300)  # 2 - let's create the cache object.




def valueOfBandInPixel(band):
    #print(bandName)
    print("Vrijednost na pixelu(225,90) je: {0}".format(band[90,225]))
    print("Vrijednost na pixelu(102,70) je: {0}".format(band[70,102]))
    print("Vrijednost na pixelu(167,52) je: {0}".format(band[52,167]))
    print("Vrijednost na pixelu(215,55) je: {0}".format(band[55,215]))
    print("Vrijednost na pixelu(262,90) je: {0}".format(band[90,262]))


@cached(cache)  # 3 - it's time to decorate the method to use our cache system!
def valueOfBand(dataset, band):
    #if not os.path.isfile('csv/'+band+'.csv'):
    #print("Ne postoji file "+band+".txt")
    radiance = np.array(dataset.variables[band])
    radiance = radiance[8070:8250, 1200:1600]

    np.savetxt("csv/"+band+".csv", radiance, delimiter=",")

    im = Image.fromarray(radiance).convert('RGB')
    im.save("image/"+band+".jpeg")

    print(
        "Radiance measurements: {0}, max radiance: {1:.2f} C, min radiance: {2:.2f} C, avg radiance: {3:.2f} C".format(
            len(radiance), np.max(radiance), np.min(radiance), np.average(radiance)))
   # print(dataset.variables["long_name"])
    np.savetxt('cache/'+band+'.txt', radiance)
    """
    else:
        radiance = np.fromfile("csv/"+band+".csv")
        print("Postoji file za "+band)
    """
    return radiance

def drawPlot(bands):
    numOfPics = int(1 + len(bands) / 4)
    currentPic = 0
    row = int(1+len(bands) / 4)
    f = plt.figure()
    for b in bands:
        currentPic = currentPic + 1
        #print(row, numOfPics, currentPic)
        f.add_subplot(row, numOfPics, currentPic)
        plt.imshow(b, cmap='inferno', interpolation='nearest')
        #f.title.set_text('B'+currentPic)
        valueOfBandInPixel("B"+str(currentPic), b)
        #plt.savefig('B'+str(currentPic)+'.png')


LST_dataset = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')
another = Dataset('/home/piki/Ostalo/FERSAT/SentinelData/S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')


#print(LST_dataset.variables)
#print(LST_dataset.variables['B8'])

radiances = []
"""
for i in range(1,12):
    if i==10:
        continue
    band = "B"+str(i)
    radiances.append(valueOfBand(LST_dataset, band))


rad1 = np.array(LST_dataset.variables['B5'])
rad2 = np.array(another.variables['B5'])
diff = rad1-rad2
radiances.append(diff)

rad1 = np.array(LST_dataset.variables['B6'])
rad2 = np.array(another.variables['B6'])
diff = rad1-rad2
radiances.append(diff)

rad1 = np.array(LST_dataset.variables['B7'])
rad2 = np.array(another.variables['B7'])
diff = rad1-rad2
radiances.append(diff)

rad1 = np.array(LST_dataset.variables['B8'])
rad2 = np.array(another.variables['B8'])
diff = rad1-rad2
radiances.append(diff)

rad1 = np.array(LST_dataset.variables['B8A'])
rad2 = np.array(another.variables['B8A'])
diff = rad1-rad2
radiances.append(diff)

rad1 = np.array(LST_dataset.variables['B9'])
rad2 = np.array(another.variables['B9'])
diff = rad1-rad2
radiances.append(diff)



radiances.append(valueOfBand(LST_dataset, "B1"))
radiances.append(valueOfBand(LST_dataset, "B2"))
radiances.append(valueOfBand(LST_dataset, "B3"))
radiances.append(valueOfBand(LST_dataset, "B4"))
radiances.append(valueOfBand(LST_dataset, "B5"))
radiances.append(valueOfBand(LST_dataset, "B6"))
radiances.append(valueOfBand(LST_dataset, "B7"))
radiances.append(valueOfBand(LST_dataset, "B8"))
radiances.append(valueOfBand(LST_dataset, "B9"))
#radiances.append(valueOfBand(LST_dataset, "B10"))
radiances.append(valueOfBand(LST_dataset, "B8A"))
radiances.append(valueOfBand(LST_dataset, "B11"))
radiances.append(valueOfBand(LST_dataset, "B12"))




drawPlot(radiances)

plt.show()



"""



"""
try:
    radiances.append(valueOfBand(another, "B8"))
    diff = radiances[0] - radiances[1]
    drawPlot(radiances[0], radiances[1], diff)

except:
    print("ubit cu se")


"""




"""
temps = np.array(LST_dataset.variables['LST'])
temps_c = np.array([(temp * 0.002) + 290 - 272.15 for temp in temps])

print("Temperature measurements: {0}, max-temp: {1:.2f} C, min temp: {2:.2f} C, avg temp: {3:.2f} C".format(
    len(temps_c), np.max(temps_c), np.min(temps_c), np.average(temps_c)))

plt.imshow(temps_c,cmap='viridis', interpolation='nearest')

# from matplotlib.colors import LogNorm
# plt.imshow(temps_c,cmap='viridis', interpolation='nearest', norm = LogNorm())

plt.colorbar()

plt.show()
"""

rad2 = np.array(LST_dataset.variables['B6'])
rad1 = np.array(another.variables['B6'])

rad2, rad1 = rad2[8070:8250, 1200:1600], rad1[8070:8250, 1200:1600]

dif = rad1 - rad2

f = plt.figure()
f.add_subplot(1, 3, 1)
plt.imshow(rad1,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(1, 3, 2)
plt.imshow(rad2,cmap='inferno', interpolation='sinc')
plt.colorbar()

f.add_subplot(1, 3, 3)
plt.imshow(dif,cmap='inferno', interpolation='sinc')
plt.colorbar()

plt.show()



