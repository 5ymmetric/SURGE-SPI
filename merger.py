import os
import glob
import pandas as pd
import sys

#year = sys.argv[1]
os.chdir("C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\Combined\\")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ], axis=1)
#export to csv
combined_csv.to_csv("combined.csv", index=False, encoding='utf-8-sig')
