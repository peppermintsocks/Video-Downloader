import os
from yt_dlp import YoutubeDL
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

def get_urls_from_file_or_prompt(filename="urls.txt"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
            if urls:
                print(f"Found {len(urls)} URL(s) in {filename}.")
                return urls
    # If file doesn't exist or is empty, ask user
    url = input("Enter a YouTube URL: ")
    return [url]

def download_video(url):
    progress = Progress(
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        TimeRemainingColumn()
    )

    task = None

    def progress_hook(d):
        nonlocal task
        if d['status'] == 'downloading':
            if task is None:
                filename = d['info_dict']['title'][:30] + "..." if len(d['info_dict']['title']) > 30 else d['info_dict']['title']
                task = progress.add_task("", filename=filename, total=d.get("total_bytes") or d.get("total_bytes_estimate"))
            progress.update(task, completed=d['downloaded_bytes'])
        elif d['status'] == 'finished':
            progress.update(task, completed=progress.tasks[0].total)

    ydl_opts = {
        'format': 'bestvideo[vcodec^=avc1][height<=1080]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]',
        'progress_hooks': [progress_hook],
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ffmpeg_location' : './ffmpeg/bin'
    }

    with progress:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if __name__ == "__main__":
    urls = get_urls_from_file_or_prompt()
    for url in urls:
        print(f"\n▶ Downloading: {url}")
        download_video(url)