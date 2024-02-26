from pathlib import Path
import threading
import yt_dlp
from yugong.logger import logger
from concurrent.futures import ThreadPoolExecutor
from yugong.video import Video

class Downloader:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)

    def download(self, url):
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._download, url)
            future.result()
            return self.parse_info(self.dir(url))
        
    def _download(self, url):
        try:
            data_dir = self.dir(url)
            options = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{data_dir}/%(title)s.%(ext)s',
                'progress_hooks': [self.update_progress],
                'logger': logger,
                'writeinfojson': True,
            }
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
        except Exception as e:
            logger.error(e)
            return False

    def dir(self, url):
        v = url.split("v=")[1].split("&")[0]
        return self.output_dir / v
        
    def update_progress(self, d):
        if d['status'] == 'finished':
            logger.info('Done downloading, now converting ...')
        if d['status'] == 'downloading':
            logger.info(f"Downloading {d['_percent_str']} of {d['_total_bytes_str']} at {d['_speed_str']} ETA {d['_eta_str']}")
        if d['status'] == 'error':
            logger.error(d['error'])
            return False
        return True
    
    def parse_info(self, path):
        json_files = list(path.rglob("*.info.json"))
        if len(json_files) == 0:
            raise Exception("No info.json file found")
        json_file = json_files[0]
        with open(json_file, "r") as f:
            data = f.read()
            video = Video.from_json(data)
            video.file = path / f"{video.title}.{video.ext}"
