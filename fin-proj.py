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


billboard_chart = billboard.ChartData('hot-100') #Get the current Top 100 Chart

conn = sqlite3.connect('Billboard_data.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Billboard_data')
cur.execute('CREATE TABLE Billboard_data(rank INTEGER, title TEXT, artist TEXT)') 
for song in billboard_chart:
    _rank = song.rank
    _title = song.title
    _artist = song.artist
    cur.execute("INSERT INTO Billboard_data (rank, title, artist) VALUES (?, ?, ?)", (_rank, _title, _artist))
conn.commit() #commit the changes to the database
