import os
import zipfile
import ntpath
import sys


"""
Example:
"""
def is_dir(pathdir):
    return os.path.isdir(pathdir)

def is_file(pathfile):
    return os.path.exists(pathfile)


# pathdir: path/to/folder/to-be/zipped
# pathzip: path/to/resulting-file.zip
def zipdir(pathdir, pathzip):

    if not is_dir(pathdir):
        return print(f"zipit: Not zipped: directory {pathdir} does not exist")

    if is_file(pathzip):
        return print(f"zipit: Not zipped: File {pathzip} already exists")

    parentdir = os.path.realpath(pathdir+"/..")
    # print("PARENTDIR: "+parentdir); 
    # fileorig = ntpath.basename(pathfile)
    foldertozip = pathdir.split("/")[-1]
    #print(foldertozip); sys.exit()
    filezip = ntpath.basename(pathzip)

    os.chdir(parentdir)
    ziphandler = zipfile.ZipFile(filezip, 'w', zipfile.ZIP_DEFLATED)
    # ziph is zipfile handle
    for root, dirs, files in os.walk(foldertozip):
        #print("root:"+root)
        for file in files:
            ziphandler.write(os.path.join(root, file))

    ziphandler.close()

    pathzipped = parentdir+"/"+filezip
    # si existe el comprimido y no es igual a la ruta de destino donde deberia estar moverse 
    # es decir pathzip
    if is_file(pathzipped) and pathzipped != pathzip:
        os.replace(pathzipped,pathzip)
        # os.remove(pathzipped)


def zipfilesingle(pathfile, pathzip):
    # print(f"from: {pathfile} to {pathzip}")
    if not is_file(pathfile):
        return print(f"zipit: Not zipped: File {pathfile} does not exist")

    if is_file(pathzip):
        return print(f"zipit: Not zipped: File {pathzip} already exists")

    pathdirorig = os.path.dirname(os.path.realpath(pathfile))
    os.chdir(pathdirorig)

    fileorig = ntpath.basename(pathfile)
    filezip = ntpath.basename(pathzip)

    zipf = zipfile.ZipFile(filezip,"w", zipfile.ZIP_DEFLATED)
    zipf.write(fileorig)
    zipf.close()

    pathzipped = pathdirorig+"/"+filezip
    # si existe el comprimido y no es igual a la ruta de destino donde deberia estar moverse 
    # es decir pathzip
    if is_file(pathzipped) and pathzipped != pathzip:
        os.replace(pathzipped,pathzip)
        # os.remove(pathzipped)

    # zipfile.ZipFile(pathzip, mode="w").write(pathfile) no va
    # print(ziphandler,"ziphandler")
    #ziphandler.close()
    
