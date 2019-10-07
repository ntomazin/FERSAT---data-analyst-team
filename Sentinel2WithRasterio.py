import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
#%matplotlib inline

imagePath = '/home/piki/PycharmProjects/FERSAT/S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/GRANULE/L2A_T33TVK_A005296_20180312T100018/IMG_DATA/R10m/'
band2 = rasterio.open(imagePath+'L2A_T33TVK_20180312T100019_B02_10m.jp2', driver='JP2OpenJPEG') #blue
band3 = rasterio.open(imagePath+'L2A_T33TVK_20180312T100019_B03_10m.jp2', driver='JP2OpenJPEG') #green
band4 = rasterio.open(imagePath+'L2A_T33TVK_20180312T100019_B04_10m.jp2', driver='JP2OpenJPEG') #red
band8 = rasterio.open(imagePath+'L2A_T33TVK_20180312T100019_B08_10m.jp2', driver='JP2OpenJPEG') #nir


#multiple band representation
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
plot.show(band2, ax=ax1, cmap='Blues')
plot.show(band3, ax=ax2, cmap='Greens')
plot.show(band4, ax=ax3, cmap='Reds')
fig.tight_layout()

#export true color image
trueColor = rasterio.open('/home/piki/PycharmProjects/FERSAT/S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/Output/SentinelTrueColor2.tiff','w',driver='Gtiff',
                         width=band4.width, height=band4.height,
                         count=3,
                         crs=band4.crs,
                         transform=band4.transform,
                         dtype=band4.dtypes[0]
                         )
trueColor.write(band2.read(1),3) #blue
trueColor.write(band3.read(1),2) #green
trueColor.write(band4.read(1),1) #red
trueColor.write(band8.read(1),4) #red

trueColor.close()
src = rasterio.open(r"/home/piki/PycharmProjects/FERSAT/S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/Output/SentinelTrueColor2.tiff", count=3)
plot.show(src)


#export false color image
falseColor = rasterio.open('/home/piki/PycharmProjects/FERSAT/S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/Output/SentinelFalseColor.tiff', 'w', driver='Gtiff',
                          width=band2.width, height=band2.height,
                          count=3,
                          crs=band2.crs,
                          transform=band2.transform,
                          dtype='uint16'
                         )
falseColor.write(band3.read(1),3) #Blue
falseColor.write(band4.read(1),2) #Green
falseColor.write(band8.read(1),1) #Red
falseColor.close()
#generate histogram
#trueColor = rasterio.open('/home/piki/PycharmProjects/FERSAT/S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/Output/SentinelTrueColor2.tiff')
#plot.show_hist(trueColor, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")

import sentinelsat as SentinelAPI
import rasterio as rio


user = 'pikiens'
password = 'pikiens1908'
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

# Open Bands 4, 3 and 2 with Rasterio
R10 = 'S2B_MSIL2A_20180312T100019_N0206_R122_T33TVK_20180312T124613.SAFE/GRANULE/L2A_T33TVK_A005296_20180312T100018/IMG_DATA/R10m'
b4 = rio.open(R10+'/L2A_T33TVK_20180312T100019_B04_10m.jp2')
b3 = rio.open(R10+'/L2A_T33TVK_20180312T100019_B03_10m.jp2')
b2 = rio.open(R10+'/L2A_T33TVK_20180312T100019_B02_10m.jp2')


# Create an RGB image
with rio.open('RGB.tiff','w',driver='Gtiff', width=b4.width, height=b4.height,
              count=3,crs=b4.crs,transform=b4.transform, dtype=b4.dtypes[0]) as rgb:
    rgb.write(b2.read(1),1)
    rgb.write(b3.read(1),2)
    rgb.write(b4.read(1),3)
    rgb.close()