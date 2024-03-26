import sqlite3
CONN=sqlite3.connect("mymusic.db")#Create a database
CURSOR=CONN.cursor()#Create a cursor where we will run the commands
#Create the songs table
#CURSOR.execute("DROP TABLE IF EXISTS songs;")#Deleting the table
CURSOR.execute("""CREATE TABLE IF NOT EXISTS songs(
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       release_yr TEXT NOT NULL
);""")
#Create the artists table
#CURSOR.execute("DROP TABLE IF EXISTS artists;")
CURSOR.execute("""CREATE TABLE IF NOT EXISTS artists(
               id INTEGER PRMARY KEY,
               name TEXT NOT NULL,
               email TEXT NOY NULL,
               song_id INTEGER,
               FOREIGN KEY (song_id) REFERENCES songs(id)
);""")
CONN.commit()#Commit the changes
CONN.close()#close the database