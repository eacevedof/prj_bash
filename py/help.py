def index():
    print("\n\t --- HELP MENU ---")
    arhelp = []
    arhelp.append("""
    module: deploy
    - hace el deploy de un proyecto en local en prod
       
    ejemplo:
        <prject-id> esta en el config/json
        py.sh deploy.<function> <project-id>
        
        py.sh deploy tinymarket
        py.sh deploy.frontbuild tinymarket
        py.sh deploy.frontbuildembed tinymarket  #solo los assets
        py.sh deploy.composer tinymarket    #solo capreta vendor
        py.sh deploy.dbrestore tinymarket
        py.sh deploy.pictures tinymarket

        py.sh deploy.backend tinymarket #gitpull, composer, dbstore
        py.sh deploy.codeonly tinymarket #gitpull
    """)

    arhelp.append("""
    module: dump  
    - mueve datos de la carpeta mapeada del contenedor de sqlyog a un proyecto concreto. 
    - Hay que configurar el diccionario projects (config/projects.local.json)
    - copia en: https://trello.com/c/ULyscnT8/1-config-deploy
    ejemplo:
        py.sh dump tinymarket
    """)  

    arhelp.append("""
    module: react  
    - hace el despliegue del build dentro de unas rutas locales
    - para esto se necesita el archivo .pysh configurado de esta forma:
        PATH_BUILD=/Users/ioedu/projects/prj_doblerr/frontend_react/pannel/build
        PATH_INDEX_TWIG=/Users/ioedu/projects/prj_doblerr/backend_web/templates/restrict/restrict-react.html.twig
        PATH_PUBLIC=/Users/ioedu/projects/prj_doblerr/backend_web/public/react%

    ejemplo:
        py.sh react "/Users/ioedu/projects/prj_doblerr/frontend_react/pannel/.pysh"
    """)  

    arhelp.append("""
    module: udemy  
    - Crea un indice acorde con tags de README.md
    - Se necesita un archivo de origen con el contenido. Este contenido es un copy/pasete del indice del curso de Udemy
    - Generará un archivo .bk
    
    ejemplo:
        py.sh udemy "/Users/ioedu/Desktop/temp.php"
    """)      

    arhelp.append("""
    module: fromserver
    - Recupera algun recurso del servidor
    - Por el momento solo un backup de la bd
    - Todo se hace con config/projects.json

    ejemplo:
        py.sh fromserver.database tinymarket
    """)          

    arhelp.append("""
    module: doctrine
    - Limpia las entidades autogeneradas con doctrine usando el comando:
        php bin/console --env=local doctrine:mapping:import "App\Entity" annotation --path=src/Entity --filter="AppPromotion"
    - Generará un fichero .clean
    
    ejemplo:
        py.sh doctrine <path-entities>
        py.sh doctrine "$HOME/projects/prj_doblerr/backend_web/src/Entity"
    """)

    arhelp.append("""
    module: images
    - Hace tratamiento de imagenes
    - reduce:
        Hace una reducción en resolución a 150 x 150 ppp en la misma carpeta
    
    ejemplo:
        py.sh images.reducedpi <path-folder-images> <dpi=100 default>
        py.sh images.reducedpi $PWD 150
        py.sh images.reducedpi /Users/ioedu/Downloads/ech-nuevas 150
    """)   
    
    arhelp.append("""
    module: phpstorm
    - Resetea phpstorm para evitar bug de ventanas bailando
    - reduce:
        A veces se solapan las ventanas y si deseas seleccionar alguna no puedes porque salta a la otra y a la inversa ^^
    
    ejemplo:
        py.sh phpstorm <sudo-password>
    """)       
    #arhelp.append("""
    #module: get-pip  
    #- Ni idea porque está ahi ^^ cosas de la vida :)
    #ejemplo:
    #    py.sh dump tinymarket
    #""")    

    strhelp = "\n".join(arhelp)
    print(strhelp)
    print("\n\t --- END HELP MENU ---")
