import sqlite3
import matplotlib
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

#Get the data from Spotify that needs to be plotted on x-axis
x_values = ['J. Cole', 'Lil Nas X', 'Billie Eilish', 'Jonas Brothers', 'Ariana Grande', 'Mustard', 'YNW Melly', 'Juice WRLD', 'Khalid', 
    'Sam Smith', 'Cardi B', 'Lauv', 'Marshmello', 'Lil Skies', 'Daddy Yankee', 'Mabel', 'benny blanco', 'Offset', 'Maren Morris', 'Nipsey Hussle', 
    'Khelani', 'Logic', 'Ozuna', 'FLETCHER', 'Anuel Aa', 'Rich The Kid', 'Polo G', 'Tory Lane', 'Bebe Rexha', 'YK Osiris', 'NLE Choppa', 
    'Blueface', 'ScHoolboy Q', 'Post Malone', 'Lil Uzi Vert', 'P!nk', 'Future', 'Lil Peep', 'YUNGBLUD', 'Maluma', 'Bazzi']

#Get the data from Spotify that needs to be plotted on y-axis
y_values = [spotify_artist_dict['J. Cole'], spotify_artist_dict['Lil Nas X'], spotify_artist_dict['Billie Eilish'], spotify_artist_dict['Jonas Brothers'], 
    spotify_artist_dict['Ariana Grande'], spotify_artist_dict['Mustard'], spotify_artist_dict['YNW Melly'], spotify_artist_dict['Juice WRLD'], 
    spotify_artist_dict['Khalid'], spotify_artist_dict['Sam Smith'], spotify_artist_dict['Cardi B'], spotify_artist_dict['Lauv'], 
    spotify_artist_dict['Marshmello'], spotify_artist_dict['Lil Skies'], spotify_artist_dict['Daddy Yankee'], spotify_artist_dict['Mabel'], 
    spotify_artist_dict['benny blanco'], spotify_artist_dict['Offset'], spotify_artist_dict['Maren Morris'], spotify_artist_dict['Nipsey Hussle'], 
    spotify_artist_dict['Kehlani'], spotify_artist_dict['Logic'], spotify_artist_dict['Ozuna'], spotify_artist_dict['FLETCHER'], 
    spotify_artist_dict['Anuel Aa'], spotify_artist_dict['Rich The Kid'], spotify_artist_dict['Polo G'], spotify_artist_dict['Tory Lanez'], 
    spotify_artist_dict['Bebe Rexha'], spotify_artist_dict['YK Osiris'], spotify_artist_dict['NLE Choppa'], spotify_artist_dict['Blueface'], 
    spotify_artist_dict['ScHoolboy Q'], spotify_artist_dict['Post Malone'], spotify_artist_dict['Lil Uzi Vert'], spotify_artist_dict['P!nk'], 
    spotify_artist_dict['Future'], spotify_artist_dict['Lil Peep'], spotify_artist_dict['YUNGBLUD'], spotify_artist_dict['Maluma'], spotify_artist_dict['Bazzi']]

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