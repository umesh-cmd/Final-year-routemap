import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd
import matplotlib.cm
import os
from mpl_toolkits.basemap import Basemap
from geopandas import GeoDataFrame
from matplotlib.patches import Polygon

from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import numpy as np
from csv import reader
import relative_sphe as rsc


elv = 5.0e2
earth_radius = 6.378e6
gsat15_lon = 93.5
gsat15_elv = 3.5782e7

def beamangle(x,y):
    x=float(x)
    y=float(y)
    loc= (earth_radius+elv, 90.0-x, y)
    gsat15= (earth_radius+gsat15_elv, 90.0, gsat15_lon)
    loc_gsat15 = rsc.rel_coord(loc, gsat15)
    loc_gsat15_local = [loc_gsat15[0],
                     loc_gsat15[1] - 90.0 + x,
                     loc_gsat15[2] - y]
    bsteer_cape = [loc_gsat15_local[1], loc_gsat15_local[2]]
    return (bsteer_cape)

'''
data = pd. read_csv ("IND_adm0.csv")
fig, ax = plt. subplots()

m= Basemap(resolution='c', projection='merc', lat_0=54.5, lon_0=-4.36, llcrnrlon=68., llcrnrlat=6., urcrnrlon=97., urcrnrlat=37.)

m.drawmapboundary(fill_color='#46bcec')

m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')

m.drawcoastlines()


m.readshapefile( 'IND_adm0', 'INDIA')

'''
os.chdir(r'C:\Users\Umesh\Downloads')

df = pd.read_csv("AnyConv.com__route.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)
gdf.plot()
plt.show()

lat=[]
long=[]

    

with open('AnyConv.com__route.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    i=0
    for row in csv_reader:
       if i==0:
           i=i+1
           continue
       
       x=float(row[0])
       y=float(row[1])
            
       a=beamangle(x,y)
       
                   
       print(a)
                   

                   

       


