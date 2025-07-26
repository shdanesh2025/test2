from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=VIDEO_ID"  # replace with actual URL

ydl_opts = {
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'skip_download': True,
    'outtmpl': 'subtitle.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
