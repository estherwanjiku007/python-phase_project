from artist import Artist
from song import Song

def exit_programme():
    print("Goodbye")
    exit(0)

def list_arttists():
    artists=Artist.get_all()   
    for artist in artists:
         # print(type(artist))
          print(artist)
    # else:print("Sorry,no artist found")

def find_artist_by_name():
    name=input("Enter the artist's name:\n> ")
    artists=Artist.find_by_name(name)
    print(artists) if artists else print(f"Sorry, Artist {name} not found")

def find_artist_by_id():
    id_=input("Enter an artist's id:\n> ")
    artists=Artist.find_by_id(id_)
    print(artists) if artists else print(f"Sorry, Artist_id {id_} not found")

def find_artist_by_email():
    email=input("Enter the artist's email:\n> ")
    artists=Artist.find_by_email(email)
    print(artists) if artists else print(f"Sorry, Artist {email} not found")
        
def create_artist():
    artist=input("Enter the artist's name:\n> ")
    email=input("Enter the artist's email:\n> ")
    song_id=input("Enter the artist's song_id:\n> ")
    #genre=input("Enter the artist's genre")
    artists=Artist.create(artist,email,song_id)
   
    try:
        print(f"Artist {artists} successfully created ")
    except Exception as exc:
            print("Sorry,you were unable to create an artist",exc)
    #else:print("Sorry,you were unable to create an artist")

def update_artist():
    id_=input("Enter the artist's id:\n> ")
    if artist:=Artist.find_by_id(id_):
        try:
            artist_name=input("Enter the artist's new name:\n> ")
            artist_email=input("Enter the artist's new email:\n> ")
            artist._name=artist_name
            artist._email=artist_email
            artist.update()
            print(f"Your new arist's name is {artist.name} and email is{artist.email}")
        except Exception as error:("Error while upating artist",error)
    else:print(f"Sorry,Artistid {id_} not found")

def delete_artist():
    id_=input("Enter the artist's id:\n> ")
    artist=Artist.find_by_id(id_)
    if artist:
        artist.delete()
        print(f"artist {artist} deleted successfully")
    else:print(f"Artist_id {id_} not found")

def list_songs():
    songs=Song.get_all()
    for song in songs:
        print(song)

def find_song_by_name():
    song_name=input("Enter the song name:\n> ")
    songs=Song.find_by_name(song_name)
    if songs:
        print(songs)
    else:print(f"{song_name} not found")

def find_song_by_id():
    id_=input("Enter the artist song's id:\n> ")
    song=Song.find_by_id(id_)
    if song:
        print(song)
    else:print(f"Song id{id_} not found")

def find_song_by_release_yr():
    release_yr=input("Enter the song's release year:\n> ")
    if song:=Song.find_by_release_year(release_yr):
        print(song)
    else:print(f" sorry,Release year {release_yr} not found ")

def create_song():    
        song=input("Enter the song's name:\n> ")
        release_yr=input("Enter the song's release year:\n> ")
        try:
           song=Song.create(song,release_yr)
           print(f"{song} created successfully")
        except Exception as error:
            print(f"Error creating a song {error}")
        
def update_song():
    id_=input("Enter the song's id:\n> ")
    if song:=Song.find_by_id(id_):
        try:
            song_name=input("Enter new song name:\n> ")
            song.name=song_name
            song_releaseyr=input("Enter new song releaseyear:\n> ")
            song.release_yr=song_releaseyr
            song.update()
        except Exception as error:
            print("Error updating song",error)
    else:print(f"Song id {id_} not found")

def delete_song():
    id_=input("Enter the song_id:\n> ")
    if song:=Song.find_by_id(id_):
        song.delete()
        print(f"song {song} deleted successfully")
    else:print("Error deleting song")
        

            

      
    



    

    
    