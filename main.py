import time
from player_module.file_watcher import FileChangeHandler, Observer
from player_module.stream_extractor import get_best_stream
from player_module.video_player import play_video_in_vlc

LINKS_FILE = 'data/youtube_links.txt'

def read_and_play_videos():
    try:
        while True:
            with open(LINKS_FILE, 'r') as file:
                links = file.readlines()
                if not links:
                    print("No links found. Waiting...")
                    time.sleep(10)
                    continue
                for line in links:
                    if line.strip():
                        url, name = line.strip().split(maxsplit=1)
                        print(f'Playing: {name}')
                        video_url = get_best_stream(url)
                        play_video_in_vlc(video_url)
    except KeyboardInterrupt:
        print("Stopping video playback.")

if __name__ == "__main__":
    event_handler = FileChangeHandler(read_and_play_videos)
    observer = Observer()
    observer.schedule(event_handler, path='data', recursive=False)
    observer.start()
    try:
        read_and_play_videos()
    finally:
        observer.stop()
        observer.join()

