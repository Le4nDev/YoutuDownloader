# YouTube Playlist to MP3 Converter

**Table of Contents**
- [Overview](#overview)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Notes](#notes)
- [License](#license)

## Overview

This is a command-line program that allows you to download YouTube playlists and convert them into MP3 audio files. You can use this program to save your favorite music in MP3 format and listen to it anytime, even when you're offline.

## Requirements

Make sure you have Python 3 installed on your system. You'll also need to install the following Python libraries:

- pytube
- moviepy
- tqdm

You can install these libraries using pip:

```bash
pip install pytube moviepy tqdm
```

## How to Use
Run the program from the command line:
```bash
python main.py
```
You'll be prompted to enter the URL of the YouTube playlist you want to download. You can also enter "n" to close the program.

The program will download the videos from the playlist, convert them into MP3 files, and store them in a folder called "mp3_sounds."

After completing the download and conversion of the current playlist, the program will ask if you want to process another playlist. You can enter "y" to continue or "n" to close the program.

If you choose to continue, repeat steps 2-4 for the next playlist.

## Notes
Ensure that the YouTube playlists you want to download are public and accessible to avoid download issues.

The program will rename MP3 files by removing special characters and accents to ensure file system compatibility.

MP3 files will be stored in a folder named "mp3_sounds" within the directory where the program is located.

If you want to stop the execution at any time, you can press "Ctrl + C" in the terminal.

## License
This program is under the MIT license. You can refer to the LICENSE file for more details.
