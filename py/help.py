def index():
    print("\n\t --- HELP MENU ---")
    arhelp = []
    arhelp.append("""
    module: deploy
    - hace el deploy de un proyecto en local en prod
       
    ejemplo:
        <prject-id> esta en el config/json
        py.sh <project-id> index deploy
        py.sh deploy tinymarket
        py.sh deploy.composer tinymarket
        py.sh deploy.dbrestore tinymarket
    """)

    arhelp.append("""
    module: dump  
    - mueve datos de la carpeta mapeada del contenedor de sqlyog a un proyecto concreto. 
    - Hay que configurar el diccionario projects (config/projects.local.json)

    ejemplo:
        py.sh dump tinymarket
    """)    

    strhelp = "\n".join(arhelp)
    print(strhelp)


