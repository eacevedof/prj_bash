# routines.image.py
# py.sh images.reducedpi <PATH>
# py.sh images.reducedpi /Users/ioedu/Downloads/ech-nuevas
#print("routines.images.py")
from tools.tools import is_dir, scandir, get_now, pr
import shutil
import os

# python3 -m pip install Pillow
from PIL import Image

def is_extensionok(filename):
    extensions = ["jpg","png","jpeg"]
    # ext = filename.lower().split(".")[-1:]
    ext = os.path.splitext(filename)[1].replace(".","")
    #pr(ext,"ext")
    if ext in extensions:
        return True
    return False


def reducedpi(pathfolder, resolution=100):
    print(f"process: pathfolder={pathfolder}, resolution={resolution}")
    timeini = get_now()
    pr(f"image.reducedpi: of {pathfolder}. {timeini}")

    if not is_dir(pathfolder):
        return die(f"Error pathfolder {pathfolder} is not a directory")

    files = scandir(pathfolder)
    
    for filename in files:
        pr(f"handling: {filename}")

        pathfile = f"{pathfolder}/{filename}"
        if not is_extensionok(filename) or is_dir(pathfile):
            continue
        
        extension = os.path.splitext(filename)[1].replace(".","")
        pathfilenew = os.path.splitext(pathfile)[0]

        pathfilenew = f"{pathfilenew}-{resolution}x{resolution}.{extension}"
        pr(f"generated file: {pathfilenew}")
        objimg = Image.open(pathfile)
        objimg.save(pathfilenew, dpi=(resolution,resolution))

    timeend = get_now()
    pr(f"...image reduce of {pathfolder} has finished. ini:{timeini} - end:{timeend}")