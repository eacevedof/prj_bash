import sys
from pprint import pprint
import os
from subprocess import run
import math


# py.sh ffmpeg path-to-in-file.mp4  path-to-out-file.mp4 50
# raw command: ffmpeg -i $HOME/Downloads/v/yyy.mp4 -b 3800k $HOME/Downloads/v/z/zzz.mp4
def index(pathin, pathto, min_duration=0):
    min_duration = int(min_duration)
    if min_duration:
        duration = min_duration * 60
        r = (32000 + 100000) * (1.073741824 * duration) / (8 * 1024)
        r = math.floor(r)
        pprint(f"best bitrate: {r}")
        return

    if not os.path.exists(pathin):
        pprint(f"not a file: {pathin}")
        sys.exit()

    cmd = f"ffmpeg -i {pathin} -b 3800k {pathto} -y"
    cmd = "ls -lat"

    result = run(cmd, capture_output=True, shell=True)
    if result.stderr.decode("utf-8"):
        print("\t\nerror:")
        print(result.stderr.decode("utf-8"))
        return

    print(result.stdout.decode("utf-8"))
