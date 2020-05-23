import os
import zipfile
import ntpath


"""
Example:
"""
def is_file(pathfile):
    return os.path.exists(pathfile)

# pathdir: dir to zip
# ziphandler:  zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
def zipdir_zh(pathdir, ziphandler):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(pathdir):
        for file in files:
            ziphandler.write(os.path.join(root, file))

# pathdir: path/to/folder/to-be/zipped
# pathzip: path/to/resulting-file.zip
def zipdir(pathdir, pathzip):
    ziphandler = zipfile.ZipFile(pathzip, 'w', zipfile.ZIP_DEFLATED)
    if is_file(pathzip):
        ziphandler.close()
        return print(f"Not zipped: File {pathzip} already exists")

    # ziph is zipfile handle
    for root, dirs, files in os.walk(pathdir):
        for file in files:
            ziphandler.write(os.path.join(root, file))

    ziphandler.close()


def zipfilesingle(pathfile, pathzip):
    print(f"from: {pathfile} to {pathzip}")
    if not is_file(pathfile):
        return print(f"Not zipped: File {pathfile} does not exist")

    if is_file(pathzip):
        return print(f"Not zipped: File {pathzip} already exists")

    pathdirorig = os.path.dirname(os.path.realpath(pathfile))
    os.chdir(pathdirorig)

    fileorig = ntpath.basename(pathfile)
    filezip = ntpath.basename(pathzip)

    zipf = zipfile.ZipFile(filezip,"w", zipfile.ZIP_DEFLATED)
    zipf.write(fileorig)
    zipf.close()

    pathzipped = pathfile+"/"+filezip 
    if is_file(pathzipped) and pathzipped != pathzip:
        os.replace(pathzipped,pathzip)
        os.remove(pathzipped)

    # zipfile.ZipFile(pathzip, mode="w").write(pathfile) no va
    # print(ziphandler,"ziphandler")
    #ziphandler.close()
    
