#!/bin/bash
file=$1
echo "translating $file to hologram.mp4";
backgroundremover -i $file -tv -o "v.mp4"
ffmpeg -i v.mp4 -filter_complex "\
[0:v]rotate=45*PI/180:bilinear=0,split=3[vTL1][vTL2][vTL3]; \
[vTL1]vflip[vTR]; \
[vTL2]hflip[vBL]; \
[0:v]rotate=315*PI/180:bilinear=0,hflip[vBR]; \
[vTL3][vTR][vBL][vBR]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0,fps=22[outv]" \
-map "[outv]" -map 0:a? -c:v libx264 -pix_fmt yuv420p -c:a copy hologram.mp4
echo "Script finished !";
