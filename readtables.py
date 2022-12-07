import pandas as pd
import os

#read data from .cvs files in folder

directory = input("Enter the name of your folder: ")

#go find the files
for filename in os.list.dir(directory):
    f = os.path.join(directory, filename)

    #check if file
    if os.path.isfile(f):
        print(f'Processing {f}')

        #read tables and perform projection calucaltions
        data = pd.read_table(f, delimiter = ",")
        data['2023 Projected'] = data['2022 Revenue'] * 1.06

        #print to concole & write to file
        print(data)
        data.to_csv(f, sep=',')
