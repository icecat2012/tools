from moviepy.editor import *
import os
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, default="", help="input video")
parser.add_argument("-o", "--output", type=str, default="./", help="output dir")
parser.add_argument("-s", "--speed", type=str, default="1", help="speedup or slow down, default=1")
parser.add_argument("-c", "--fps", type=str, default="30", help="fps, default=30")
args = parser.parse_args()

if __name__=='__main__':
    if not os.path.exists(args.file) or not os.path.isfile(args.file):
        print('No input video')
        exit()
    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        print('No output dir')
        exit()

    ext = args.file.rsplit('.', 1)[1]
    myclip = VideoFileClip(args.file)
    final_clip = myclip.fx( vfx.speedx, float(args.speed))
    final_clip.to_videofile(os.path.join(args.output, "output.{}".format(ext)), fps=int(args.fps), remove_temp=True)