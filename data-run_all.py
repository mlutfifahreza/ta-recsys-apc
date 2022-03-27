import os, time

file_names = [
    "data-generate_playlists_csv.py",
    "data-generate_artists_csv.py",
    "data-generate_tracks_csv.py",
    "data-generate_tracks_popular_csv.py"
]

for name in file_names:
    command = "python3 ./" + name
    print("Running:",command)
    start = time.time()
    os.system(command)
    end = time.time()
    print("Start\t:", time.asctime( time.localtime(start)))
    print("End\t:", time.asctime( time.localtime(end)))
    print("Total\t:", round(end-start), "ms")
    print()