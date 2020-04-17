import os
import csv

cereal_csv = os.path.join('..','Resources', 'cereal.csv')

with open(cereal_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader, None)
    
    
    
    for x in csv_reader:
        
        if float(x[7]) >= 5:
            print(x[0] + ' has ' + x[7] + ' of Fiber.')
            

        
