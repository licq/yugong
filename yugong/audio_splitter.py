import subprocess
from yugong.logger import logger

class AudioSplitter:
    def split(self, video):
        audio_file_name = f"{video.file.stem}.{video.acodec}"
        output = subprocess.run(["ffmpeg", "-i", video.file, "-vn", "-acodec", "copy", audio_file_name], cwd=video.file.parent, capture_output=True, text=True)
        logger.info(output)
        video.audio_file = video.file.parent / audio_file_name