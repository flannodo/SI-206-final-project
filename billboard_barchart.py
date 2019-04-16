import sqlite3
import matplotlib
import json
import matplotlib.pyplot as plt
import numpy as np 

#Calculate data from Billboard.com
conn = sqlite3.connect("Billboard_top.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Billboard_top")
artist_dict = {}
for row in cur:
    artist = row[1]
    artist_dict[artist] = artist_dict.get(artist, 0) + 1

with open('billboard_data.text', 'w') as outfile:
    json.dump(artist_dict, outfile) 

#Assign the x values to the keys of the dictionary and the y values to the values that correspond to those keys
xvals = artist_dict.keys()
yvals = artist_dict.values() 

#Plot the bar chart with xvals and yvals. Align the bars in center and assign a color to each bar.
index = np.arange(len(xvals))
plt.bar(index, yvals, align='center', width =1.0, color = ["green"])

#Give ylabel to the plot
plt.ylabel("Number of Songs Artist has on Billboard Top 100 List")

#Give xlabel to the plot
plt.xlabel("Artist Name")

#Give the title to the plot
plt.title("Amount of Songs Each Artist Has on the Billboard Top 100 List") 

#Adjust the placement of the x-axis labels 
plt.xticks(index, xvals, rotation=90, fontsize = 4) 

#Save the plot as a .png file
plt.savefig("billboard_artist_freq.png")

#Show the plot
plt.show()