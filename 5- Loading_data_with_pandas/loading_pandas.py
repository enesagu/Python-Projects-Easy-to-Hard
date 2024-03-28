import pandas as pd

# Read the CSV file
csv_path = 'basic.csv'
df = pd.read_csv(csv_path)

# Display the first few rows of the DataFrame
print(df.head())

# Creating a new DataFrame
songs = {"Album": ["Ligts Out", "Kazıdık Tırnaklarla", "Ahde vefa", "kan"],
         "Released": [2019, 2017, 2018, 2020],
         "Length": ["00:42:19", "00:42:11", "00:57:44", "00:46:21"]}
songs_frame = pd.DataFrame(songs)

# Filtering rows where the "Released" column has a value greater than or equal to 2018
df1 = df[df["YEAR"] >= 2020]

# Display the filtered DataFrame
print(df1)

# Save the filtered DataFrame to a new CSV file
df1.to_csv("new_songs.csv", index=False)
