import tkinter as tk
from tkinter import font
import music_downloader as music
#import getpass
#import subprocess
import os

user_profile = os.environ['USERPROFILE']
# cmd = ['echo %userprofile%']
# result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True)
user_path = user_profile #result.stdout

music_path = os.path.join(user_path, 'Music\\Music Downloader')
print (music_path)


def download_song():
    song_query = song_query_entry.get()
    path = path_entry.get()
    output_text.delete("1.0", tk.END)  # Clear previous output
    if path == '':
        output_text.insert(tk.END, music.download(song_query, music_path))
    else:
        output_text.insert(tk.END, music.download(song_query, path))

window = tk.Tk()
window.title("Music Downloader")

default_font = font.Font(family="Arial", size=14)

song_query_label = tk.Label(window, text="Song Query:", font=default_font)
song_query_label.pack()
song_query_entry = tk.Entry(window, font=default_font)
song_query_entry.pack()

path_label = tk.Label(window, text="Path (optional):", font=default_font)
path_label.pack()
path_entry = tk.Entry(window, font=default_font)
path_entry.pack()

download_button = tk.Button(window, text="Download", font=default_font, command=download_song)
download_button.pack()

song_query_label = tk.Label(window, text="output", font=default_font)
song_query_label.pack()


output_text = tk.Text(window, font=default_font, height=5, width=40)
output_text.pack(pady=10)

disclaimer_label = tk.Label(window, text=(f"If no path is given, songs will be saved to '{music_path}'\n You can access this folder by clicking the Music tab in file explorer"), font=font.Font(family="Arial", size=8), justify="center")
disclaimer_label.pack(side="bottom", pady=10)

disclaimer_label = tk.Label(window, text=('If you have problems exporting, change all "\\" to "\\\\" or "/" \nIt is best to only download copyright-free music.\nWe do not endorse music piracy.'), font=font.Font(family="Arial", size=8), justify="center")
disclaimer_label.pack(side="bottom", pady=10)

window.mainloop()


