import csv
import plotly.express as pe

with open("Final.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        row.append(row)

headers = row[0]
star_data_rows = row[1: ]

temp = list(star_data_rows)
