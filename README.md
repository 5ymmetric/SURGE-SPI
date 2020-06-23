# SURGE
The overall goal of this for this project is to help predict social unrest. With worldwide instability and unrest, the Social Unrest Reconnaissance GazEtteer (SURGE) project was created to predict this underlying problem. It emphasizes making long-term predictions using dynamic social media data and multiagent simulations. This project’s overall goal is to devise a system--integrating data, creating novel algorithms, and conducting multi agent simulations--that automatically and accurately anticipate social unrest events. With this project, the purpose is to improve on the current distance function used to identify a conceptual neighborhood of a social unrest event, to more effectively group similar unrest events. This, in turn, enables the system to more accurately predict social unrest by including influences or impacts from neighboring events. A conceptual neighborhood is beyond just spatial distances, as the distance function also involves temporal, social-economic, and infrastructural gaps. Specifically, in this project, we will observe how additional factors, mainly provided by the Global Database of Events, Language, and Tone (GDELT) database, can contribute to this distance function through the implementation of more positively influenced factors. With different variables, SPI is potentially one of many influencers of social unrest. We will be focusing specifically on SPI here. This project is funded by the NGA and lead by Dr. Soh at the University of Nebraska-Lincoln.

# What is SPI?
The Standardized Precipitation Index (SPI) was developed by McKee et al. (1993, 1995) as a widely used indicator to characterize meteorological drought, which standardizes the rainfall deficits/excess on a temporal and regional basis. SPI expresses the actual rainfall as a standardized departure with respect to rainfall probability distribution function permitting comparisons across space and time. Computation of SPI requires long term, typically 30-50 years of data on precipitation to determine the probability distribution function, which is then transformed to a normal distribution with a mean of zero and standard deviation of one.

The SPI was designed to quantify the precipitation deficit for multiple timescales. The timescales can be of any length, but McKee and others (1993) initially calculated the SPI for 3-, 6-,12-, 24- and 48-month timescales. Statistically, 1–24 months is the best practical range of application (Guttman, 1994, 1999).

The positive (negative) SPI values are greater (less) than the median precipitation that is zero because of the standardization. The magnitude of the departure from zero is a probabilistic measure of the severity of a wet (+) or dry (-) condition (WMO, 2012; Guttman, 1999). 
  
SPI Value | Condictions
------------ | -------------
2.0+ | Extremely Wet
1.5 to 1.99 | Very Wet
1.0 to 1.49 | Moderately Wet
-0.99 to 0.99 | Near Normal
-1.0 to -1.49 | Moderately Dry
-1.5 to -1.99 | Very Dry
-2.0 and less | Extremely Dry

# Calculating SPI
1. First, we need to determine the No Data Value of our image
      1. Since precipitation from CHIRPS is from satellite, the developers had selected a magic number for areas where you wouldn’t care about. For example, we would not care about the precipitation in the Pacific so we would set the values around the Pacific Ocean to -9999. So when we see the number -9999 at any pixel, we can determine that that is a NoData value. 
      2. We can determine the NoData value by using QGIS or ArcGIS. For this example, we will us QGIS. First, open QGIS and then drive one of the raw images into the application. One the image is opened in the application, select the “Identify Features” button on the toolbar at the top. The keyboard for it on Windows 10 is Ctrl+Shift+I. Click on a pixel in the ocean and it should give you a value. Typically the value should be -9999. Now that we found our NoData value, we can look at the code. 
2. Clipping the Images
      1. Currently, everything is hardcoded, but can easily be changed for easier usage. Change the variable ‘odir’ to your desired out directory. Change the variable ‘idir’ to the location of your raw data. Change ‘inMash’ to the path of your Shapefile. 
      2. If your NoData value is not -9999, locate the ‘cmd’ variable. Within that variable, replace the value -9999 to the data’s actual NoData value.  
      3. Once all these changes are completed, run the script and it will begin clipping. **Please note, depending on how big your shapefiles are, this can take up a lot of space and use a lot of time.**
3. Aggregating Precipitation values over 30 years into a single NetCDF file
      1. Find the latitude and longitude of the required country by using GDAL.
      2. Currently, everything is hardcoded, but can easily be changed for easier usage. Change the variable ‘odir’ to your desired out directory. Change the variable ‘wdir’ to the location of your clipped images. Change ncfile.createDimension('lat',606) and ncfile.createDimension('lon',585) with the latitude and longitude found from the previous step.
      3. Once all these changes are completed, run the script and it will begin aggregating the clipped images over time. 
4. Compute SPI
      1. We use the command line tool provided by the climate_indices library to compute the SPI.
      2. Run the commandline_runner script by adjusting the periodicity, scales and variable names to compute the requred SPI.
      
# Additional Materials
* QGIS (https://www.qgis.org/en/site/)
* GDAL (https://gdal.org/)
* Precipitation Data CHRIPS: (ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0/global_daily/tifs/p05/)
* Shape Files: (https://data.humdata.org/)
* Climate Indices (https://github.com/monocongo/climate_indices)
* ArcGIS (https://www.arcgis.com/index.html)
