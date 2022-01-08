# testing-fastapi
Proyecto para testear vulnerabilidades en imagen docker y librerías 

## Requerimientos:
 - mysql
 - docker
 - python >= 3.8

## Ejecutar con docker 

Cree un archivo ´.env´ que contenga las variables de entorno (CAMBIA VALORES POR VALORES VALIDOS):
```
    ENVIRONMENT=localhost
    X_API_KEY=NEW_APIKEY
    DATABASE=NAME_DB
    DB_HOST=HOST_DB
    DB_USER=USER_DB
    DB_PASSWORD=PASS_DB
    JWT_SECRET=JWT_SECRET
```

Suponiendo que ya ha instalado docker, cree una imagen que contenga la API
```
docker build -t omargc/testing-fastapi-image:image_python_3.9-slim .
```

Crear contenedor dev y correr proyecto
```
docker run -d --env-file ./.env --name testing-fastapi-dev -p 8000:80 omargc/testing-fastapi-image:image_python_3.9-slim
```

Una ves el proyecto se ejecute abrir navegador en la ruta:  
```
http://localhost:8000/docs
```
