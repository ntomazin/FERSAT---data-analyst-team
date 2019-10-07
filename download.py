import os
import requests
from datetime import date, datetime, timedelta



url    = "https://scihub.copernicus.eu/dhus/search?format=json&"
usr    = "pikiens"
passwd = "pikiens1908"

#hehe = "https://scihub.copernicus.eu/dhus/search?format=json&start=0&rows=10&q=footprint:%22Intersects(POLYGON((12.45%2042.20,%2019.50%2042.20,%2019.50%2046.60,%2012.45%2046.60,%2012.45%2042.20)))%22%20AND%20beginposition:[NOW-3DAYS%20TO%20NOW]%20AND%20endposition:[NOW-3DAYS%20TO%20NOW]"
#footprint = "footprint:%22Intersects(POLYGON((12.45 42.20, 19.50 42.20, 19.50 46.60, 12.45 46.60, 12.45 42.20)))%22"     #only has to match this area in a single dot, not whole area
#footprint = "footprint:%22Intersects(46.50, 16.35)%22 AND footprint:%22Intersects(45.50, 13.5)%22 AND footprint:%22Intersects(42.40, 18.5)%22 AND footprint:%22Intersects(45.20, 19.4)%22" #Croatia footprint
footprint = "footprint:%22Intersects(43.55, 16.45)%22 AND footprint:%22Intersects(43.50, 16.45)%22 AND footprint:%22Intersects(43.50, 16.35)%22 AND footprint:%22Intersects(43.55, 16.35)%22" #Marjan forest
#footprint = "footprint:%22Intersects(45.40, 14.80)%22 AND footprint:%22Intersects(45.00, 15.00)%22 AND footprint:%22Intersects(44.80, 15.60)%22 AND footprint:%22Intersects(45.40, 15.40)%22" #Gorski Kotar

#dates = "beginposition:[NOW-3DAYS%20TO%20NOW]%20AND%20endposition:[NOW-3DAYS%20TO%20NOW]"
#dates = "beginposition:[2018-04-01T00:00:00.000Z TO 2018-04-04T00:00:00.000Z]%20AND%20endposition:[2018-04-01T00:00:00.000Z TO 2018-04-04T00:00:00.000Z]"

from DownloadGUI import main

dateFrom, dateTo = main()
print(str(dateFrom) + " "+ str(dateTo))
dates = "beginposition:[" + str(dateFrom) + "T00:00:00.000Z TO " + str(dateTo) + "T00:00:00.000Z] AND endposition:[" + str(dateFrom) + "T00:00:00.000Z TO " + str(dateTo) + "T00:00:00.000Z]"
def downloads():

    start = 0
    row = 10
    while True:
        fullUrl = f"{url}start={start}&rows={row}&q={footprint} AND {dates}"
        print(fullUrl)
        req_offline = requests.get(fullUrl, auth=(usr, passwd))
        #print(req_offline.json())
        try:
            files = req_offline.json()["feed"]["entry"]
            try:
                first = files[0]
            except:
                link = files["link"][0]["href"]
                name = files["title"]
                size = files["summary"].split("\\s")
                #print(size)

                if size[len(size) - 1] == "GB" and float(size[len(size) - 2]) > 2:      #if size[len(size) - 1] == "MB" and float(size[len(size) - 2]) > 100 or size[len(size) - 1] == "GB":
                    fileSize = size[len(size) - 2] + size[len(size) - 1]
                    print("FILE TOO LARGE: " + fileSize)
                    break
                if not name.startswith("S2"):
                    print ("WRONG SATTELITE")
                    break

                download = requests.get(link, auth=(usr, passwd))
                print(f"Status code: {download.status_code}")
                with open(f"netCDF/{name}.nc", "wb") as fout:
                    fout.write(download.content)
                break

            for file in files:
                link = file["link"][0]["href"]
                name = file["title"]
                size = file["summary"].split()
                print(link)
                print(name)
                #print(size)
                if size[len(size) - 1] == "GB" and float(size[len(size) - 2]) > 2:      #if size[len(size) - 1] == "MB" and float(size[len(size) - 2]) > 100 or size[len(size) - 1] == "GB":
                    fileSize = size[len(size) - 2] + size[len(size) - 1]
                    print("FILE TOO LARGE: " + fileSize)
                    continue
                #if not name.startswith("S2"):
                #    print ("WRONG SATTELITE")
                #    continue

                download = requests.get(link, auth=(usr, passwd))
                print(f"Status code: {download.status_code}")
                with open(f"GKotar/{name}.rar", "wb") as fout:
                    fout.write(download.content)

            if len(files) != row:
                break
            else:
                start += row
        except:
            break


"""
    This program downloads Sentinel data for Croatia in rectangular shape.
    Currently it is hardcoded with coordinates and downloading data for the last 3 days.
"""
if __name__ == "__main__":
    #print("IDEMO")
    downloads()