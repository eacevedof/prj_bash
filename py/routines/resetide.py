# https://tsukie.com/en/technologies/how-to-reset-trial-time-for-jetbrains-products/
# https://trello.com/c/dUy29phH/2-resetear-periodo-de-evaluacion-phpstorm

#1. Terminate your JetBrains application

#2. Remove all *.key files in /Users/<user>/Library/Application Support/JetBrains/PhpStorm2020.1/eval 

#3. remove /Users/<user>/Library/"Application Support"/JetBrains/PhpStorm2020.1/options/options.xml (esto no existe)
    # cd /Users/<user>/Library/"Application Support"/JetBrains/PhpStorm2020.1/options
    
#4. Remove any Jetbrains related keys in ~/Library/Preferences/com.apple.java.util.prefs.plist (ok)

#5. Remove all JetBrains related plist files in ~/Library/Preferences/
    # /Users/<user>/Library/preferences
    """
    -rw-------    1 <user>  staff     280 21 jul 12:56 com.jetbrains.PhpStorm.plist
    -rw-------@   1 <user>  staff     181 15 jul 21:58 jetbrains.phpstorm.aba76028.plist
    -rw-------@   1 <user>  staff      87 25 jun 21:57 jetbrains.jetprofile.asset.plist
    """