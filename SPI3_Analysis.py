import h5py
import numpy as np
import csv
from climate_indices import indices, compute
import time

start = time.time()

filename = 'C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\NetCDF\\Pakistan_prcp.nc'

with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[2]

    # Get the data
    data = list(f[a_group_key])
    # Since the dimensions of each matrix is the same, we can simply use the rows/column dimension in the first matrix
    rows = len(data[0])
    columns = len(data[0][0])
    gridded_spi = []
    for i in range(0, rows):
        row_spi = []
        for j in range(0, columns):
            pixel_precipitations = []
            for clipped_image in data:
                pixel_precipitations.append(clipped_image[i][j])
            spi = indices.spi(np.array(pixel_precipitations), 90, indices.Distribution.gamma, 1989, 1989, 2018, compute.Periodicity.daily)
            print('Spi')
            print(spi)
            print("Length of SPI: " + str(len(spi)))
            row_spi.append(spi)
        gridded_spi.append(row_spi)

    print()
    print("Rows: " + str(len(gridded_spi)))
    print("Coloums: " + str(len(gridded_spi[len(gridded_spi) - 1])))
    print()
    #print(gridded_spi)

    # Outputing the result as a CSV
    print("Writing truncated Results to CSV file.....")
    with open('test_Pakistan.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(gridded_spi)

    print("Quitting......(Done with test file)")
    quit()

    # Changing threshold to print the whole numpy array for SPI values
    np.set_printoptions(threshold=np.inf)

    # Outputing the result as a CSV
    print("Writing Results to CSV file.....")
    with open('spi3_Nebraska.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(gridded_spi)

    end = time.time()

    print('The process took %.2f minutes.' % ((end - start) / 60))
