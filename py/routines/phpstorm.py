
from tools.tools import pr, shsudo,die

dicconf = {
    "pathcache1": "/Users/ioedu/Library/Caches/JetBrains/PhpStorm2020.1", # PhpStorm2020 # ls -lat | grep Jet existe la carpeta PhpStorm

    "pathphp": "/Users/ioedu/Library/Application Support/PhpStorm",  #webview

    "pathappsup1": "/Users/ioedu/Library/Application Support/JetBrains/consentOptions", #flag accepted
    "pathappsup2": "/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.1/eval", #eval key
    "pathappsup3": "/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.1/phpstorm.vmoptions",

    # https://trello-attachments.s3.amazonaws.com/5ecce8fe2983ed33bd68451c/1056x466/c9ffe4b4c7d1fc5c7d1131ac93525e98/image.png
    "pathprefs1": "/Users/ioedu/Library/Preferences/jetbrains.phpstorm.aba76028.plist",
    
    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/1503497d7d710eab81343e7fb9d74ab7/image.png
    "pathprefs2": "/Users/ioedu/Library/Preferences/com.jetbrains.PhpStorm.plist",

    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/a72f26e83e6612c57f5bdee563753b92/image.png
    "pathprefs3": "/Users/ioedu/Library/Preferences/jetbrains.jetprofile.asset.plist",

    # https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/5f69b438df665206ee82b29a0154be2d/image.png
    "pathxmlmanual": "/Users/ioedu/Library/Preferences/com.apple.java.util.prefs.plist", #manual quitar entradas jetbrains 
}

sudopass = ""

def rmdir(pathdir):
    cmd = f"rm -fr {pathdir}"
    pr(cmd,"rmdir:")
    shsudo(cmd, sudopass)

def rmdirall(pathfolder):
    cmd = f"rm -f {pathfolder}/*"
    pr(cmd,"rmdirall:")
    shsudo(cmd, sudopass)

def rmfile(pathfile):
    cmd = f"rm -f {pathfile}"
    pr(cmd,"rmfile:")
    shsudo(cmd, sudopass)    

def index(supass):
    if not supass:
        pr("No sudo pass")
        die()

    sudopass = supass
    pr(sudopass,"sudopass")

    rmdir(dicconf["pathcache1"])
    die()


    rmdirall(dicconf["pathappsup1"])
    rmdirall(dicconf["pathappsup2"])
    rmfile(dicconf["pathappsup3"])

    rmfile(dicconf["pathprefs1"])
    rmfile(dicconf["pathprefs2"])
    rmfile(dicconf["pathprefs3"])

    pathmanual = dicconf["pathxmlmanual"]
    pr(pathmanual,"Hay que editar esto manualmente")

