import sqlite3
import matplotlib
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