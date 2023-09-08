import os
import urllib.request
import time

print ('TO CREATE A DESKTOP SHORTCUT, MAKE SURE TO RUN AS ADMINISTRSTOR. WINDOWS REQUIRES ADMIN TO CREATE SHORTCUTS. WITHOUT AADMINISTRATOR, EVERYTHING SHOULD STILL WORK AS NORMAL EXCEPT WITHOUT A DESKTOP SHORTCUT. YOU CAN CREATE A SHORTCUT TO "C:\\musicdl\\ui.pyw" MANUALLY IF YOU WANT.')
time.sleep(5)

#install dependencies
modules = [
    'os',
    'mutagen',
    'pytube',
    'spotipy',
    'youtube-search-python',
    'tkinter'
]

for i in modules:
    os.system(f'pip install {i}')


import getpass

# usrnm = input(f'please enter your username. It was auto-detected as "{getpass.getuser()}">>')
# if usrnm.lower == '':
#     usrnm = getpass.getuser()


#download files

if os.path.exists('C:\\musicdl'):
    print('Installation already exists. Installing latest version')
    os.remove('C:\\musicdl\\ui.pyw')
    os.remove('C:\\musicdl\\music_downloader.py')
    os.remove('C:\\musicdl\\youtube_download.py')
    update = True
else:
    os.mkdir('C:\\musicdl')
    update = False


# Define the URL and file path
url = 'https://raw.githubusercontent.com/CreepyTnt/Music-Downloader/main/ui.pyw'
file_path = 'C:\\musicdl\\ui.pyw'
# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)

# Define the URL and file path
url = 'https://raw.githubusercontent.com/CreepyTnt/Music-Downloader/main/music_downloader.py'
file_path = 'C:\\musicdl\\music_downloader.py'
# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)

# Define the URL and file path
url = 'https://raw.githubusercontent.com/CreepyTnt/Music-Downloader/main/youtube_download.py'
file_path = 'C:\\musicdl\\youtube_download.py'
# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)


#create config.py file
if os.path.exists('C:\\musicdl\\config.py'):
    print('already installed')

else:

    does_have_spotify = input('Do you have a spotify developer account, client id, and secret token for music metadata? (y/n)')

    if does_have_spotify.lower() == 'y':
        client_id = input('enter your client_id')
        secret = input('please enter your secret token')
        with open('C:\\musicdl\\config.py', 'w') as f:
            f.write(f"use_spotify = True; client_id={client_id}; client_secret={secret}")

    else:

        with open('C:\\musicdl\\config.py', 'w') as f:
            f.write(f"use_spotify = False; client_id=''; client_secret=''")


os.system(r'mklink %userprofile%\Desktop\MusicDL.ink "C:\musicdl\ui.pyw"')
print('\ncompleted. If there is no desktop icon, re-run as administrator')
time.sleep(10)
