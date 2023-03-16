from moviepy.editor import *
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="./", help="input video dir")
parser.add_argument("-o", "--output", type=str, default="./", help="output video file")
parser.add_argument("-s", "--speed", type=str, default="1", help="speedup or slow down, default=1")
parser.add_argument("-c", "--fps", type=str, default="30", help="fps, default=30")
args = parser.parse_args()

if __name__=='__main__':
    if not os.path.exists(args.input) or not os.path.isdir(args.input):
        print('No input dir')
        exit()
    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        print('No output dir')
        exit()

    files = os.listdir(args.input)
    if len(files)<=0:
        exit()

    files = [[f, int(f.split('.', 1)[0])] for f in files]
    files = sorted(files, key=lambda x:x[1])

    L = list()
    for f in files:
        filename = f[0]
        video = VideoFileClip(os.path.join(args.input, filename))
        L.append(video)

    final_clip = concatenate_videoclips(L)
    final_clip = final_clip.fx(vfx.speedx, float(args.speed))
    final_clip.to_videofile(os.path.join(args.output, "output.mp4"), fps=int(args.fps), remove_temp=True)