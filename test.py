import vlc
import yt_dlp as youtube_dl
import sys

def get_best_stream(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'logger': MyLogger(),  # Enable logging
        'progress_hooks': [my_hook],  # Progress hook
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get('url')
        return video_url

class MyLogger(object):  # Logger class
    def debug(self, msg):
        print(msg)
    def warning(self, msg):
        print(msg)
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    elif d['status'] == 'downloading':
        print(d['filename'], d['eta'])

def play_video_in_vlc(video_url):
    player = vlc.MediaPlayer(video_url)
    player.play()
    try:
        input("Press Enter to stop playing...")
    finally:
        player.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python play_youtube_in_vlc.py <YouTube URL>")
        sys.exit(1)
    youtube_url = sys.argv[1]
    video_url = get_best_stream(youtube_url)
    play_video_in_vlc(video_url)
