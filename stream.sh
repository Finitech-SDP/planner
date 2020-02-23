#!/usr/bin/env bash

# https://stackoverflow.com/a/16836338/4466589
device=${1:-/dev/video2}

vlc -v v4l2://$device:width=1280:height=1024 --v4l2-chroma=UYVY --v4l2-fps=5 --sout "#transcode{vcodec=theo,vb=1024,scale=1,acodec=none,fps=25}:standard{access=http,mux=ogg,dst=:8081/stream.ogg}"
