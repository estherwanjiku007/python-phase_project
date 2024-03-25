from artist import Artist
from song import Song

def new_data():
  # Song.delete_table()
  # Artist.delete_table()
  # Song.create_table()
  # Artist.create_table()

  song1=Song.create("Shusha_Nyavu","2020")  
  Artist.create("Chrirstina Shusho","Christina_Shusho@gmail.com",song1.id)
  song2=Song.create("Vimbada","2018")  
  song3=Song.create("Ngori","2016")  
  Artist("Moji Shotbaba","Shotbaba@gmail.com",song2.id)
  Artist("Jabidii","Jabidii@gmail.com",song3.id)

 

 




# try: 
#     my_genre=Genre.all
#     print(my_genre)
# except:raise ValueError("My_genre has no genre")
