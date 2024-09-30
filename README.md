# Tik Tok Caption Generator (python)
forked from [Tik Tok Caption Generator (python)](https://github.com/lernEarnBurn/TikTok-Caption-Generator)
Modified for easier installation, and change the format to more like tiktok captions

## What it does
Takes an mp4 video and adds captions on top

## How it works (from original Readme.md)
+ Uses openai whisper api to create an srt file
+ Uses moviepy to put the captions on the video

## Installation
```bash
pip install -r requirements.txt
```

Install Whisper model 

```bash
pip install -U openai-whisper
```

### Whisper OpenAI
You must also install ffmpeg this for the Whisper model

### MacOs 
```bash
    brew install ffmpeg
```

### Windows (Using Chocolatey)
```bash
    choco install ffmpeg
```

### Arch Linux 
```bash
    sudo pacman -S ffmpeg
```

### Other Installations
[Whisper Github Repo](https://github.com/openai/whisper)

## Notes (lernEarnBurn) 
+ In order to shorten each Token in Whisper I tweaked the source code (see https://github.com/openai/whisper/discussions/223 for details.)

