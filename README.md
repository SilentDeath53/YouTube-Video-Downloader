# YouTube Video Downloader (Python)

A simple, scriptable YouTube downloader built with **yt-dlp**. This project focuses on automation: you can run it from the command line, integrate it into cron jobs, or call it from other scripts.

> Note: Downloading content may be subject to YouTube's Terms of Service and local laws. Use responsibly.

## Features

- Download the best available video + audio quality.
- Extract audio-only (MP3) with FFmpeg.
- Custom output folder and format selector.
- Non-interactive, automation-friendly CLI.

## Requirements

- Python 3.9+
- `yt-dlp`
- **Optional**: `ffmpeg` (required for audio-only extraction)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Download a video (best quality)

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Download to a custom folder

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --output-dir downloads
```

### Audio-only (MP3)

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only
```

### Use a custom format selector

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format "best[ext=mp4]/best"
```

## Automation Examples

### Cron (daily download)

```cron
0 3 * * * /path/to/.venv/bin/python /path/to/downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --output-dir /path/to/downloads
```

### Bash script batch

```bash
#!/usr/bin/env bash
set -euo pipefail

URLS=(
  "https://www.youtube.com/watch?v=VIDEO_ID_1"
  "https://www.youtube.com/watch?v=VIDEO_ID_2"
)

for url in "${URLS[@]}"; do
  python downloader.py "$url" --output-dir downloads
done
```

## Troubleshooting

- **Audio-only fails**: install FFmpeg and ensure `ffmpeg` is on your PATH.
- **403/429 errors**: YouTube may throttle. Try again later or use `--cookies` with `yt-dlp` options in advanced usage.

## Advanced Usage (Optional)

If you need more control, you can pass extra options directly by editing `downloader.py` or wrapping it in another script.

## License

MIT
