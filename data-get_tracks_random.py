import os, csv
import numpy as np
from tqdm import tqdm

# Constants
TRACKS_COUNT = 2262292
GET_COUNT = 10

# Getting path
current_path = os.getcwd()
read_path_name = current_path + "/1-data/dataset/tracks.csv"

# Read from CSV
row_number_to_get = np.random.randint(1, TRACKS_COUNT, GET_COUNT)
random_data_result = []

row_number = 0
with open(read_path_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in tqdm(csv_reader):
        row_number += 1
        if row_number in row_number_to_get:
            random_data_result.append([row_number, *row])
for data in random_data_result:
    print(data)