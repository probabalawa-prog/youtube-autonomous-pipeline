# Autonomous YouTube Pipeline

## Overview

This project automatically generates one long-form video and three short-form videos from a single text input using free tools.

## Workflow

script.txt
↓
Edge-TTS
↓
audio.mp3
↓
Whisper
↓
audio.srt
↓
FFmpeg
↓
long_video.mp4
↓
short1.mp4, short2.mp4, short3.mp4

## Tools Used

* Python
* Edge-TTS
* OpenAI Whisper
* FFmpeg

## Generated Files

* audio.mp3
* audio.srt
* long_video.mp4
* short1.mp4
* short2.mp4
* short3.mp4

## Result

A minimal autonomous YouTube content generation pipeline built using free tools and capable of generating long-form and short-form content from a single text input.
## Installation

Install Python:

https://www.python.org/downloads/

Install required packages:

pip install edge-tts
pip install openai-whisper
pip install moviepy

Install FFmpeg and add it to your system PATH.

## Usage

1. Edit the file:

input/script.txt

2. Enter the text you want to convert into a video.

3. Run:

python run_pipeline.py

4. Generated files will appear in:

output/

## Output Files

- audio.mp3
- audio.srt
- long_video.mp4
- short1.mp4
- short2.mp4
- short3.mp4
