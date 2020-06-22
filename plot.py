import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


wdir = "C:\\Users\\Karthik.P\\OneDrive\\Desktop\\Research_SPI_Calculations\\Output\\spi3_Nebraska.csv"

test = pd.read_csv(wdir)
array = np.array(test)

print(np.shape(array))
print()
np.set_printoptions(threshold=np.inf)

# for i in range(0, 59):
#     for j in range(0, 175):
#         array[i][j] = list(map(float, array[i][j].strip('[]').split()))
#         print("Done")
