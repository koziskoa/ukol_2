import csv
from os import read
with open("priklad_vstupu.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    
    for row in reader:  # vytiskne soubor .csv
        print(row[:])
    