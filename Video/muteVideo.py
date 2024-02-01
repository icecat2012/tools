from moviepy.editor import VideoFileClip
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, default="", help="input video")
parser.add_argument("-o", "--output", type=str, default="./", help="output dir")
args = parser.parse_args()

if __name__=='__main__':
    if not os.path.exists(args.file) or not os.path.isfile(args.file):
        print('No input video')
        exit()
    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        print('No output dir')
        exit()

    ext = args.file.rsplit('.', 1)[1]
    videoclip = VideoFileClip(args.file)
    new_clip = videoclip.without_audio()
    new_clip.write_videofile(os.path.join(args.output, "output.{}".format(ext)), codec='libx264', remove_temp=True)