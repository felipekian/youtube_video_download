from pytube import YouTube
from pytube import Playlist

url = input('Insera a url da playlist: \n>>> ')
path_save = input('\n\nInforme o caminho para salvar os videos: \n>>> ')


#link of the video to be downloaded
links = url
# SAVE_PATH = "C:\\Users\\Felipe\\Desktop\\Musicas_yt"
SAVE_PATH = path_save

playlist = Playlist(links)

PlayListLinks = playlist.video_urls
N = len(PlayListLinks)
#print('Number of videos in playlist: %s' % len(PlayListLinks))

print(f"This link found to be a Playlist Link with number of videos equal to {N} ")
print(f"\n Lets Download all {N} videos")

for i,link in enumerate(PlayListLinks):
    yt = YouTube(link)
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    d_video.download(SAVE_PATH)
    print(i+1, ' Video is Downloaded.')