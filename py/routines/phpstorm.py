
from tools.tools import pr, shsudo,die

dicconf = {
    "pathcache1": "/Users/ioedu/Library/Caches/JetBrains/PhpStorm2020.2", # PhpStorm2020 # ls -lat | grep Jet existe la carpeta PhpStorm
    # aqui se crea otra carpeta PhpStorm2020.2 para lo nuevo instalado

    "pathphp": "'/Users/ioedu/Library/Application Support/PhpStorm'",  #webview

    "pathappsup1": "'/Users/ioedu/Library/Application Support/JetBrains/consentOptions'", #flag accepted
    "pathappsup2": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/eval'", #eval key
    "pathappsup3": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/phpstorm.vmoptions'",
    # "pathappsup4": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/options'", # en duda, creo que hace falta

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

    global sudopass
    sudopass = supass
    pr(sudopass,"sudopass")

    rmdir(dicconf["pathcache1"])
    rmdirall(dicconf["pathappsup1"])
    rmdirall(dicconf["pathappsup2"])
    rmfile(dicconf["pathappsup3"])
    #rmdirall(dicconf["pathappsup4"])

    rmfile(dicconf["pathprefs1"])
    rmfile(dicconf["pathprefs2"])
    rmfile(dicconf["pathprefs3"])

    pathmanual = dicconf["pathxmlmanual"]
    pr(pathmanual,"\n\tHay que editar esto manualmente y GUARDAR\n\t")
    print("\n end phpstorm")

    # creo que la he fastidiado al no guardar de forma manual solo he editado el fichero apple.java.util.prefs.plist
