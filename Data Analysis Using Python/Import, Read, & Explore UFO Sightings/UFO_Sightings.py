#!/usr/bin/env python
# coding: utf-8

# # Module 1

# #### In this assignment, you will work with ufo sightings data.
# - The data includes various data points about individual ufo sightings
# - Data File(s): ufo-sightings.csv



'''
1. Import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''

import csv
filepath = "ufo-sightings.csv"
ufosightings = [] 

with open("ufo-sightings.csv", "r") as cvsfile:
    reader = csv.DictReader(cvsfile)
    
    ufosightings = [] 
    
    for row in reader:
        ufosightings.append(row)




'''
2. How many sightings were there in total?  Put the count in "ufosightings_count" and print the result.
'''


ufosightings_count = len(ufosightings)

print("Total number of sightings is", ufosightings_count)




'''
3. How many sightings were there in the US?  Put the US sightings in "sightings_us" and print.
'''

sightings_us = [row for row in ufosightings if row["country"] == "us"]

print("The number of sightings in the US is", sightings_us)



'''
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".
'''

#First, define a Python function that checks if a given duration (seconds) is "valid"
def is_valid_duration(duration_as_string):
    try:
        duration = float(duration_as_string)
    
    except ValueError:
        
        return False
    
    else:
        
        return duration > 10
    
fball=[]
    
fball = [row for row in sightings_us if(row["shape"] == "fireball" and is_valid_duration(row["duration (seconds)"]))]

for fsighting in fball:
    print("Datetime of firball is", fsighting["datetime"], "and it was located in", fsighting["state"])



'''
5. Sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''

fballsorted = sorted(fball, key = lambda x: float(x["duration (seconds)"]), reverse = True)

for row in fballsorted:
    print(row["duration (seconds)"], row["datetime"], row["state"])



'''
6. What state had the longest lasting "fireball"?   Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''


fball_max = max(fball, key = lambda x: float(x["duration (seconds)"]))

state = fball_max["state"]

print(fball_max["duration (seconds)"], state)



'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
Write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings

'''

def valid_sighting(string):
    try:
        duration = float(string)
        
    except ValueError:
        return False
    
    else:
        return duration > 0

filtered_sightings = [row for row in ufosightings if(valid_sighting(row["duration (seconds)"]))]

fball_min = min(filtered_sightings, key = lambda x: float(x["duration (seconds)"]))

min_duration = float(fball_min["duration (seconds)"])

print(min_duration)



'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

sightings_shapes = []

for row in ufosightings:
    sightings_shapes.append(row["shape"])

sightingsset = set(sightings_shapes)

count = {shape:sightings_shapes.count(shape) for shape in sightingsset}
    
sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)


top3shapes = [sorted_count[0], sorted_count[1], sorted_count[2]] 
    
print(top3shapes)





