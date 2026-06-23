import os

print("=" * 50)
print("AUTONOMOUS YOUTUBE PIPELINE")
print("=" * 50)

# Generate audio
print("\n[1/4] Generating audio...")
os.system("python scripts\\tts.py")

# Generate subtitles
print("\n[2/4] Generating subtitles...")
os.system("whisper output\\audio.mp3 --model base --output_format srt")

# Generate long-form video
print("\n[3/4] Generating long-form video...")
os.system(
    "\"C:\\Users\\FIVERR ACCOUNT1\\Downloads\\ffmpeg-8.1.1-essentials_build\\bin\\ffmpeg.exe\" "
    "-y -loop 1 -i assets\\background.jpg "
    "-i output\\audio.mp3 "
    "-c:v libx264 -tune stillimage "
    "-c:a aac -b:a 192k "
    "-shortest output\\long_video.mp4"
)

# Generate shorts
print("\n[4/4] Generating short-form videos...")

os.system(
    "\"C:\\Users\\FIVERR ACCOUNT1\\Downloads\\ffmpeg-8.1.1-essentials_build\\bin\\ffmpeg.exe\" "
    "-y -i output\\long_video.mp4 -ss 0 -t 8 output\\short1.mp4"
)

os.system(
    "\"C:\\Users\\FIVERR ACCOUNT1\\Downloads\\ffmpeg-8.1.1-essentials_build\\bin\\ffmpeg.exe\" "
    "-y -i output\\long_video.mp4 -ss 8 -t 8 output\\short2.mp4"
)

os.system(
    "\"C:\\Users\\FIVERR ACCOUNT1\\Downloads\\ffmpeg-8.1.1-essentials_build\\bin\\ffmpeg.exe\" "
    "-y -i output\\long_video.mp4 -ss 16 -t 8 output\\short3.mp4"
)

print("\nPipeline completed successfully!")
print("Files generated:")
print("- audio.mp3")
print("- audio.srt")
print("- long_video.mp4")
print("- short1.mp4")
print("- short2.mp4")
print("- short3.mp4")