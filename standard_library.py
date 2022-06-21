# Work with files and directories
import string
import subprocess
import sys
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
import random
import webbrowser
# email library
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from datetime import datetime, timedelta


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


#zipFile = ZipFile("file.zip", "w")# Creates a zipfile and readies it to be writen to
#for path in Path(r"C:\Users\baezl\PycharmProjects\Python_Training_2022").rglob("*.*"):
#    zipFile.write(path)

# ############################ #
# #### Work with csv files ### #
# ############################ #

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


movies = [{"id": 1, "title": "Terminator", "year": 1989},
          {"id": 2, "title": "Judge Dredd", "year": 1989},
          {"id": 3, "title": "Predator", "year": 1989}]

data = json.dumps(movies)
Path("movies.json").write_text(data)

# ############################ #
# ## Work with sqlite files ## #
# ############################ #

movies_db = json.loads(Path("movies.json").read_text())
# When working with files if you use the with statement
# Python will open use and then close files automatically

with sqlite3.connect("db.sqlite3") as conn:
    command0 = """CREATE TABLE Movies (
    ID int,
    Name varchar(255),
    Year int);"""
    command = "INSERT INTO Movies Values(?, ?, ?)"
#conn.execute(command0)
#for movie in movies_db:
#    conn.execute(command, tuple(movie.values()))\
# commits changes above to the DB
#conn.commit()

# ############################ #
# ###### Work with time ###### #
# ############################ #

# time
def send_emails():
    for i in range(100000):
        pass

# long way of calculating time of execution
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)

# Datetime
datetime(2018,11,1) # creating a datetime object
datetime.now() # returns current datetime
# string of a datetime object must specify in python, %ymd are directives for year, month, day etc
#datetime.strptime("2018/01/01", "%y/$m/%d")
dt = datetime.fromtimestamp(time.time()) # creates a current datetime object
print(f"{dt.year}/{dt.month}")

# Timedeltas give you duration or lenght of datetime objects
d1 = datetime(2010,1,1) + timedelta(days=1, seconds=3600)
d2 = datetime.now()
duration = d2 - d1
print(duration)
print("Days", duration.days)
print("Seconds", duration.seconds)

# ############################ #
# # Work with random numbers # #
# ############################ #
r = random.random() # returns a random value (floats usually)
random.randint(1,10) # returns a random integer from the parameters
#random.choice() # takes an array and randomly picks a random value in the array.
random.choices([1, 2, 3, 4], k=2) # return 2 values in the array
# creating a random password
# string method has ascii letters/digits to choose
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))

# ############################ #
# ##### Open web-browser ##### #
# ############################ #

# print("Deployment Test Completed. Automatic push will be implemented")
# webbrowser.open("https://www.xe.com/")

# ############################ #
# ##### email interaction #### #
# ############################ #

# to auto send emails you need one class to interact with mails and another one to
# connect to a smtp server to access the emails sending process

# message = MIMEMultipart()
# message["from"] = "Don Fidelo"
# message["to"] = "baezlopezfidel24@gmail.com"
# message["subject"] = "Testing"
# message.attach(MIMEText("Body"))
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo() # hello call to smtp server
#     smtp.starttls() #  tls is transport layer security
#     smtp.login("baezlopezfidel24@gmail.com", "z3r0xExE")
#     smtp.send_message(message)
#     print("Email Sent")

# ############################ #
# ####### Subprocesses  ###### #
# ############################ #

# run an external program
completed = subprocess.run(["python3", "main.py"], capture_output=True)
print(completed.args) #Array the includes the arguments inserted into the subprocess
print(completed.returncode) # return process code python
print(completed.stderr) # Errors in our program
print(completed.stdout) # Output in our program
