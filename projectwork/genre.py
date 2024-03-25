# from database import CURSOR,CONN
class Genre:
    all={}
    def __init__(self,name=None,id=None):
        self.name=name
        self.id=id
    #Validating that the  name must be a string of length greater than zero
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value)>0:
            self._name=value
        else:raise ValueError("Name must be a string of length greater than zero")
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE OF NOT EXISTS genres(
                       id  INTERGER PRIMARY KEY,
                       genre TEXT NOT NULL,
                       artist_id INTEGER,
                       FOREIGN KEY (artist_id) REFERENCES artists(id)
)""")

    def save(self,genre):
        self.name=genre
        CURSOR.execute("INSERT INTO genres(genre) VALUES(?)",(self.name))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    
    @classmethod
    def create(cls,a_genre):
        new_genre=cls(a_genre)
        new_genre.save(a_genre)
        return new_genre
    
    def update(self):
        CURSOR.execute("UPDATE genres SET name=? WHERE id=? ",(self.name,self.id)) 
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM genres WHERE id=?",(self.id,))
        del type(self).all[self.id]
        self.id=None
        CONN.commit()

    @classmethod
    def instance_from_db(cls,row):
        genre=row[1]
        if genre:
            genre.name=row[0]
        else:
            genre=cls(row[0])
            genre.id=row[1]
            cls.all[genre.id]=genre
        return genre
    
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM genres"
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
        
    
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM genres WHERE id=?"
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql="SELECT * FROM genres WHERE name=?"
        rows=CURSOR.execute(sql,(name,)).fetchone()
        return [cls.instance_from_db(row)for row in rows ]
from database import CURSOR,CONN 
CONN.close()


