# FusionAI
![](https://i.imgur.com/roUPorE.png)
Sitio que trata sobre Inteligencia Artificial en Español. 

## Descrición

La idea inicial para FusionAI era ser un sitio que abarcara diferentes tipos de contenidos relacionados al mundo de la IA en su idioma original, sin embargo se decidió cambiar el rumbo para que el contenido esté traducido en español, el porque de esto se debe a que no hay tantos recursos como si en el idioma inglés.

Mas allá de la idea general del proyecto, también quería practicar y probar nuevas formas de realizar una aplicación utilizando Docker y Django. También quería utilizar nuevas formas de crear y gestionar usuarios, por ejemplo enviar códigos vía email para activar usuarios.


## Getting Started

### Dependencias

* Docker

### Descarga
```
$ git clone https://github.com/diegovasconcelo/FusionAI.git
```

### Configuración
* Configurar el archivo secret.json.sample. Contiene datos para el funcionamiento del proyecto.
    * Borrar la extensión .sample del archivo secret.json.sample quedaría de la siguiente manera:
        * secret.json
    * Configurar este archivo con los valores correspondiente a la app y a los datos de su proveedor smtp.

### Ejecutar el programa

```
$ docker-compose up
$ docker-compose run web_fai python manage.py makemigrations
$ docker-compose run web_fai python manage.py migrate
$ docker-compose run web_fai python manage.py createsuperuser
```
Luego, desde el administrador de Django insertar un registro para "HomePage", Indicando el título, la descripción, etc.


## Nota

Si existen problemas a la hora de ejecutar Docker puede ser debido a mi poca experiencia utilizando esta técnología. 


## Licencia
MIT.

