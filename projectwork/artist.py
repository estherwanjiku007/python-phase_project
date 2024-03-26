#from database import CONN,CURSOR

import sqlite3
CONN=sqlite3.connect("mymusic.db")
CURSOR=CONN.cursor()
class Artist:
    all={}#Dictionary to keep track of all the artists 
    
    def __init__(self,artist,email,song_id,id=None):
        self.id=id
        self._name=artist 
        self._email=email       
        self._song_id=song_id       
    
    def __repr__(self):
        return f"<Artist {self.id}:{self.name}, {self.email}, {self.song_id}\n"
    
    @property
    def name(self):
        return self._name
    
    #Check if the artist name is a string greater than zero
    @name.setter
    def name(self,value):
        if isinstance(value,str) and Song.find_by_id(value):
            self._name=value
        else:raise ValueError("Artist name must be a string  that has a length greater than zero")
    
    @property
    def song_id(self):
        return self._song_id
    
    #Check if the song_id is an insance of the id in songs table 
    @song_id.setter
    def song_id(self,value):
        if isinstance(value,int) and len(value)>0 :
            self._song_id=value
        else:raise ValueError("Song_id must be an integer  that must be an instance of a song")

    #Check if the email is a string of length greater than zero
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        if isinstance(value,str) and len(value)>0:
            self._email=value
        else:raise ValueError("Email name must be a string  that has a length greater than zero")
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS artists(
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       song_id INTEGER,
                       FOREIGN KEY (song_id) REFERENCES songs(id)
                        )""")
        CONN.commit()
        print("Artist table created successfully")
        
    @classmethod
    def delete_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS artists;")
        CONN.commit() # saves changes made to the db

    # Method to add the new artist to the database
    def save(self):
        sql="""
        INSERT INTO artists(name,email,song_id) VALUES(?,?,?)
        """
        CURSOR.execute(sql,(self._name,self._email,self._song_id))
        self.id=CURSOR.lastrowid#Make the id of the new artist to be equal to a new key
        type(self).all[self.id]=self#Add the artist to the dictionary
        CONN.commit()

        # self._id=CURSOR.lastrowid#Make the id of the new artist to be equal to a new key
        # type(self).all[self._id]=self#Add the artist to the dictionary
       
    #Method to create a new artist
    @classmethod
    def create(cls,artist,email,song_id):        
        new_artist=cls(artist,email,song_id)#Create a new instance of the artist
        new_artist.save()       
        return new_artist
    
    def update(self):
        sql="UPDATE artists SET name=? email=? song_id=? WHERE id =?"
        CURSOR.execute(sql,(self._name,self._email,self._song_id,self.id)) 
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM artists WHERE id=?",(self.id,))
        del type(self).all[self.id]#Delete the dictionary entry using the id as the key
        self.id=None #Set the id to none 
        CONN.commit()             
    
    @classmethod
    def instance_from_db(cls,row):
        artist=cls.all.get(row[0])#Check the dictionary for an existing instance using the row's primary key
        if artist:
           # ensure attributes match row values in case local instance was modified
           artist._name=row[1]
           artist._email=row[2]
           artist._song_id=row[3]
           
        else:
            # not in dictionary, create new instance and add to dictionary
            artist=cls(row[1],row[2],row[3])
            artist.id=row[0]
            cls.all[artist.id]=artist
        return artist
    
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM artists"
        rows=CURSOR.execute(sql).fetchall()#Return the data from the database        
        return [cls.instance_from_db(row) for row in rows]
        
    @classmethod
    def find_by_id(cls,id_):
        sql="SELECT * FROM artists WHERE id=?"
        row=CURSOR.execute(sql,(id_,)).fetchone()#Return data from the database
        
        return cls.instance_from_db(row) if row else print(f"Artist_id {id_} not found")
    
    @classmethod
    def find_by_name(cls,name):
        sql="SELECT * FROM artists WHERE name=?"
        row=CURSOR.execute(sql,(name,)).fetchone()#Return data from the database
        return cls.instance_from_db(row)if row else print(f"Artist {name} not found")
    
    @classmethod
    def find_by_email(cls,email):
        sql="SELECT * FROM artists WHERE email=?"
        rows=CURSOR.execute(sql,(email,)).fetchone()#Return data from the database
        return cls.instance_from_db(rows) if rows else print(f"Email {email} not found") 
        
#from genre import Genre
from song import Song