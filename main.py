import os
import vlc
import re

work_dir = os.getcwd()

# Set folders
fOut = "exported_genres"
if not os.path.exists(fOut):
    os.makedirs(fOut)

f1 = "Modern music"
f2 = "Old music"
f3 = "Nostalgic"

fQ = "Electronic"
fW = "Rock"
fE = "Folk"

# Make folders, if they don't exist yet
if not os.path.exists(fOut+"/"+f1):
    os.makedirs(fOut+"/"+f1)
if not os.path.exists(fOut+"/"+f2):
    os.makedirs(fOut+"/"+f2)
if not os.path.exists(fOut+"/"+f3):
    os.makedirs(fOut+"/"+f3)

if not os.path.exists(fOut+"/"+f1+"/"+fQ):
    os.makedirs(fOut+"/"+f1+"/"+fQ)
if not os.path.exists(fOut+"/"+f1+"/"+fW):
    os.makedirs(fOut+"/"+f1+"/"+fW)
if not os.path.exists(fOut+"/"+f1+"/"+fE):
    os.makedirs(fOut+"/"+f1+"/"+fE)

if not os.path.exists(fOut+"/"+f2+"/"+fQ):
    os.makedirs(fOut+"/"+f2+"/"+fQ)
if not os.path.exists(fOut+"/"+f2+"/"+fW):
    os.makedirs(fOut+"/"+f2+"/"+fW)
if not os.path.exists(fOut+"/"+f2+"/"+fE):
    os.makedirs(fOut+"/"+f2+"/"+fE)

if not os.path.exists(fOut+"/"+f3+"/"+fQ):
    os.makedirs(fOut+"/"+f3+"/"+fQ)
if not os.path.exists(fOut+"/"+f3+"/"+fW):
    os.makedirs(fOut+"/"+f3+"/"+fW)
if not os.path.exists(fOut+"/"+f3+"/"+fE):
    os.makedirs(fOut+"/"+f3+"/"+fE)


# Print a guide of use
print("""
            Enter:
            1 for {f1}                      Q for {fQ} 
            2 for {f2}          +           W for {fW} 
            3 for {f3}                      E for {fE}
            Enter nothing to do nothing and skip to the next song.
            
            Example:
            1E = '{f1}' into '{fE}'
            3Q = '{f3}' into '{fQ}' 
            
            """.format(f1=f1, f2=f2, f3=f3, fQ=fQ, fE=fE, fW=fW))

for directory, subdirectories, files in os.walk(work_dir):
    for file in files:
        file_path = str(os.path.join(directory,file))
        # Filter only .mp3 files
        if "mp3".lower() in file_path.lower(): 
            # "Tell the user what are we doing!"
            print(os.path.join(directory,file))
            print("Playing file")
            # Initialize VLC and load file
            p = vlc.MediaPlayer("file://{0}".format(file_path))
            # Play file and skip to 30% - if song is 5:00, it will skip to 1:30
            p.play()
            p.set_position(0.3)

            # Request keyboard input for genre filter
            genre_in = input("Input? ")



            if "1" in genre_in.lower():
                if not os.path.exists(fOut+"/"+f1):
                    os.makedirs(fOut+"/"+f1)


                elif "q" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f1+"/"+fQ):
                        os.makedirs(fOut+"/"+f1+"/"+fQ)
                    os.rename(file_path, directory+"/"+fOut+"/"+f1+"/"+fQ+"/"+file)

                elif "w" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f1+"/"+fW):
                        os.makedirs(fOut+"/"+f1+"/"+fW)
                    os.rename(file_path, directory+"/"+fOut+"/"+f1+"/"+fW+"/"+file)

                elif "e" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f1+"/"+fE):
                        os.makedirs(fOut+"/"+f1+"/"+fE)
                    os.rename(file_path, directory+"/"+fOut+"/"+f1+"/"+fE+"/"+file)

                else:
                    os.rename(file_path, directory+"/"+fOut+"/"+f1+"/"+file)


            if "2" in genre_in.lower():
                if not os.path.exists(fOut+"/"+f2):
                    os.makedirs(fOut+"/"+f2)


                elif "q" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f2+"/"+fQ):
                        os.makedirs(fOut+"/"+f2+"/"+fQ)
                    os.rename(file_path, directory+"/"+fOut+"/"+f2+"/"+fQ+"/"+file)

                elif "w" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f2+"/"+fW):
                        os.makedirs(fOut+"/"+f2+"/"+fW)
                    os.rename(file_path, directory+"/"+fOut+"/"+f2+"/"+fW+"/"+file)

                elif "e" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f2+"/"+fE):
                        os.makedirs(fOut+"/"+f2+"/"+fE)
                    os.rename(file_path, directory+"/"+fOut+"/"+f2+"/"+fE+"/"+file)

                else:
                    os.rename(file_path, directory+"/"+fOut+"/"+f2+"/"+file)


            if "3" in genre_in.lower():
                if not os.path.exists(fOut+"/"+f3):
                    os.makedirs(fOut+"/"+f3)


                elif "q" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f3+"/"+fQ):
                        os.makedirs(fOut+"/"+f3+"/"+fQ)
                    os.rename(file_path, directory+"/"+fOut+"/"+f3+"/"+fQ+"/"+file)

                elif "w" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f3+"/"+fW):
                        os.makedirs(fOut+"/"+f3+"/"+fW)
                    os.rename(file_path, directory+"/"+fOut+"/"+f3+"/"+fW+"/"+file)

                elif "e" in genre_in.lower():
                    if not os.path.exists(fOut+"/"+f3+"/"+fE):
                        os.makedirs(fOut+"/"+f3+"/"+fE)
                    os.rename(file_path, directory+"/"+fOut+"/"+f3+"/"+fE+"/"+file)

                else:
                    os.rename(file_path, directory+"/"+fOut+"/"+f3+"/"+file)

            p.stop()

