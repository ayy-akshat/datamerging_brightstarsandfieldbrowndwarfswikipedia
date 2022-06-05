import csv
import pandas as pd

fbd_df = pd.read_csv("field_brown_dwarfs.csv")
star_df = pd.read_csv("stars.csv")

fbd_df = fbd_df[fbd_df['distance'].notna()]
fbd_df = fbd_df[fbd_df['mass'].notna()]
fbd_df = fbd_df[fbd_df['radius'].notna()]

star_df = star_df[star_df['distance'].notna()]
star_df = star_df[star_df['mass'].notna()]
star_df = star_df[star_df['radius'].notna()]

fbd = fbd_df.to_numpy()
star = star_df.to_numpy()

for i in range(1, len(fbd)):
    fbd[i][2] = fbd[i][2] * 0.000954588
    fbd[i][3] = fbd[i][3] * 0.102763


final = [
    ['name', 'distance', 'mass', 'radius']
]
for i in fbd:
    final.append(i)

for index, i in enumerate(star):
    if index != 0: final.append(i)

with open("final.csv", "w") as final_csv:
    writer = csv.writer(final_csv)
    writer.writerows(final)
    