import os
from glob import glob
import gdal
import numpy as np
import netCDF4 as nc4
from netCDF4 import Dataset
import datetime
import gc

wdir = 'C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\Clipped\\India_Clipped'
odir = 'C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\NetCDF\\'

beg = datetime.datetime.now()
dtstamp = datetime.datetime.now().strftime("%Y%m%d")

# Create arrays for lat and long, netCDF file, add dimensions
ds = gdal.Open(wdir+"\\2006\\India_prcp_20060417.tif")
b = ds.GetGeoTransform()
lon = np.arange(585)*b[1]+b[0]
lat = np.arange(606)*b[5]+b[3]
ncfile = nc4.Dataset(odir + "India_prcp_monthly.nc", "w", format="NETCDF4")
ncfile.createDimension('lat',606)
ncfile.createDimension('lon',585)
ncfile.createDimension('time',372)
lato = ncfile.createVariable('lat', 'f4', ('lat'))
lato.units = 'degrees_north'
lato.long_name = 'latitude'
lono = ncfile.createVariable('lon', 'f4', ('lon'))
lono.units = 'degrees_east'
lono.long_name = 'longitude'

time = ncfile.createVariable('time','f4', ('time'))
today = datetime.datetime.today()
ncfile.history = "Created " + today.strftime("%d/%m/%y")
time.units = 'days since 1900-01-01 00:00:00.0 UTC'
time.calendar = 'gregorian'
time.long_name = 'time'
zeroce = datetime.datetime.strptime("1900001","%Y%j")

thevar = ncfile.createVariable('prcp', 'f4', ('lat', 'lon','time'))
thevar.standard_name = 'Precipitation'
thevar.units = 'mm'
thevar.missing_value = -9999

flist = glob(wdir+"/**/*.tif")
flist.sort()
print(len(flist))
#alist=[]
count = 0
j=0
dd = 1
lato[:] = lat
lono[:] = lon
for yyyy in range(1989,2020):
    if yyyy%4 != 0:
        Feb = 28
    elif yyyy%100 == 0 and yyyy%400!=0:
        Feb = 28
    else:
        Feb = 29
    for mm in range(1,13):
        if mm in [1,3,5,7,8,10,12]:
            days = 31
        elif mm == 2:
            days = Feb
        elif mm in [4,6,9,11]:
            days = 30
        month_ag = []
        start = count
        end = count+days
        print(start,days,end)
        print(flist[start:end])
        for prcp in flist[start:end]:
            #print(prcp)
            ds = gdal.Open(prcp)
            ds_array = ds.ReadAsArray()
            ds_array[ds_array==-9999]= np.nan
            month_ag.append(ds_array)
        count = end
        #print(count)
        date = datetime.datetime(yyyy,mm,dd)
        print(date)
        gregorian_day = (date-zeroce).total_seconds()/86400
        time[j] = gregorian_day
        #month_ag[month_ag%9999==0] = np.nan
        #alist.append(month_ag)
        fpcp = np.sum(month_ag, axis = 0)
        thevar[:,:,j] = fpcp
        j = j + 1
        del month_ag
    gc.collect()
ncfile.close()

end = datetime.datetime.now()
dur = end - beg
print(dur)
