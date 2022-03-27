import os, csv

# Constants
ARTISTS_COUNT = 295860 # number of unique artists 295860

# Getting path
current_path = os.getcwd()
read_path_name = current_path + "/1-data/dataset/artists.csv"

# Read from CSV
print("Reading file", read_path_name)
count = 0
is_with_header = True
with open(read_path_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = -1 if is_with_header is True else 0 
    for row in csv_reader:
        count += 1

if (count == ARTISTS_COUNT):
    print("Count is validated, count =",count)
else:
    print("Count is wrong!")