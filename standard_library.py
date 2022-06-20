# Work with files and directories

from pathlib import Path

# r before strings creates a raw string
Path(r"c:\Program Files (x86)\MySQL")
Path.home() # returns the home directory of the current user
path = Path(r"C:\Users\baezl\PycharmProjects\Python_Training_2022")
path.is_file() # checks if the path is to a file
path.is_dir() # checks if the path leads to a dir
print(path.name) # returns the files.dir/s name in the path
print(path.stem) # returns the files.dir/s name in the path w/o extention
print(path.suffix) # returns the files.dir/s extention in the path
print(path.parent) # returns the files.dir/s name ofthe parent folder
# Remenber that these path methods represent data but dont change any of the files being viewed

# To get a list of paths and or directories
for p in path.iterdir(): # return an iterator object that can be looped to view all the files and directories.
    print(p)
# can turn into a list as well like this.
paths = [p for p in path.iterdir() if p.is_dir()]  # retunts all the directories only
print(paths)
files = [f for f in path.rglob("*.py")]
print(files)

# Methods to work with files
#path.exists() # Checks if the directory exists
#path.rename() # rename the file
#path.unlink() # deletes a file
#path.stats() # Checks metadata of the file

# ############################ #
# #### Work with Zip files ### #
# ############################ #
from zipfile import ZipFile

#zipFile = ZipFile("file.zip", "w")# Creates a zipfile and readies it to be writen to
#for path in Path(r"C:\Users\baezl\PycharmProjects\Python_Training_2022").rglob("*.*"):
#    zipFile.write(path)

# ############################ #
# #### Work with csv files ### #
# ############################ #
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Store", "Product",])
    writer.writerow(["Naoyuki", "Fukushima", "Volunteers"])
    writer.writerow(["Chiemi", "Fukushima", "Food"])
    writer.writerow(["Miyuki", "Gifu", "Love"])

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ############################ #
# ### Work with Json files ### #
# ############################ #
# Json means JavaScript Object Notation

import json

movies = [{"id": 1, "title": "Terminator", "year": 1989},
          {"id": 2, "title": "Judge Dredd", "year": 1989},
          {"id": 3, "title": "Predator", "year": 1989}]

data = json.dumps(movies)
Path("movies.json").write_text(data)

# ############################ #
# ## Work with sqlite files ## #
# ############################ #

import sqlite3

movies_db = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:

    command = "INSERT INTO Movies Values(?, ?, ?)"
    for movie in movies_db:
        conn.execute(command, tuple(movie.values()))
    conn.commit()