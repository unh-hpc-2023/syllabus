#! /bin/bash

FIRST_FRAME=1
LAST_FRAME=119

python lim1.py
for a in `seq $FIRST_FRAME $LAST_FRAME`; do
    python plot.py data_$a.npy data_$a.png
done

ffmpeg -y -r 8 -i data_%d.png -r 30 -pix_fmt yuv420p lim1.mp4

rm -f *.png *.npy 
