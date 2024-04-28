import vlc

def play_video_in_vlc(video_url):
    player = vlc.MediaPlayer(video_url)
    player.play()
    try:
        input("Press Enter to stop playing...")
    finally:
        player.stop()

