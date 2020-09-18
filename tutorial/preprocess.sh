#!/bin/bash

echo file in: $1
ffmpeg -i $1 -loglevel error -c:a pcm_s16le -af "highpass=f=300, lowpass=f=3000" -filter:a loudnorm -ar 8000 -f wav -y $2
echo file out: $2