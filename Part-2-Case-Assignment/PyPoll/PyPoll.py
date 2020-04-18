#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:31:31 2020

@author: pariya
"""
import os
import csv

csv_path = os.path.join('../PyPoll/Resources/election_data.csv')

#Lists to store data

voter_id = [] 
county = []
candidate = []

with open(csv_path) as pypoll_csv:
    
    csvreader = csv.reader(pypoll_csv, delimiter=',')
    header = next(csvreader)
    
    for line in csvreader:
        
        #define columns
        voter_id = pypoll_csv[0]
        county = pypoll_csv[1]
        candidate = pypoll_csv[2]
        
     
      
