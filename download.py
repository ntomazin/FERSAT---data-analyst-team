import os
import requests
from datetime import date, datetime, timedelta

url    = "https://scihub.copernicus.eu/dhus/search?format=json&"
usr    = "test"
passwd = "test"

#hehe = "https://scihub.copernicus.eu/dhus/search?format=json&start=0&rows=4&q=footprint:%22Intersects(POLYGON((12.45%2042.20,%2019.50%2042.20,%2019.50%2046.60,%2012.45%2046.60,%2012.45%2042.20)))%22%20AND%20beginposition:[NOW-3DAYS%20TO%20NOW]%20AND%20endposition:[NOW-3DAYS%20TO%20NOW]"
footprint = "footprint:%22Intersects(POLYGON((12.45%2042.20,%2019.50%2042.20,%2019.50%2046.60,%2012.45%2046.60,%2012.45%2042.20)))%22"
dates = "beginposition:[NOW-3DAYS%20TO%20NOW]%20AND%20endposition:[NOW-3DAYS%20TO%20NOW]"

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
                download = requests.get(link, auth=(usr, passwd))
                print(f"Status code: {download.status_code}")
                with open(f"netCDF/{name}.nc", "wb") as fout:
                    fout.write(download.content)
                break;

            for file in files:
                link = file["link"][0]["href"]
                name = file["title"]
                print(link)
                print(name)
                download = requests.get(link, auth=(usr, passwd))
                print(f"Status code: {download.status_code}")
                with open(f"netCDF/{name}.rar", "wb") as fout:
                    fout.write(download.content)

            start += row
            if len(files) != row:
                print(f"kraj, ostalo je samo {len(files)} fajlova")
                break;
            break;
        except:
            break


"""
    This program downloads Sentinel data for Croatia in rectangular shape.
    Currently it is hardcoded with coordinates and downloading data for the last 3 days.
"""
if __name__ == "__main__":
    #print("IDEMO")
    downloads()
