import sqlite3
import matplotlib
import json
import matplotlib.pyplot as plt
import numpy as np 

#Calculate data from Spotify
conn = sqlite3.connect("Spotify_top.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Spotify_top")
spotify_artist_dict = {}
for row in cur:
    spotify_artist = row[1]
    spotify_artist_dict[spotify_artist] = spotify_artist_dict.get(spotify_artist, 0) + 1

with open('spotify_data.text', 'w') as outfile:
    json.dump(spotify_artist_dict, outfile) 

#Assign the x values to the keys of the dictionary and the y values to the values that correspond to those keys
x_values = spotify_artist_dict.keys()
y_values = spotify_artist_dict.values() 

#Plot the bar chart with xvals and yvals. Align the bars in center and assign a color to each bar.
index = np.arange(len(x_values))
plt.bar(index, y_values, align='center', width =1.0, color = ["blue"])

#Give ylabel to the plot
plt.ylabel("Number of Songs Artist has on Spotify Top 100 List")

#Give xlabel to the plot
plt.xlabel("Artist Name")

#Give the title to the plot
plt.title("Amount of Songs Each Artist Has on the Spotify Top 100 List") 

#Adjust the placement of the x-axis labels 
plt.xticks(index, x_values, rotation=90, fontsize = 4) 

#Save the plot as a .png file
plt.savefig("spotify_artist_freq.png")

#Show the plot
plt.show()