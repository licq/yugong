from yugong.downloader import Downloader
from pathlib import Path
from yugong.audio_splitter import AudioSplitter


downloader = Downloader(Path.cwd() / "data")
video = downloader.download("https://www.youtube.com/watch?v=F1bXfnrzAxM&ab_channel=MatthewGrdinic")
splitter = AudioSplitter()
splitter.split(video)
print(video.__repr__())