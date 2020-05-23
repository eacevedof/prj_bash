import os
import zipfile

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
    if not is_file(pathfile):
        return print(f"Not zipped: File {pathfile} does not exist")

    if is_file(pathzip):
        return print(f"Not zipped: File {pathzip} already exists")

    zipfile.ZipFile(pathzip, mode="w").write(pathfile)
    # print(ziphandler,"ziphandler")
    #ziphandler.close()
    
