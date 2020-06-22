import os
from glob import glob
import time

# set up directories and working environment
odir = "C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\Clipped\\Pakistan_Clipped\\"
idir = "C:\\Users\\Karthik.P\\OneDrive\\Desktop\\"
inMask = "C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\Shape\\Pakistan_Shape\\PAK_adm0-2.shp"

start = time.time()

# read files into list
filelist = [f for f in glob(idir+"**/*.tif")]
filelist.sort()
print(filelist)
print()
print("Length of the filelist: " + str(len(filelist)))
print()

name =  os.path.basename(filelist[0])
os.chdir(odir[:-1])
command = 'mkdir ' + name.split('.')[2]
os.system(command)
odir = odir + name.split('.')[2] + "\\"

# a loop for clipping
for files in filelist:
    print(files)
    filename = os.path.basename(files)
    newname = 'Pakistan_prcp_'+ filename.split('.')[2] + filename.split('.')[3] +\
                filename.split('.')[4]+'.tif'
    outputfile = odir+newname
    cmd = 'gdalwarp -dstnodata -9999 -q\
            -cutline %s -crop_to_cutline %s %s'\
            % (inMask, files, outputfile)           # the command line to clip the raster
    os.system(cmd)
    print(newname+' is done.')
end = time.time()

print('The process took %.2f minutes.' % ((end-start)/60))
