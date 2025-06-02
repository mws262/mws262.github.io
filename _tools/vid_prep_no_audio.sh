#!/bin/bash

# Usage: ./strip_audio_compress.sh input.mp4 output.mp4

if [ $# -ne 2 ]; then
  echo "Usage: $0 input.mp4 output.mp4"
  exit 1
fi

INPUT="$1"
OUTPUT="$2"

ffmpeg -i "$INPUT" -b:v 2000k -c:v libx264 -preset slow -an "$OUTPUT"
