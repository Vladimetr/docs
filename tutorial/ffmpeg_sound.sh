#!/bin/bash
# convert single audio

file_in=/mnt/raid10/home/SPEECH/Diarization/destination_folder/audio/szsyz.wav
file_out=/mnt/raid10/home/SPEECH/Diarization/Clustering/test3.wav

ffmpeg -i $file_in -c:a pcm_s16le -af "highpass=f=300, lowpass=f=3000" -filter:a loudnorm -ar 8000 -f wav -y $file_out