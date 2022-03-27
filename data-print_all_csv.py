import os, csv
import numpy as np

# Constants
PLAYLIST_COUNT = 1000000 # number of playlists 1000000
TRACKS_COUNT = 2262292 # number of unique tracks 2262292
ARTISTS_COUNT = 295860 # number of unique artists 295860
DISPLAY_COUNT = 5 # number of item to display
EMOJI_CHECK = "\U00002705" # emoji check mark button
EMOJI_CROSS = "\U0000274C" # emoji cross mark
IS_DISPLAY_RANDOM = False

file_names = [
    "artists.csv"
    "playlists.csv"
    "tracks.csv"
    "tracks_popular.csv"
]

files_detail = [
    { "name" : "artists.csv" , "count" : ARTISTS_COUNT},
    { "name" : "playlists.csv" , "count" : PLAYLIST_COUNT},
    { "name" : "tracks.csv" , "count" : TRACKS_COUNT},
    { "name" : "tracks_popular.csv" , "count" : TRACKS_COUNT}
]

base_path = os.getcwd() + "/1-data/dataset/"

for file in files_detail:
    full_path = base_path+file["name"]
    row_number_to_display = [0,1,2,3]
    if IS_DISPLAY_RANDOM : 
        row_number_to_display = np.random.randint(1, file["count"], DISPLAY_COUNT)
    print()
    print("Reading :", full_path)
    with open(full_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = -1
        for row in csv_reader:
            if count in row_number_to_display:
                print(row)
            count += 1
        print("Total count :", count)
        if file["count"] != None:
            if count == file["count"]:
                print(EMOJI_CHECK, "Good")
            else:
                print(EMOJI_CROSS, "Wrong!")
        else:
            print(EMOJI_CHECK, "Good")