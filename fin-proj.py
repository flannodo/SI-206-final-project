##SI 206 W19 final project
##Group Name: Flashing Rainbow
##Group Members: Flannery O'Donnell and Katherine Berry

import billboard
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import sqlite3
import json
import matplotlib
import matplotlib.pyplot as plt

## Get your secret values to authenticate to Spotify.
cid = "4ff3fc5f0f7d4c018266c853f7f5e69e"
secret = "151610db800f47c291dbd685b5363128"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#GET DATA FROM BILLBOARD.COM 
billboard_top = billboard.ChartData('hot-100') #Get the current Top 100 Chart
billboard_artists = billboard.ChartData('artist-100') #Get the current Artist 100 Chart

conn = sqlite3.connect('Billboard_top.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Billboard_top')
cur.execute('CREATE TABLE Billboard_top(title TEXT, artist TEXT)') 
for song in billboard_top:
    _title = song.title
    _artist = song.artist
    cur.execute("INSERT INTO Billboard_top (title, artist) VALUES (?, ?)", (_title, _artist))
conn.commit() #commit the changes to the database

#GET DATA FROM SPOTIFY
conn = sqlite3.connect('Spotify_top.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Spotify_top')
cur.execute('CREATE TABLE Spotify_top(title TEXT, artist TEXT)')
for i in range(0,100,20):
    track_results = sp.search(q='year:2019', type='track', limit=20, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):    
        __title = t['name'] 
        __artist = t['artists'][0]['name']
        cur.execute("INSERT INTO Spotify_top (title, artist) VALUES (?, ?)", (__title, __artist))
conn.commit() #commit the changes to the database

#Calculate data from Billboard.com
conn = sqlite3.connect("Billboard_top.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Billboard_top")
artist_dict = {}
for row in cur:
    artist = row[1]
    artist_dict[artist] = artist_dict.get(artist, 0) + 1

#Get the data from Billboard.com that needs to be plotted on x-axis
xvals = ['Lil Nas X', 'Post Malone & Swae Lee', 'Ariana Grande', 'Post Malone', 'Halsey',
    'Cardi B & Bruno Mars', 'Billie Eilish', 'Jonas Brothers', 'Marshmello & Bastille', 'J. Cole',
    'Lady Gaga & Bradley Cooper', 'benny blanco, Halsey & Khalid', 'Blueface', 'Meek Mill Featuring Drake', 
    'Sam Smith & Normani', 'Khalid', 'Panic! At The Disco', 'Ava Max', 'Travis Scott', 'YNW Melly', '21 Savage', 
    'Maroon 5 Featuring Cardi B', 'Luke Combs', 'Ellie Goulding X Diplo Featuring Swae Lee', 'Dean Lewis', 
    'Lil Baby & Gunna', 'Lauren Daigle', 'Mustard & Migos', 'Cardi B', 'A Boogie Wit da Hoodie', 'Calboy', 
    '5 Seconds Of Summer', 'Pinkfong', 'Nipsey Hussle Featuring Roddy Ricch & Hit-Boy', 'Bad Bunny Featuring Drake', 
    'City Girls', 'Juice WRLD', 'Kodak Black Featuring Travis Scott & Offset', 'Dan + Shay', 'Brett Young', 
    'A Boogie Wit da Hoodie Featuring 6ix9ine', 'YNW Melly Featuring Kanye West', 'Marshmello Featuring CHVRCHES', 
    'The Chainsmokers Featuring 5 Seconds Of Summer', 'Yo Gotti Featuring Lil Baby', 'Daddy Yankee Featuring Snow', 
    'Blake Shelton', 'YK Osiris', 'Chase Rice', 'Lil Baby', 'Nipsey Hussle Featuring Belly & DOM KENNEDY', 
    'Imagine Dragons', 'Morgan Wallen', 'Kane Brown', 'Michael Ray', 'Ariana Grande & Victoria Monet', 'Kelsea Ballerini', 
    'Ella Mai', 'Old Dominion', 'Thomas Rhett', 'Riley Green', 'Summer Walker X Drake', 'FLETCHER', 
    'Lil Peep & iLoveMakonnen Featuring Fall Out Boy', 'P!nk', 'Khalid & Kane Brown', 'Nipsey Hussle Featuring YG', 
    'City Girls Featuring Cardi B', 'Maren Morris', 'Billie Eilish & Khalid', 'Pedro Capo X Farruko', 'DaBaby', 
    'Jon Pardi', 'Scotty McCreery', 'Lee Brice', 'benny blanco, Tainy Selena Gomez & J Balvin', 'Mabel', 
    'Nipsey Hussle Featuring Kendrick Lamar', 'Chris Stapleton', 'Florida Georgia Line', 'Ski Mask The Slump God', 
    'Jason Aldean', 'Polo G Featuring Lil Tjay']

