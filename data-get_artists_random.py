import os, csv
import numpy as np
from tqdm import tqdm

# Constants
ARTISTS_COUNT = 295860 # number of unique artists 295860
GET_COUNT = 100 # number of unique artists to display

# Getting path
current_path = os.getcwd()
read_path_name = current_path + "/1-data/dataset/artists.csv"

# Read from CSV
row_number_to_get = np.random.randint(1, ARTISTS_COUNT, GET_COUNT)
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