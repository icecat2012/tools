Speed Video:
1. input a video to speedup or slowdown
speedVideo -f [video file path] -o [output dir] -s [speed, default=1.0] -c [output fps, default=30]

Merge Video:
1. The name of the video files in input dir need to be i.mp4, where i is an integer number
2. The output.mp4 contains the input mp4s, which are sorted by the integer (0.mp4, 1.mp4, 2.mp4 ...)
mergeVideo -i [input dir] -o [output dir] -s [speed, default=1.0] -c [output fps, default=30]

Cut Video by Time:
1. Output a video clip
cutVideo -f [video file path] -o [output dir] [start minute] [start second] [end minute] [end second]
e.g., Cut a video clip from 1:30 to 2:00
cutVideo -f [video file path] -o [output dir] 1 30 2 0

Mute Video:
1. Output a video clip
muteVideo -f [video file path] -o [output dir]
e.g., Mute a video
muteVideo -f [video file path] -o [output dir]
