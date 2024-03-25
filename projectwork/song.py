#from database import CONN,CURSOR
import sqlite3
CONN=sqlite3.connect("mymusic.db")
CURSOR=CONN.cursor()
class Song: 
    all={}   #Dictionary to keep track of the songs
    def __init__(self,song,release_yr,id=None):
        self.id=id
        self.name=song
        self.release_yr=release_yr        
    
    def __repr__(self):
       return f"Song {self.id} {self.name} {self.release_yr}"
    
    @property
    def name(self):
        return self._name
    #Checking if the name is a non_empty string 
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value)>0:
            self._name=value
        else:raise ValueError("Song_Name must be a string of length greater than zero")
 
    @property
    def release_yr(self):
        return self._release_yr
    #Check if the release year is a non_empty string
    @release_yr.setter
    def release_yr(self,value):
        if isinstance(value,str) and len(value)>0:
            self._release_yr=value
        else:raise ValueError("Name must be a string of length greater than zero")

#     @classmethod
#     def create_table(cls):
#         CURSOR.execute('''CREATE TABLE IF NOT EXISTS songs(
#                        id INTEGER PRIMARY KEY,
#                        song TEXT NOT NULL,
#                        release_yr TEXT NOT NULL,
# );''')
#         print("Table created successfully")
#         CONN.commit()    
    
#     @classmethod
#     def delete_table(cls):
#         CURSOR.execute("DROP TABLE IF EXISTS songs")

    
    def save(self):
        #Method to insert into the table        
        CURSOR.execute("INSERT INTO songs(name,release_yr) VALUES(?,?)",(self.name,self.release_yr))
        self.id=CURSOR.lastrowid #Setting the id to the lastrowid
        type(self).all[self.id]=self#Giving the dictionary a value
        CONN.commit()
        # self.id=CURSOR.lastrowid 
        # type(self).all[self.id]=self
   

    @classmethod
    def create(cls,song,release_yr):
       # id_=CURSOR.lastrowid
        new_song=cls(song,release_yr)#Create an instance of the class
        new_song.save()#Calling the save method

    def update(self):
        #Method to change the value of a current song to a a new song
        CURSOR.execute("UPDATE songs SET name=?,release_yr=? WHERE id=?",(self.name,self.release_yr,self.id))
        CONN.commit()

    def delete(self):
        #Deleting the current value in the database
        CURSOR.execute("DELETE FROM songs WHERE id=?",(self.id,))
        del type(self).all[self.id]#Deleting the value from the dictionary
        CONN.commit()

        
        print("song deleted successfully")

    @classmethod
    def instance_from_db(cls,row):
        song=cls.all.get(row[0])#Retreiving the id of the current instance
        if song:#Ensuring that the instance are of the correct values incase of change and the id is not an empty string
            song.name=row[1]
            song.release_yr=row[2]
        else:#If it is not in the dictionary,create one
            song=cls(row[1],row[2])#Calling the class and giving it values
            song.id=row[0]#Set the id to the value of the first column
            cls.all[song.id]=song#Give the dictionary the current value
        return song
    
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM songs"
        rows=CURSOR.execute(sql).fetchall()#Select all the data
        return [cls.instance_from_db(row) for row in rows]#Return all the data from the database in form of an array
    
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM songs WHERE id=?"
        row=CURSOR.execute(sql,(id,)).fetchone()#Select data where the id is same as the given id
        return cls.instance_from_db(row) if row else print(f"Song_id {id} not found")
    
    @classmethod
    def find_by_name(cls,name):
        sql="SELECT * FROM songs WHERE name=?"
        rows=CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(rows)if rows else print(f"Song_name {name} not found") 
    
    @classmethod
    def find_by_release_year(cls,release_yr):
        sql="SELECT * FROM songs WHERE release_yr=?"
        rows=CURSOR.execute(sql,(release_yr,)).fetchone()
        return cls.instance_from_db(rows) if rows else print(f"Release_yr for this song was not found")

#CONN.close()




    


        
