import spotipy
import json


if __name__ == '__main__':    
    with open('data/keys.json', 'r') as infile:
        keys = json.load(infile)
    
    sp = spotipy.Spotify()
    plistId = '68chiQq5L7XnyCI2UaqVq7'
    # get the playlist first
    playlist = sp.playlist(plistId)
    print(playlist)
