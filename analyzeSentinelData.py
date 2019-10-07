from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

LST_dataset = Dataset('E:\FERSAT\Marjan\S2A_MSIL2A_20170806T095031_N0205_R079_T33TXJ_20170806T095744_resampled.nc')
another_dataset = Dataset('E:\FERSAT\Marjan\S2A_MSIL2A_20190217T095051_N0211_R079_T33TXJ_20190217T123757_resampled.nc')
# print(LST_dataset.variables['LST_orphan'])
#print(LST_dataset.variables['B8'])
radiances = np.array(LST_dataset.variables['B8'])
print("Radiance measurements: {0}, max radiance: {1:.2f} C, min radiance: {2:.2f} C, avg radiance: {3:.2f} C".format(
    len(radiances), np.max(radiances), np.min(radiances), np.average(radiances)))

another = np.array(another_dataset.variables['B8'])
print("Radiance measurements: {0}, max radiance: {1:.2f} C, min radiance: {2:.2f} C, avg radiance: {3:.2f} C".format(
    len(another), np.max(another), np.min(another), np.average(another)))

dif = radiances - another

f = plt.figure()
f.add_subplot(1, 3, 1)
plt.imshow(radiances,cmap='inferno', interpolation='nearest')
plt.colorbar()

f.add_subplot(1, 3, 2)
plt.imshow(another,cmap='inferno', interpolation='nearest')
plt.colorbar()

f.add_subplot(1, 3, 3)
plt.imshow(dif,cmap='inferno', interpolation='nearest')
plt.colorbar()

plt.show()



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