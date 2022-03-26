import os, json, csv
from tqdm import tqdm

# Constants
PLAYLIST_COUNT = 1000000
MPD_FILE_COUNT = 1000 # number of files inside mpd data
MPD_FILE_DATA_COUNT = int(PLAYLIST_COUNT/MPD_FILE_COUNT) # count of data inside each file
MAX_TRACK_COUNT = 250

# Getting path
current_path = os.getcwd()
data_path = current_path + "/1-data/mpd/spotify_million_playlist_dataset/data/"

# Getting file names
data_file_names = []
for i in range(MPD_FILE_COUNT):
    start = i*MPD_FILE_DATA_COUNT
    end = start+(MPD_FILE_DATA_COUNT-1)
    data_file_names.append("mpd.slice." + str(start) + "-" + str(end) + ".json")

# Getting data and extract CSV
header = ["id","title","tracks"]
extract_path_name = current_path + "/1-data/dataset/playlists.csv"
with open(extract_path_name, 'w', encoding='UTF8', newline='') as f:
    print("Creating", extract_path_name)
    writer = csv.writer(f)
    writer.writerow(header)
    # Open each file
    for i in tqdm(range(MPD_FILE_COUNT)):
    # for i in range(MPD_FILE_COUNT):
        # print("opening data",data_path+data_file_names[i])
        opened_file = open(data_path+data_file_names[i])
        loaded_json = json.load(opened_file)
        # Get each playlist data in file
        for j in range(MPD_FILE_DATA_COUNT): 
            # Get data for each playlist
            playlist = loaded_json["playlists"][j]
            # Extracting relevant data
            playlist_id = playlist["pid"]
            playlist_title = playlist["name"].replace(","," ")
            playlist_tracks = []
            for track in playlist["tracks"]:
                track_id = track["track_uri"].replace("spotify:track:","")
                playlist_tracks.append(track_id)
            # Writiting to csv for each playlist
            writer.writerow([playlist_id, playlist_title, *playlist_tracks])