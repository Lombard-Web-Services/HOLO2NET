#!/bin/bash
file=$1
echo "translating $file to hologram.mp4";
backgroundremover -i $file -tv -o "v.mp4"
ffmpeg -i v.mp4 -vf "rotate=45*(PI/180):bilinear=0" vTL.mp4
ffmpeg -i vTL.mp4 -vf vflip vTR.mp4
ffmpeg -i vTL.mp4 -vf hflip vBL.mp4
ffmpeg -i vTL -vf "rotate=225*(PI/180):bilinear=0" vBR.mp4
ffmpeg -i vTL.mp4 -i vTR.mp4 -i vBL.mp4 -i vBR.mp4 -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" hologram.mp4
echo "Script finished !";
