
from helpers import( 
   exit_programme,
   list_arttists,
   find_artist_by_name,
   find_artist_by_id,
   find_artist_by_email,
   create_artist,
   update_artist,
   delete_artist,
   list_songs,
   find_song_by_id,
   find_song_by_name,
   find_song_by_release_yr,
   create_song,
   update_song,
   delete_song
   )

                 

def app():
      while True:
            menu()
            the_choice=input(">")
            if the_choice=="1":
                exit_programme()
            elif the_choice=="2":
                list_arttists()
            elif the_choice=="3": 
                 find_artist_by_name()
            elif the_choice=="4": 
                 find_artist_by_id()  
            elif the_choice=="5":
                 find_artist_by_email()            
            elif the_choice=="6":
                 create_artist()
            elif the_choice=="7":
                 update_artist()
            elif the_choice=="8":
                 delete_artist() 
            elif the_choice=="9":
                 list_songs()  
            elif the_choice=="10":
                 find_song_by_id()
            elif the_choice=="11":
                 find_song_by_name()
            elif the_choice=="12":
                 find_song_by_release_yr()
            elif the_choice=="13":
                 create_song()
            elif the_choice=="14":
                 update_song()
            elif the_choice=="15":
                 delete_song()
                
def menu():
    print("Please select an option:")
    print("1. Exit the program")
    print("2. List_artists")
    print("3. Find artist by name")
    print("4. Find artist by id")
    print("5: Find artist by email")
    print("6: Create artist")
    print("7: update artist")
    print("8. delete artist")
    print("9. list songs")
    print("10. Find song by id")   
    print("11: find song by name")
    print("12: find song by release_yr")
    print("13: create song")
    print("14: update song")
    print("15: delete song")


            
if __name__=="__main__":
     app()
