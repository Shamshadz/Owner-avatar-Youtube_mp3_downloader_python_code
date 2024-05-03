from pytube import YouTube, Playlist
import os

def download_mp3(url, destination):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        out_file = audio.download(output_path=destination)
        base, _ = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded in .mp3 format.")
        return True
    except Exception as e:
        print("Error downloading", url, ":", str(e))
        return False

def playlist_urls():
    playlist_url = input("Enter the URL of the YouTube playlist: \n>> ")
    playlist = Playlist(playlist_url)
    destination = input("Enter the destination (leave blank for current directory):\n>> ") or './music'
    failed_downloads_file = "failed_downloads.txt"

    print("Downloading videos from the playlist...")
    with open(failed_downloads_file, 'a') as f:
        for url in playlist.video_urls:

            print("Downloading:", url)
            if not download_mp3(url=url, destination=destination):
                f.write(url + '\n')

    print("Playlist download completed.")

def download_failed_urls():

    failed_downloads_file = "failed_downloads.txt"
    destination = input("Enter the destination (leave blank for current directory):\n>> ") or './music'

    try:
        with open(failed_downloads_file, 'r') as f:
            urls = f.readlines()
        
        for url in urls:
            url = url.strip()  # Remove leading/trailing whitespaces and newlines
            print("Downloading:", url)
            if not download_mp3(url=url, destination=destination):
                print("Failed to download:", url)
    except Exception as e:
        print("Error:", str(e))

if __name__=="__main__":

    # playlist_urls()
    download_failed_urls()
