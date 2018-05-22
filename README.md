# Cut information out of videos

Automate video editing to prepare EM material for presentations and sharing.

# Usage

- Install Python 3
- Clone this repository

```
git clone https://github.com/tnc-ca-geo/video.git
```

- Install requirements

```
cd video
pip install -r requirements.txt
```

- Edit clean_videos.py

```
IN_DIRECTORY = {location of .mp4 files, subdirectories will be searched as well}
OUT_DIRECTORY = {destination of processed videos, subdirectories will be created}
PERCENTAGE = {percentage of height that will be cut from the top}
```

- Run

```
python clean_videos.py
```

Every processed video will start to play for QC. Close at any point in order to proceed with the next one. If autoplay is not desired comment out the last line of the script. Change ...

```
modified.preview()
```

to 

```
# modified preview()
```

All done
