import sys, os
from pathlib import Path
import moviepy.editor as mp


output_extension = sys.argv[1] # mp4
codec = sys.argv[2] if len(sys.argv) > 2 else None # libx264
output_indexed = sys.argv[3] == "True" if len(sys.argv) > 3 else False # libx264


for index, filename in enumerate(os.listdir("in"), 1):
	clip = mp.VideoFileClip("in" + "/" + filename)

	if output_indexed:
		newname = str(index)
	else:
		newname = Path(filename).stem

	clip.write_videofile("out/" + newname + "." + output_extension, codec=codec)