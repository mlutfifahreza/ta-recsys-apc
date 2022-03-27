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

# Getting data
artists = {}
# Open each file
print("Reading mpd files")
for i in tqdm(range(MPD_FILE_COUNT)):
    opened_file = open(data_path+data_file_names[i])
    loaded_json = json.load(opened_file)
    # Get each playlist data in file
    for j in range(MPD_FILE_DATA_COUNT): 
        playlist = loaded_json["playlists"][j]
        # Extracting relevant data
        for track in playlist["tracks"]:
            artist_id = track["artist_uri"].replace("spotify:artist:","")
            artist_name = track["artist_name"]
            artists[artist_id] = artist_name

# Extract to CSV
header = ["id","name"]
extract_path_name = current_path + "/1-data/dataset/artists.csv"
with open(extract_path_name, 'w', encoding='UTF8', newline='') as f:
    print("Export : creating", extract_path_name)
    writer = csv.writer(f)
    writer.writerow(header)
    for id, name in tqdm(artists.items()):
        writer.writerow([id,name])