#Get the data from Billboard.com that needs to be plotted on y-axis
yvals = [artist_dict['Lil Nas X'], artist_dict['Post Malone & Swae Lee'], artist_dict['Ariana Grande'], artist_dict['Post Malone'], artist_dict['Halsey'],
    artist_dict['Cardi B & Bruno Mars'], artist_dict['Billie Eilish'], artist_dict['Jonas Brothers'], artist_dict['Marshmello & Bastille'], artist_dict['J. Cole'],
    artist_dict['Lady Gaga & Bradley Cooper'], artist_dict['benny blanco, Halsey & Khalid'], artist_dict['Blueface'], artist_dict['Meek Mill Featuring Drake'], 
    artist_dict['Sam Smith & Normani'], artist_dict['Khalid'], artist_dict['Panic! At The Disco'], artist_dict['Ava Max'], artist_dict['Travis Scott'], artist_dict['YNW Melly'], artist_dict['21 Savage'], 
    artist_dict['Maroon 5 Featuring Cardi B'], artist_dict['Luke Combs'], artist_dict['Ellie Goulding X Diplo Featuring Swae Lee'], artist_dict['Dean Lewis'], 
    artist_dict['Lil Baby & Gunna'], artist_dict['Lauren Daigle'], artist_dict['Mustard & Migos'], artist_dict['Cardi B'], artist_dict['A Boogie Wit da Hoodie'], artist_dict['Calboy'], 
    artist_dict['5 Seconds Of Summer'], artist_dict['Pinkfong'], artist_dict['Nipsey Hussle Featuring Roddy Ricch & Hit-Boy'], artist_dict['Bad Bunny Featuring Drake'], 
    artist_dict['City Girls'], artist_dict['Juice WRLD'], artist_dict['Kodak Black Featuring Travis Scott & Offset'], artist_dict['Dan + Shay'], artist_dict['Brett Young'], 
    artist_dict['A Boogie Wit da Hoodie Featuring 6ix9ine'], artist_dict['YNW Melly Featuring Kanye West'], artist_dict['Marshmello Featuring CHVRCHES'], 
    artist_dict['The Chainsmokers Featuring 5 Seconds Of Summer'], artist_dict['Yo Gotti Featuring Lil Baby'], artist_dict['Daddy Yankee Featuring Snow'], 
    artist_dict['Blake Shelton'], artist_dict['YK Osiris'], artist_dict['Chase Rice'], artist_dict['Lil Baby'], artist_dict['Nipsey Hussle Featuring Belly & DOM KENNEDY'], 
    artist_dict['Imagine Dragons'], artist_dict['Morgan Wallen'], artist_dict['Kane Brown'], artist_dict['Michael Ray'], artist_dict['Ariana Grande & Victoria Monet'], artist_dict['Kelsea Ballerini'], 
    artist_dict['Ella Mai'], artist_dict['Old Dominion'], artist_dict['Thomas Rhett'], artist_dict['Riley Green'], artist_dict['Summer Walker X Drake'], artist_dict['FLETCHER'], 
    artist_dict['Lil Peep & iLoveMakonnen Featuring Fall Out Boy'], artist_dict['P!nk'], artist_dict['Khalid & Kane Brown'], artist_dict['Nipsey Hussle Featuring YG'], 
    artist_dict['City Girls Featuring Cardi B'], artist_dict['Maren Morris'], artist_dict['Billie Eilish & Khalid'], artist_dict['Pedro Capo X Farruko'], artist_dict['DaBaby'], 
    artist_dict['Jon Pardi'], artist_dict['Scotty McCreery'], artist_dict['Lee Brice'], artist_dict['benny blanco, Tainy, Selena Gomez & J Balvin'], artist_dict['Mabel'], 
    artist_dict['Nipsey Hussle Featuring Kendrick Lamar'], artist_dict['Chris Stapleton'], artist_dict['Florida Georgia Line'], artist_dict['Ski Mask The Slump God'], 
    artist_dict['Jason Aldean'], artist_dict['Polo G Featuring Lil Tjay']]

#Plot the bar chart with xvals and yvals. Align the bars in center and assign a color to each bar.
plt.bar(xvals, yvals, align='center', width =10.0, color = ["green"])

