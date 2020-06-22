import os

command = 'process_climate_indices --index spi --periodicity monthly --netcdf_precip \\data\\India_prcp_monthly.nc --var_name_precip prcp --output_file_base \\data\\India --scales 3 6 12 --calibration_start_year 1989 --calibration_end_year 2019 --multiprocessing all'

os.system(command)
