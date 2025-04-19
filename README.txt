This is a simple, Python-based YouTube downloader script. It grabs the best available video (up to 1080p) and merges it with audio using ffmpeg.

	If you don't have python, get it here:

	https://www.python.org/downloads/

	**Make sure to leave "add to PATH" checked during the installation if you're on a windows machine!

**Requires yt-dlp and rich**

Ex:
"pip install yt-dlp"
"pip install rich"

DOWNLOADING FFMPEG:
https://www.gyan.dev/ffmpeg/builds/

ffmpeg is a utility for working with audio and video files. Here it's being used to merge together the audio and video from a YouTube download as YouTube stores them separately

On the page linked above, look for the "release builds" section and download "ffmpeg-release-essentials.zip".
	Unzip this and place it in the folder with the rest of these files, go ahead and just rename it "ffmpeg".
	The "YouTube Video Downloader" directory (folder) should look something like this now:
	YouTube Video Downloader/
	├── ffmpeg
	├── download.py
	├── urls.txt
	├── README.txt
	└── requirements.txt

HOW TO USE:

If you had to install python, ffmpeg, or the required libraries, it may be best to restart your computer before using it (first time only)

Open up your command line in this folder and run the python script. Ex: "python download.py" 
	It will either look for a list of urls separated by line in "urls.txt", and if it doesn't find any, it will ask for a single 	url to download from. Files will automatically be downloaded into this folder.
