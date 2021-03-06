import eyed3
import os


# In the case of my Windows at least the change for some reason it's not visible if you check it in the properties' window
# but, using a program like foobar2000, if you make a little change to all the songs (like changing the one property, e.g. the album name)
# it will appear on the properties' window).

print("\nThis program allows you to set the title of a song using its filename.")
print("If the name is in the form: 'myAlbum - myTitle.mp3'.")
print("You can introduce the 'myAlbum - ' part and the format ('.mp3') to change the title to 'myTitle'.\n\n")
print("This program will loop through all the files from the current directory. Make sure there aren't files you don't want to manipulate.\n\n")

strHeader = input("Introduce the header of the file: ")
strMp3    = input("Introduce the format of the file: ")

def get_directory():
    return os.path.dirname(os.path.realpath(__file__))


files = [f for f in os.listdir(get_directory()) if f.endswith(strMp3)]

for f in files:
    audiofile = eyed3.load(f)

    songTitle = f[len(strHeader):][:-len(strMp3)]
    
    audiofile.tag.title = songTitle
    audiofile.tag.save()

print()
