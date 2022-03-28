import os, csv
from tqdm import tqdm

# Constants
PLAYLIST_COUNT = 1000000 # number of playlists 1000000

# Getting path
read_file_path = os.getcwd() + "/1-data/dataset/playlists.csv"

# Reading playlists.csv dataset
titles = {}
with open(read_file_path) as csv_file:
    print("Reading :",read_file_path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_at_header = True
    col_title_index = 1
    for row in tqdm(csv_reader):
        if is_at_header:
            is_at_header = False
        else:
            titles[row[col_title_index]] = None

# Writing to titles.csv
write_file_path = os.getcwd() + "/1-data/dataset/titles.csv"
header = ["title"]
with open(write_file_path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    sorted_titles = sorted(titles.keys())
    count = 0
    for title in tqdm(sorted_titles):
        writer.writerow([title])