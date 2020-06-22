import numpy as np
from netCDF4 import Dataset
nc = Dataset('C:\\Users\\kpagilla2\\Downloads\\India_spi_gamma_03.nc','r')
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
    d = np.array(nc.variables['spi_gamma_03'], dtype=type(nc.variables))
    print(d[26, 36, 0])
