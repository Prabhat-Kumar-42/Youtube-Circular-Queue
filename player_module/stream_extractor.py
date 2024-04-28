import yt_dlp
from player_module.logger import MyLogger
from player_module.hook import my_hook

def get_best_stream(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'logger': MyLogger(),  # Enable logging
        'progress_hooks': [my_hook],  # Progress hook
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get('url')
        return video_url


