#!/bin/bash
# convert audios in dir

dir_in=/mnt/raid10/home/SPEECH/Diarization/Clustering/test_sounds/noise_samples
dir=$dir_in

i=1
for file in $(find $dir_in/ -name '*.mp3' | xargs -P 20);
do 
ffmpeg -i $file -c:a pcm_s16le -af "highpass=f=300, lowpass=f=3000" -filter:a loudnorm -ar 8000 -f wav -y $dir/final_$i.wav
i=$((i+1))
done