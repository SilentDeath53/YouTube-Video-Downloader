#!/usr/bin/env python3
"""Simple YouTube downloader using yt-dlp."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from yt_dlp import YoutubeDL


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download YouTube videos or extract audio using yt-dlp.",
    )
    parser.add_argument(
        "url",
        help="YouTube video URL to download",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="downloads",
        help="Directory for downloaded files (default: downloads)",
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Extract audio only (best available format)",
    )
    parser.add_argument(
        "--format",
        default="bestvideo+bestaudio/best",
        help="yt-dlp format selector (default: bestvideo+bestaudio/best)",
    )
    return parser


def download_video(url: str, output_dir: Path, audio_only: bool, format_selector: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts: dict[str, object] = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "format": format_selector,
        "noplaylist": True,
    }

    if audio_only:
        ydl_opts.update(
            {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
        )

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        download_video(
            url=args.url,
            output_dir=Path(args.output_dir),
            audio_only=args.audio_only,
            format_selector=args.format,
        )
    except Exception as exc:
        print(f"Download failed: {exc}", file=sys.stderr)
        return 1

    print("Download completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
