# import statements should generally be the very first line in a module
import re

# select a keyword (user input)
keyword = raw_input("What keyword would you like to search for? ")

# while the keyword isn't a single word
while len(keyword.split()) > 1:
    keyword = raw_input("Please input a single word to search for! ")

# create a dictionary of song names to file names
songs = {
    "10 Day": {
        "14,400 Minutes": "14400minutes.txt",
        "Missing You": "missingyou.txt",
        "Nostalgia": "nostalgia.txt",
        "Windows": "windows.txt",
        "Brain Cells": "braincells.txt",
        "Long Time": "longtime.txt",
        "22 Offs": "22offs.txt",
        "U Got Me Fucked Up": "ugotmefuckedup.txt",
        "Family": "family.txt",
        "Juke Juke": "jukejuke.txt",
        "Fuck You Tahm Bout": "fuckyoutahmbout.txt",
        "Long Time II": "longtimeII.txt",
        "Prom Night": "promnight.txt",
        "Hey Ma": "heyma.txt"},
    "Acid Rap": {
        "Good Ass Intro": "goodassintro.txt",
        "Pusha Man / Paranoia": "pushamanparanoia.txt",
        "Cocoa Butter Kisses": "juice.txt",
        "Lost": "lost.txt",
        "Everybody's Something": "everybodyssomething.txt",
        "Interlude (That's Love)": "thatslove.txt",
        "Favorite Song": "favoritesong.txt",
        "NaNa": "nana.txt",
        "Smoke Again": "smokeagain.txt",
        "Acid Rain": "acidrain.txt",
        "Chain Smoker": "chainsmoker.txt",
        "Everything's Good (Good Ass Outro)": "everythingsgood.txt"},
    "Coloring Book": {
        "All We Got": "allwegot.txt",
        "No Problem": "noproblem.txt",
        "Summer Friends": "summerfriends.txt",
        "D.R.A.M. Sings Special": "special.txt",
        "Blessings": "blessings.txt",
        "Same Drugs": "samedrugs.txt",
        "Mixtape": "mixtape.txt",
        "Angels": "angels.txt",
        "Juke Jam": "jukejam.txt",
        "All Night": "allnight.txt",
        "How Great": "howgreat.txt",
        "Smoke Break": "smokebreak.txt",
        "Finish Line / Drown": "finishlinedrown.txt",
        "Blessings (Reprise)": "blessingsreprise.txt"},
}

# replace filenames with song lyrics
all_songs = {}
for album, album_songs in songs.iteritems():
    for song, filename in album_songs.iteritems():
        with open('songs/' + filename, 'r') as f:
            lyrics = f.read()
            songs[album][song] = lyrics
            all_songs[song] = lyrics

artist = "Chano"

# count and print for mixtapes!
print("")
print("%s said the word %s..." % (artist, keyword))

for album, songs in songs.iteritems():
    count = 0
    for song, lyrics in songs.iteritems():
        count += re.sub("[^\w]", " ", lyrics).split().count(keyword.lower())

    print("%d time%s on the mixtape %s!" % (count, "" if (count == 1) else "s", album))


# count and print for each song with an occurence
print("")
print("%s said the word %s..." % (artist, keyword))

for song, lyrics in all_songs.iteritems():
    count = re.sub("[^\w]", " ",  lyrics).split().count(keyword.lower())
    if (count != 0):
        print("%d time%s in the song %s!" % (count, "" if (count == 1) else "s", song))
