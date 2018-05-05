from pydub import AudioSegment
import glob
from console_progressbar import ProgressBar


temp1_song_list = glob.glob(
    '/home/atrumoram/Documents/PYTHON_PROJECTS/FLAC_TO_WMV/INPUT/*.flac')

song_list = []

name_band = input('Name of band: ')
name_album = input('Name of album: ')

for x in temp1_song_list:
    docastny_list = x.split("/")
    song_list.append(docastny_list[-1])

pb = ProgressBar(total=len(song_list),
                 prefix='Here',
                 suffix='Now',
                 length=50,
                 fill='X')

for x in range(len(song_list)):
    pb.print_progress_bar(x)
    song_name = song_list[x].replace('.flac', '')
    awesome = AudioSegment.from_file(f"INPUT/{song_list[x]}", "flac")
    awesome.export(f"OUTPUT/{song_name}",
                   format='mp3',
                   tags={'artist': name_band,
                         'album': name_album,
                         'title': song_name[5:]},
                   bitrate='320k')
