from yugong.downloader import Downloader
from pathlib import Path

downloader = Downloader(Path.cwd() / "data")
video = downloader.download("https://www.youtube.com/watch?v=F1bXfnrzAxM&ab_channel=MatthewGrdinic")
print(video)