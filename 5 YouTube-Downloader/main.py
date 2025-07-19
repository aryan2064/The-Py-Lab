import yt_dlp
import re


def is_valid_url(url):
    pattern = r"^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+"
    return re.match(pattern, url) is not None


def get_quality_choice():
    print("\nChoose download option:")
    print("1. Best quality (up to 4K)")
    print("2. 1080p")
    print("3. 720p")
    print("4. Audio only (MP3)")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        return "bestvideo+bestaudio/best", "mp4"
    elif choice == "2":
        return "bestvideo[height<=1080]+bestaudio/best[height<=1080]", "mp4"
    elif choice == "3":
        return "bestvideo[height<=720]+bestaudio/best[height<=720]", "mp4"
    elif choice == "4":
        return "bestaudio", "mp3"
    else:
        return "bestvideo+bestaudio/best", "mp4"


def download_video(url):
    format_code, ext = get_quality_choice()

    ydl_opts = {
        "format": format_code,
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [],
    }

    if ext == "mp3":
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]

    try:
        print("\nDownloading...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "Unknown")
            print(f"\nDownload complete: {title}")
            return True
    except yt_dlp.utils.DownloadError:
        print("\nDownload failed")
        return False
    except Exception:
        print("\nDownload failed")
        return False


def main():
    print("=" * 40)
    print("   YouTube Video Downloader")
    print("=" * 40)

    while True:
        url = input("\nEnter YouTube video URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("\nGoodbye!")
            break

        if not is_valid_url(url):
            print("\nInvalid URL")
            continue

        download_video(url)

        again = input("\nDownload another video? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()