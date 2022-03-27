import os,tqdm, csv

# Getting path
current_path = os.getcwd()
read_path_name = current_path + "/1-data/dataset/tracks.csv"

# Read from CSV
count = 0
is_with_header = True
with open(read_path_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = -1 if is_with_header is True else 0 
    for row in csv_reader:
        count += 1

print(count)