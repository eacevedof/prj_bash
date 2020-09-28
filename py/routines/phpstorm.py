
from tools.tools import pr, shsudo,die

version = "PhpStorm2020.2"

dicconf = {
    "pathcache1": "/Users/ioedu/Library/Caches/JetBrains/PhpStorm2020.2", # PhpStorm2020 # ls -lat | grep Jet existe la carpeta PhpStorm
    # aqui se crea otra carpeta PhpStorm2020.2 para lo nuevo instalado

    "pathphp": "'/Users/ioedu/Library/Application Support/PhpStorm'",  #webview

    "pathappsup1": "'/Users/ioedu/Library/Application Support/JetBrains/consentOptions'", #flag accepted
    "pathappsup2": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/eval'", #eval key
    "pathappsup3": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/phpstorm.vmoptions'",
    
    # en duda, creo que hace falta.
    # si se elimina toda se queda el ide en blanco y no salta el mensaje de expirado ^^. Habría que afinar los xml
    # a eliminar
    "pathappsup4": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/options'", 

    "pathappsup5": "'/Users/ioedu/Library/Application Support/JetBrains/bl'",
    "pathappsup6": "'/Users/ioedu/Library/Application Support/JetBrains/crl'",
    "pathappsup7": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/port'",
    "pathappsup8": "'/Users/ioedu/Library/Application Support/JetBrains/PhpStorm2020.2/port.lock'", 
    
    # https://trello-attachments.s3.amazonaws.com/5ecce8fe2983ed33bd68451c/1056x466/c9ffe4b4c7d1fc5c7d1131ac93525e98/image.png
    "pathprefs1": "/Users/ioedu/Library/Preferences/jetbrains.phpstorm.aba76028.plist",
    
    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/1503497d7d710eab81343e7fb9d74ab7/image.png
    "pathprefs2": "/Users/ioedu/Library/Preferences/com.jetbrains.PhpStorm.plist",

    #https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/a72f26e83e6612c57f5bdee563753b92/image.png
    "pathprefs3": "/Users/ioedu/Library/Preferences/jetbrains.jetprofile.asset.plist",

    # https://trello-attachments.s3.amazonaws.com/5ecb901159c8b07cc0acc96c/5ecce8fe2983ed33bd68451c/5f69b438df665206ee82b29a0154be2d/image.png
    "pathxmlmanual": "/Users/ioedu/Library/Preferences/com.apple.java.util.prefs.plist", #manual quitar entradas jetbrains 

    #"pathapps1": "/Applications/PhpStorm.app/"
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
    
    
    rmdir(dicconf["pathappsup1"])
    rmdirall(dicconf["pathappsup2"])
    rmfile(dicconf["pathappsup3"])
    #rmdirall(dicconf["pathappsup4"])
    rmfile(dicconf["pathappsup5"])
    rmfile(dicconf["pathappsup6"])
    rmfile(dicconf["pathappsup7"])
    rmfile(dicconf["pathappsup8"])

    rmfile(dicconf["pathprefs1"])
    rmfile(dicconf["pathprefs2"])
    rmfile(dicconf["pathprefs3"])

    #rmfile(dicconf["pathapps1"])

    #pathmanual = dicconf["pathxmlmanual"]
    pr(f"open -a Xcode /Users/ioedu/Library/Preferences/com.apple.java.util.prefs.plist","\n\tHay que editar esto manualmente y GUARDAR\n\t")
    # pr("\n\t cd /Users/ioedu/Library/Preferences/; dir.sh .")
    print("\n end phpstorm")

    # creo que la he fastidiado al no guardar de forma manual solo he editado el fichero apple.java.util.prefs.plist


"""
- Proceso:
- Despues de instalar no hay carpeta en appsupport/jetbrains/<nombre-carpeta> (phpstorm2002.2)
- Al abrir se crea la carpeta con dos archivos: port y port.lock
- Esta esperando el check de confirmacion de las condiciones en modal
- Despues de aceptar Aparece la ventana de seleccion de tema (sigue sin crear nada en nombre-carpeta), solo se crea 
    - consentOptions/accepted (contenido: rsch.send.usage.stat:1.1:0:1601290891421)
- Ofrece un nuevo servicio de "script launcher" que se alojaría en /usr/local/bin/pstorm
- Despues de la previa configuración salta el modal "License Activation" (nada en nombre-carpeta)
    - despues de seleccionar eval, crea en nombre-carpeta:
        /ssl (vacia)
        /eval
            /phpstorm202.evaluation.key
- Aparece modal "Welcome to phpstorm"
    - Cuando se interactua con este se crea en nombre-carpeta:
        /options
            /debugger.xml (inofensivo?)
            /vcs.xml
                <option name="COMMIT_FROM_LOCAL_CHANGES" value="true" />
            /laf.xml
                <laf class-name="com.intellij.ide.ui.laf.darcula.DarculaLaf" />
            /colors.scheme.xml
                <global_color_scheme name="Darcula" />
- Despues de sleccionar el primer proyecto:
    - Se crean (bl y crl) fuera de nombre-carpeta
    - Dentro de nombre-carpeta:
        /plugins
            /extensions.xml
        /tasks
            /proyectoabierto.tasks.zip
            /proyectoabierto.contexts.zip
        /jdbc-drivers
            jdbc-drivers.xml
        /options
            usage.statistics.xml
                <component name="FeatureUsageStatistics" first-run="1601291137722" have-been-shown="false" show-in-other="true" show-in-compilation="true">
            
            other.xml
                <property name="PhpStorm.InitialConfiguration" value="true" />
                <property name="appcds.runOnSecondStart" value="PS-202.7319.77-8640eeb6b0283ebfca389c0e21bbf92ead7acac2c531b235bf179af2cbce2292" />
                <property name="evlsprt3.202" value="18" />
                <property name="ts.lib.d.ts.version" value="3.9.5" />

            databaseDrivers.xml
            
            recentProjects.xml
                <RecentProjectMetaInfo opened="true" projectWorkspaceId="1cfgflcp4e6cMHVqNunciPZvgku">
                <option name="binFolder" value="$APPLICATION_HOME_DIR$/bin" />
                <option name="build" value="PS-202.7319.77" />
                <option name="buildTimestamp" value="1600871323657" />
                <option name="productionCode" value="PS" />
                <option name="projectOpenTimestamp" value="1601291378924" />
                </RecentProjectMetaInfo>
- Despues de configurar el check de "no tips" se crean
    - actionSymmary
        <ActionSummary times="1" last="1601291359437" />
    - other.xml (algo se ha actualizado)
    - textmate_os.xml 
        <BundleConfigBean>
          <option name="name" value="sql" />
          <option name="path" value="$APPLICATION_HOME_DIR$/plugins/textmate/lib/bundles/sql" />
        </BundleConfigBean>
    - ide.general.xml
        <option name="showTipsOnStartup" value="false" />
- Despues de tocar el primer archivo del proyecto abierto:
    - se crea en nombre-carpeta 
        workspace/<hash>.xml con la config del fichero que estoy visualizando
    - En options
        lightEdit.xml  una lista de archivos soportados
        actionSummary.xml se guarda la acción realizada
- Al abrir otro proyecto:
    - se crea window.state.xml
        <frame x="1811" y="143" width="1400" height="768" />
        <layout>
        <window_info content_ui="combo" id="Project" order="0" weight="0.25" />
        <window_info anchor="bottom" id="Version Control" order="0" />
        <window_info anchor="bottom" id="Find" order="1" />
        <window_info anchor="bottom" id="Run" order="2" />
        <window_info anchor="bottom" id="Debug" order="3" weight="0.4" />
        <window_info anchor="bottom" id="Inspection" order="4" weight="0.4" />
        </layout>    
    - se actualiza recentprojects.xml
    - se crea notifications.xml (al desactivar la inspeccion de dockerfile)
        <notification groupId="Docker: Dockerfile detection" displayType="NONE" shouldLog="false" />
"""