#Give ylabel to the plot
plt.ylabel("Number of Songs Artist has on Billboard Top 100 List")

#Give xlabel to the plot
plt.xlabel("Artist Name")

#Give the title to the plot
plt.title("Amount of Songs Each Artist Has on the Billboard Top 100 List") 

#Adjust the placement of the x-axis labels 
plt.xticks(xvals, rotation='vertical', fontsize = 4, va="bottom", ha='left') 

#Save the plot as a .png file
plt.savefig("billboard_artist_freq.png")

#Show the plot
plt.show()

#Calculate data from Spotify
conn = sqlite3.connect("Spotify_top.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Spotify_top")
spotify_artist_dict = {}
for row in cur:
    spotify_artist = row[1]
    spotify_artist_dict[spotify_artist] = spotify_artist_dict.get(artist, 0) + 1

#Get the data from Spotify that needs to be plotted on x-axis
x_values = ['J. Cole', 'Lil Nas X', 'Billie Eilish', 'Jonas Brothers', 'Ariana Grande', 'Mustard', 'YNW Melly', 'Juice WRLD', 'Khalid', 
    'Sam Smith', 'Cardi B', 'Lauv', 'Marshmello', 'Lil Skies', 'Daddy Yankee', 'Mabel', 'benny blanco', 'Offset', 'Maren Morris', 'Nipsey Hussle', 
    'Khelani', 'Logic', 'Ozuna', 'FLETCHER', 'Anuel Aa', 'Rich The Kid', 'Polo G', 'Tory Lane', 'Bebe Rexha', 'YK Osiris', 'NLE Choppa', 
    'Blueface', 'ScHoolboy Q', 'Post Malone', 'Lil Uzi Vert', 'P!nk', 'Future', 'Lil Peep', 'YUNGBLUD', 'Why Don’t We, Gunna']

#Get the data from Spotify that needs to be plotted on y-axis
y_values = [spotify_artist_dict['J. Cole'], spotify_artist_dict['Lil Nas X'], spotify_artist_dict['Billie Eilish'], spotify_artist_dict['Jonas Brothers'], 
    spotify_artist_dict['Ariana Grande'], spotify_artist_dict['Mustard'], spotify_artist_dict['YNW Melly'], spotify_artist_dict['Juice WRLD'], 
    spotify_artist_dict['Khalid'], spotify_artist_dict['Sam Smith'], spotify_artist_dict['Cardi B'], spotify_artist_dict['Lauv'], 
    spotify_artist_dict['Marshmello'], spotify_artist_dict['Lil Skies'], spotify_artist_dict['Daddy Yankee'], spotify_artist_dict['Mabel'], 
    spotify_artist_dict['benny blanco'], spotify_artist_dict['Offset'], spotify_artist_dict['Maren Morris'], spotify_artist_dict['Nipsey Hussle'], 
    spotify_artist_dict['Khelani'], spotify_artist_dict['Logic'], spotify_artist_dict['Ozuna'], spotify_artist_dict['FLETCHER'], 
    spotify_artist_dict['Anuel Aa'], spotify_artist_dict['Rich The Kid'], spotify_artist_dict['Polo G'], spotify_artist_dict['Tory Lane'], 
    spotify_artist_dict['Bebe Rexha'], spotify_artist_dict['YK Osiris'], spotify_artist_dict['NLE Choppa'], spotify_artist_dict['Blueface'], 
    spotify_artist_dict['ScHoolboy Q'], spotify_artist_dict['Post Malone'], spotify_artist_dict['Lil Uzi Vert'], spotify_artist_dict['P!nk'], 
    spotify_artist_dict['Future'], spotify_artist_dict['Lil Peep'], spotify_artist_dict['YUNGBLUD'], spotify_artist_dict['Why Don’t We, Gunna']]

#Plot the bar chart with xvals and yvals. Align the bars in center and assign a color to each bar.
plt.bar(x_values, y_values, align='center', width =10.0, color = ["blue"])

#Give ylabel to the plot
plt.ylabel("Number of Songs Artist has on Spotify Top 100 List")

#Give xlabel to the plot
plt.xlabel("Artist Name")

#Give the title to the plot
plt.title("Amount of Songs Each Artist Has on the Spotify Top 100 List") 

#Adjust the placement of the x-axis labels 
plt.xticks(x_values, rotation='vertical', fontsize = 4, va="bottom", ha='left') 

#Save the plot as a .png file
plt.savefig("spotify_artist_freq.png")

#Show the plot
plt.show()