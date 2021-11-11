from __future__ import unicode_literals
import youtube_dl, os, time

def download():
    link = input("Youtube link: ")
    ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        result = ydl.extract_info("{}".format(link))
        filename = str(ydl.prepare_filename(result)).replace(".mp4", ".mp3").replace(".webm", ".mp3")
        os.utime("%s/%s"%(os.path.dirname(os.path.abspath(__file__)), filename), (time.time(), time.time()))
    
    download()

print("Youtube Downloader by Raddis.")
download()