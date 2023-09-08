from youtubesearchpython import VideosSearch
import pprint

# importing packages
from pytube import YouTube
import os

def download(name, path):
    videosSearch = VideosSearch(name, limit = 1)

    result = videosSearch.result()
    #pprint.pprint(result['result'][0]['link'])
    url = result['result'][0]['link']

    try:
        os.remove(path + '\\' + 'file.mp3')
    except:
        print('nofile')

    yt = YouTube(str(url))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
     

    destination = str(path)
    
    # download the file
    out_file = video.download(output_path=destination)
  
    print(out_file)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = path + '\\' + 'file.mp3'
    os.rename(out_file, new_file)
  
    # result of success
    #return(yt.title + " has been successfully downloaded.")
    return out_file

#download('help, beatles', 'C:\\Bedrock')

# if __name__ == '__main__':
#     download('take on me', 'C:\\musicdl\\music')