# pip3 install moviepy
# http://shihnung.blogspot.com/2019/02/python_13.html
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import argparse

def ez_version(args, start, end): # fails when video or clip is small
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    ffmpeg_extract_subclip(args.source, start, end, targetname=args.output)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default="", help="input video file")
    parser.add_argument("-o", "--output", type=str, default="", help="output video dir")
    parser.add_argument("start_min", type=str, default=0)
    parser.add_argument("start_sec", type=str, default=0)
    parser.add_argument("end_min", type=str, default=0)
    parser.add_argument("end_sec", type=str, default=0)
    args = parser.parse_args()

    if not os.path.exists(args.file) or not os.path.isfile(args.file):
        print('No input file')
        exit()
    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        print('No output dir')
        exit()

    start = int(args.start_min)*60 + int(args.start_sec)
    end = int(args.end_min)*60 + int(args.end_sec)
    if start>=end:
        print('input time is illegal')
        exit()

    ext = args.file.rsplit('.', 1)[1]
    # ez_version(args, start, end)
    with VideoFileClip(args.file) as video:
        new = video.subclip(start, end)
        new.write_videofile(os.path.join(args.output, 'output.{}'.format(ext)))#, audio_codec='aac'