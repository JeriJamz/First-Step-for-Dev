import pandas as pd, os

# Read in data from all .csv files in folder

directory = input('Enter the name of your folder: ')


#Iterate over all files in the folder

for filename in od.listdir(directory):
    f = os.path.join(directory, filename)

    #check if file
    if os.path.isfile(f):
        print(f'processing {f}')

        #read tables and preform projection calculation
        data = pd.read_table(f, delimiter = ',')
        data['2023 Projected'] = data['2022 Revenue'] * 1.06

        #print to console & write to file
        print(data)
        data.to_csv(f, sep=',')
