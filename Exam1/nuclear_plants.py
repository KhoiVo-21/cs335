#!/usr/bin/python

import sys, math, csv, urllib

def distance(una, plant):
  # Calculate the great circle distance between two points 
  # on the earth (specified in decimal degrees)
  # **** una and plant are coordiante tuples
  
  # convert decimal degrees to radians for each coordinate tuple
  unaRad = (math.radians(una[0]), math.radians(una[1]))
  plantRad = (math.radians(plant[0]), math.radians(plant[1]))
  # haversine formula 
  dlon = plantRad[0] - unaRad[0] 
  dlat = plantRad[1] - unaRad[1] 
  a = math.sin(dlat/2)**2 + math.cos(unaRad[1]) * math.cos(plantRad[1]) * math.sin(dlon/2)**2
  c = 2 * math.asin(math.sqrt(a)) 
  mi = 3953 * c
  return mi
  
def main ():
    text = urllib.urlopen("http://una.dbms.rocks/assets/python/nuclear-plants.csv")
    if text.info().gettype() == "csv":
        print text
    # with open(text, 'r') as csv_file:
    #     reader = csv.reader(csv_file)
    
    # for row in reader:
    #     print row
    
    
if __name__ == "__main__":
    main()