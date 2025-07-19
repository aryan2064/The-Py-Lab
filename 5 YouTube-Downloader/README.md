# YouTube Downloader

A terminal-based YouTube video and audio downloader with quality selection using `yt-dlp`.

## Features

- Download videos in multiple quality options (up to 4K, 1080p, 720p)
- Extract audio as MP3
- YouTube URL validation
- Loop to download multiple videos in one session

## Requirements

- Python 3.x
- `yt-dlp`

```bash
pip install yt-dlp
```

For MP3 audio extraction, [FFmpeg](https://ffmpeg.org/) must also be installed and available on your PATH.

## How to Run

```bash
python main.py
```

## Example Output

```
========================================
   YouTube Video Downloader
========================================

Enter YouTube video URL (or 'q' to quit): https://www.youtube.com/watch?v=dQw4w9WgXcQ

Choose download option:
1. Best quality (up to 4K)
2. 1080p
3. 720p
4. Audio only (MP3)
Enter your choice (1-4): 2

Downloading...

Download complete: Rick Astley - Never Gonna Give You Up

Download another video? (y/n): n

Goodbye!
```