from pytube import Playlist
from moviepy.editor import VideoFileClip
from tqdm import tqdm
import re
import os


def clean_filename(filename):
    cleaned_name = re.sub(r'[\\/:"*?<>|]+', '_', filename)
    cleaned_name = re.sub(r'[áàâã]', 'a', cleaned_name)
    cleaned_name = re.sub(r'[éèê]', 'e', cleaned_name)
    cleaned_name = re.sub(r'[íìî]', 'i', cleaned_name)
    cleaned_name = re.sub(r'[óòôõ]', 'o', cleaned_name)
    cleaned_name = re.sub(r'[úùûü]', 'u', cleaned_name)
    return cleaned_name


def create_directory(directory):
    directory = re.sub(r'[\/:*?"<>|]', '_', directory)

    if not os.path.exists(directory):
        os.makedirs(directory)


def download_video_with_progress(video, output_path):
    cleaned_video_title = clean_filename(video.title)
    video_filename = os.path.join(output_path, f'{cleaned_video_title}.mp4')

    if os.path.exists(video_filename):
        print(
            f'Video file for "{cleaned_video_title}" already exists. Skipping download.')
    else:
        pbar = tqdm(total=video.streams.get_highest_resolution(
        ).filesize, unit="B", unit_scale=True)
        video.streams.get_highest_resolution().download(
            output_path=output_path, filename=f'{cleaned_video_title}.mp4')
        pbar.close()


def download_and_convert(video, original_video_dir, mp3_dir, playlist_title):
    mp3_subfolder = os.path.join(mp3_dir, playlist_title)

    mp3_subfolder = re.sub(r'[?]', '', mp3_subfolder)

    create_directory(mp3_subfolder)

    cleaned_video_title = clean_filename(video.title)

    video_filename = os.path.join(
        original_video_dir, f'{cleaned_video_title}.mp4')

    videos_list = list(playlist.videos)

    video_position = videos_list.index(video) + 1

    mp3_filename = os.path.join(
        mp3_subfolder, f'{video_position} - {cleaned_video_title}.mp3')

    if os.path.exists(mp3_filename):
        print(
            f'MP3 file for "{cleaned_video_title}" already exists. Skipping download.')
    else:
        download_video_with_progress(video, original_video_dir)

        video_clip = VideoFileClip(video_filename)
        video_clip.audio.write_audiofile(mp3_filename)

        video_clip.close()
        os.remove(video_filename)

        print(f'Video downloaded and converted to MP3: {mp3_filename}')


while True:
    playlist_url = input(
        'Enter the YouTube playlist URL (or "n" to close the program): ')

    if playlist_url.lower() == 'n':
        print("Closing the program.")
        break

    playlist = Playlist(playlist_url)
    playlist_title = playlist.title

    print(
        f'Total videos in the playlist "{playlist_title}": {len(playlist.video_urls)}')

    original_video_dir = 'temp_original_video'
    create_directory(original_video_dir)

    mp3_dir = 'mp3_sounds'
    create_directory(mp3_dir)

    for video in playlist.videos:
        download_and_convert(video, original_video_dir,
                             mp3_dir, playlist_title)

    user_input = input(
        "Do you want to process another playlist? (y/n): ").strip().lower()
    if user_input == 'n':
        print("Closing the program.")
        break

print("Process completed.")
