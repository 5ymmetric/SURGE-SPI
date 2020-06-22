import arcpy, os, arcinfo
import time
from arcpy import env
from arcpy.sa import *

t0 = time.time()

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

# Select the folder containing raster files.  This script will use ALL of the raster files in the selected folder.
env.workspace = "C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\2019"

# Select the shapefile containing the polygons to use as boundaries for zonal statistics
watershedFeat = "C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\India_Districts_ADM2_GADM-shp\\India_Districts_ADM2_GADM.shp"

# Select output folder for saving the output - zonal tables (.dbf files)
outDir = "C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\DBF\\2019_Output\\"

x = arcpy.ListRasters()
count = 0
for raster in arcpy.ListRasters()[0:]: # the "0" can be replaced by the most recent result of "print ndx" in order to restart where the code stopped
	if raster.endswith('.tif'):
		print raster
		ndx = x.index(raster)#+1
		print("Index: " + str(ndx) + "	Day: " + str(ndx + 1))
		tableName = str(raster[11:19]) + ".dbf"
		outTable = outDir + tableName
		arcpy.gp.ZonalStatisticsAsTable_sa(watershedFeat,
			"ID_2", # Select an attribute in the shape file to identify polygons
			raster,
			outTable,
			"DATA","SUM")
		print(tableName + " ----> Done")
		count = count + 1
print("Total rasters processed === " + str(count))
arcpy.CheckInExtension("Spatial")

t1 = time.time()

print("Time elapsed: %.2f minutes" % ((t1 - t0)/60))

print("Done!")
