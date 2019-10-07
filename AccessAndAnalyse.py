from sentinelsat import SentinelAPI
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
