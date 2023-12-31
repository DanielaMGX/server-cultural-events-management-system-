# **server-cultural-events-management-system-

_API REST en Python con FastAPI, Postgresql, TortoiseORM, como el servidor en el proyecto servicios culturales de Integrador I 2023-1_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_se necesita  Docker_

_Docker_:

En Ubuntu:

https://www.hostinger.co/tutoriales/como-instalar-y-usar-docker-en-ubuntu/

En Windows y Mac:

https://platzi.com/tutoriales/2066-docker/1779-como-instalar-docker-en-windows-y-mac/


_Postgresql_:

En Ubuntu:

https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es

En Windows:

https://www.solvetic.com/tutoriales/article/7676-como-instalar-postgresql-en-windows-10/

En Mac:

https://programadorwebvalencia.com/instalar-postgresql-en-osx/


### Instalación 🔧

_Una vez instalados Docker y Postgresql se abre una terminal dentro de la 
ruta del proyecto y se ejecuta el siguiente comando_

En Ubuntu:
primero se debe crear la network:
```
 sudo docker network create aplicativo
```
luego el volumen:
```
sudo docker volume create aplicativo-db
```

```
sudo docker-compose -f docker/Docker-compose.dev.yml build
```

Luego:


```
sudo docker-compose -f docker/Docker-compose.dev.yml up

```


En Windows (Con permisos de administrador):
primero se debe crear la network:
```
 docker network create aplicativo
```
luego el volumen:
```
docker volume create aplicativo-db


```
sudo docker-compose -f docker/Docker-compose.dev.yml build
```

Luego:


```
sudo docker-compose -f docker/Docker-compose.dev.yml up

```


Una vez ejecutados ambos comandos, la API queda ejecutándose en el puerto 8007 por defecto y lista para recibir las peticiones


Para acceder a la API:
localhost:8007


Para acceder a la documentación interactiva:
localhost:8002/docs



## Construido con 🛠️


* [FastAPI](https://fastapi.tiangolo.com/es/) - El framework web usado
* [Docker](https://www.docker.com) - Despliegue


## Autores ✒️


* **Laura Daniela Monsalve Gómez** - [danielamgx](https://github.com/DanielaMGX)


## Licencia 📄

Este proyecto está bajo la Licencia MIT license - mira el archivo [LICENSE.md](LICENSE) para detalles
