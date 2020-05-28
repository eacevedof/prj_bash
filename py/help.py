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
        py.sh deploy.composer tinymarket
        py.sh deploy.dbrestore tinymarket
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

    #arhelp.append("""
    #module: get-pip  
    #- Ni idea porque está ahi ^^ cosas de la vida :)
    #ejemplo:
    #    py.sh dump tinymarket
    #""")    

    strhelp = "\n".join(arhelp)
    print(strhelp)
    print("\n\t --- END HELP MENU ---")
