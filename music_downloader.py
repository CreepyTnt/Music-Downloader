import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_download as ytdl
from mutagen.easyid3 import EasyID3
import pprint
import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK
import auth
#import pprint


#Authentication - without user

if auth.use_spotify:
    client_credentials_manager = SpotifyClientCredentials(client_id=auth.client_id, client_secret=auth.client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def download(query, location = r'C:\gabbtools\songs'):
    try:
        if auth.use_spotify:
            results = sp.search(query, limit=1, offset=0, type='track', market='us')
        else:
            results = 'none'
        path = location


        ytdl.download(query, path)

        if auth.use_spotify:
            filename = results['tracks']['items'][0]['name'] + ' -- ' + results['tracks']['items'][0]['artists'][0]['name'] + '.mp3'
        else:
            filename = 'file.mp3'
        
            
        try:
            if not os.path.exists(f'{path}\\{filename}'):
                os.rename(f'{path}\\file.mp3', f'{path}\\{filename}')
            else:
                return('file already exists')
        except:
            if not os.path.exists(f'{path}\\{filename}'):
                os.rename(f'{path}\\file.mp3', f'{path}\\{query}')
            else:
                return('file already exists, try setting up spotify')
            
            
        return(f'Downloaded song: {filename}')
    except: 
        return(f'failed to download song: {query}')

