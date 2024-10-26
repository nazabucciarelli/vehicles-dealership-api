# Proyecto de Django

Este es un proyecto de Django diseñado para simular el sitio web de una concesionaria. Este README proporciona instrucciones sobre cómo configurar el entorno y comenzar a trabajar con el proyecto.
Requisitos

    Python 3.11.2

# Configuración del entorno

Seguí los siguientes pasos para configurar el entorno de desarrollo:

### 1. Clona el repositorio
```bash

git clone git@github.com:nazabucciarelli/vehicles-dealership-system.git
cd vehicles-dealership-system
```
### 2. Crea un entorno virtual

Hay que usar un entorno virtual para gestionar las dependencias del proyecto. 
Podes crearlo usando venv.
```bash

python3 -m venv env
```
### 3. Activa el entorno virtual

En Windows:
```bash

.\env\Scripts\activate
```
En macOS y Linux:
```bash

source env/bin/activate
```
### 4. Instala las dependencias

Instala todas las dependencias necesarias desde el archivo requirements.txt.
```bash

pip install -r requirements.txt
```
### 5. Crea las migraciones

Crea las migraciones que posteriormente seran ejecutadas.
```bash

python manage.py makemigrations
```
### 6. Ejecutar migraciones

Ejecuta las migraciones de la base de datos para configurar el esquema.
```bash

python manage.py migrate
```
### 7. Ejecuta el script post-migración

Ejecuta el script necesario después de realizar las migraciones de la base de datos. 
```bash

python manage.py runscript post_migration_script
```

### 8. Crea un superusuario

Crea un superusuario para acceder al panel de administración de Django.
```bash

python manage.py createsuperuser
```
Sigue las instrucciones en pantalla para configurar el superusuario.
### 9. Ejecuta el servidor de desarrollo

Inicia el servidor de desarrollo para asegurarte de que todo está funcionando correctamente.

```bash
python manage.py runserver
```
Accede al servidor en http://127.0.0.1:8000/

### Funcionalidades implementadas

- Login: Los usuarios que previamente se registaron pueden iniciar sesión a través de un formulario para poder acceder a más funcionalidades de la app. Los usuarios no staff y staff usan el mismo formulario para iniciar sesión.
- Registro: Los usuarios visitantes pueden registrarse a través de un formulario. Todos los usuarios registrados mediante dicho formulario, son no staff por defecto. Los usuarios staff se darán de alta mediante la consola.
- Panel de administrador: Los usuarios que estén logeados y sean staff (solo se puede crear un usuario staff utilizando el comando createsuperuser) pueden acceder a la ruta del panel de administrador. En la misma, se puede realizar operaciones CRUD de las distintas entidades relacionadas al negocio concesionario. Como por ejemplo, categorías, tipos de motores, transmisiones, direcciones, etc. Previamente se deben cargar las entidades que componen al vehículo para poder cargar el vehículo deseado en el listado de vehículos disponibles.
- Listado de vehículos: Los usuarios visitantes y registrados staff o no staff pueden listar los vehículos cargados según la categoría. Además, si no se encuentran en ninguna categoría, es decir, estan en "Home", verán todos los vehículos disponibles sin importar la categoría.
- Detalle de vehículo: Al clickear un vehículo, el usuario es dirigido a una vista con la foto ampliada y más información sobre el mismo.
- Comentarios: Luego de acceder al detalle de un vehículo, los usuarios registrados podrán dejar un comentario relacionado al mismo. El usuario no staff puede eliminar o editar sus propios comentarios únicamente, y el usuario staff puede solo eliminar comentarios ajenos o editar los propios.

### Más información

Para más información, contacta a [Nazareno](https://github.com/nazabucciarelli) o [Valentino](https://github.com/valentinoarballo).
