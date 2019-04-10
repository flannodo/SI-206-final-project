##SI 206 W19 final project
##Group Name: Flashing Rainbow
##Group Members: Flannery O'Donnell and Katherine Berry

import billboard
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import sqlite3
import json

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
cur.execute('CREATE TABLE Billboard_top(rank INTEGER, title TEXT, artist TEXT)') 
for song in billboard_top:
    _rank = song.rank
    _title = song.title
    _artist = song.artist
    cur.execute("INSERT INTO Billboard_top (rank, title, artist) VALUES (?, ?, ?)", (_rank, _title, _artist))
conn.commit() #commit the changes to the database

#GET DATA FROM SPOTIFY
conn = sqlite3.connect('Spotify_top.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Spotify_top')
cur.execute('CREATE TABLE Spotify_top(title TEXT, artist TEXT)')
for i in range(0,100,20):
    track_results = sp.search(q='year:2019', type='track', limit=20, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):    
        __title = t['artists'][0]['name']
        __artist = t['name'] 
        cur.execute("INSERT INTO Spotify_top (title, artist) VALUES (?, ?)", (__title, __artist))
conn.commit()

