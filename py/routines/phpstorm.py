from tools.tools import pr, sh

dicconf = {
    "pathcache1": "/Users/ioedu/Library/Caches/JetBrains/PhpStorm2020.1", # PhpStorm2020 # ls -lat | grep Jet existe la carpeta PhpStorm

    "pathphp": "/Users/ioedu/Library/Application Support/PhpStorm",  #webview

    #"pathjet1": "/Users/ioedu/Library/Application Support/JetBrains", #evaluation key
    "pathjet2": "/Users/ioedu/Library/Application Support/JetBrains/consentOptions", #flag accepted
    "pathjet3": "/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.1/eval", #eval key
    "pathjet4": "/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.1/phpstorm.vmoptions"

    # https://trello-attachments.s3.amazonaws.com/5ecce8fe2983ed33bd68451c/1056x466/c9ffe4b4c7d1fc5c7d1131ac93525e98/image.png
    "pathplist1": "/Users/ioedu/Library/Preferences/jetbrains.phpstorm.aba76028.plist",
    
    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/1503497d7d710eab81343e7fb9d74ab7/image.png
    "pathplist2": "/Users/ioedu/Library/Preferences/com.jetbrains.PhpStorm.plist",

    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/a72f26e83e6612c57f5bdee563753b92/image.png
    "pathplist3": "/Users/ioedu/Library/Preferences/jetbrains.jetprofile.asset.plist",

    # https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/5f69b438df665206ee82b29a0154be2d/image.png
    # "pathxmlmanual": "/Users/ioedu/Library/Preferences/com.apple.java.util.prefs.plist", #manual quitar entradas jetbrains 
}

def index():
    path = dicconf["pathcache1"]
    cmd = f"rm -fr {path}"
    pr(cmd,"pathcache1")
    # sh(cmd)

    
