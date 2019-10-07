from netCDF4 import Dataset

rootgrp = Dataset("/home/piki/Desktop/faks/FERSAT/downloaded_data/test.nc", "a", format="NETCDF4")

#print(rootgrp.data_model)
print(rootgrp)


#plin = rootgrp.createGroup("CO2")

#print(rootgrp.groups)





#print (rootgrp.dimensions)
#OrderedDict([
#             ("lat", <netCDF4._netCDF4.Dimension object at 0x1b480f8>),
#             ("lon", <netCDF4._netCDF4.Dimension object at 0x1b48a08>)
#            ])

#print(rootgrp.dimensions["lat"])

rootgrp.close()