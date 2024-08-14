import moviepy.editor as mp
from tkinter.filedialog import askopenfilename

# Prompt user to select a video file
vid_path = askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])

# Load the video file
video = mp.VideoFileClip(vid_path)

# Extract the audio from the video
aud = video.audio

# Save the extracted audio to an MP3 file
aud.write_audiofile("demo.mp3")

print("GoodBye")
