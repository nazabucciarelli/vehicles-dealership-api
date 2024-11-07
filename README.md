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

### 9. Instalar 'gettext' si no lo tienes en tu sistema operativo

Correr el siguiente comando en la terminal.

```bash
sudo apt-get install gettext
```

### 10. Compila las traducciones

Compila las traducciones.

```bash
django-admin compilemessages
```

### 11. Ejecuta el servidor de desarrollo

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

# Documentacion de Vehicles Dealership System API

### Usuarios

- **Agregar cliente via API**:  
  `POST /api/users/`  
  Agrega un nuevo cliente. Requiere permisos de staff.

- **Obtener clientes via API**:  
  `GET /api/users/`  
  Obtener clientes. No requiere permisos de staff.

- **Iniciar sesion via API**:  
  `POST /api/login/`  
  Iniciar sesion mandando username y password.

### Vehículos

- **Listar vehículos paginados**:  
  `GET /`  
  Devuelve una lista paginada de todos los vehículos.

- **Listar vehículos via API**:  
  `GET /api/vehicles/`  
  Devuelve una lista de todos los vehículos. No requiere permisos de staff.

- **Listar vehículos**:  
  `GET /vehicles/`  
  Devuelve una lista de todos los vehículos. Requiere permisos de staff.

- **Detalles de un vehículo**:  
  `GET /vehicle/<int:id>/`  
  Devuelve los detalles de un vehículo específico.

- **Agregar vehículo**:  
  `POST /vehicles/add/`  
  Agrega un nuevo vehículo. Requiere permisos de staff.

- **Editar vehículo**:  
  `PUT /vehicles/edit/<int:vehicle_id>/`  
  Edita los detalles de un vehículo específico. Requiere permisos de staff.

- **Eliminar vehículo**:  
  `DELETE /vehicles/delete/<int:vehicle_id>/`  
  Elimina un vehículo específico. Requiere permisos de staff.

### Marcas

- **Listar marcas via API**:  
  `GET /api/brands`  
  Devuelve una lista de todas las marcas, pero via API. NO requiere permisos de staff.

- **Listar marcas**:  
  `GET /brands/`  
  Devuelve una lista de todas las marcas. Requiere permisos de staff.

  - **Agregar marca via API**:  
  `POST /api/brands/`  
  Agrega una nueva marca, pero via API. Requiere permisos de staff.

- **Agregar marca**:  
  `POST /brands/add/`  
  Agrega una nueva marca. Requiere permisos de staff.

- **Editar marca**:  
  `PUT /brands/edit/<int:brand_id>/`  
  Edita los detalles de una marca específica. Requiere permisos de staff.

- **Eliminar marca**:  
  `DELETE /brands/delete/<int:brand_id>/`  
  Elimina una marca específica. Requiere permisos de staff.

### Modelos

- **Listar modelos**:  
  `GET /models/`  
  Devuelve una lista de todos los modelos. Requiere permisos de staff.

- **Agregar modelo**:  
  `POST /models/add/`  
  Agrega un nuevo modelo. Requiere permisos de staff.

- **Editar modelo**:  
  `PUT /models/edit/<int:model_id>/`  
  Edita los detalles de un modelo específico. Requiere permisos de staff.

- **Eliminar modelo**:  
  `DELETE /models/delete/<int:model_id>/`  
  Elimina un modelo específico. Requiere permisos de staff.

### Tipos de Motor

- **Listar tipos de motor**:  
  `GET /engine_types/`  
  Devuelve una lista de todos los tipos de motor. Requiere permisos de staff.

- **Agregar tipo de motor**:  
  `POST /engine_types/add/`  
  Agrega un nuevo tipo de motor. Requiere permisos de staff.

- **Editar tipo de motor**:  
  `PUT /engine_types/edit/<int:engine_type_id>/`  
  Edita los detalles de un tipo de motor específico. Requiere permisos de staff.

- **Eliminar tipo de motor**:  
  `DELETE /engine_types/delete/<int:engine_type_id>/`  
  Elimina un tipo de motor específico. Requiere permisos de staff.

### Transmisiones

- **Listar transmisiones**:  
  `GET /transmissions/`  
  Devuelve una lista de todas las transmisiones. Requiere permisos de staff.

- **Agregar transmisión**:  
  `POST /transmissions/add/`  
  Agrega una nueva transmisión. Requiere permisos de staff.

- **Editar transmisión**:  
  `PUT /transmissions/edit/<int:transmission_id>/`  
  Edita los detalles de una transmisión específica. Requiere permisos de staff.

- **Eliminar transmisión**:  
  `DELETE /transmissions/delete/<int:transmission_id>/`  
  Elimina una transmisión específica. Requiere permisos de staff.

### Controles de Tracción

- **Listar controles de tracción**:  
  `GET /traction_controls/`  
  Devuelve una lista de todos los controles de tracción. Requiere permisos de staff.

- **Agregar control de tracción**:  
  `POST /traction_controls/add/`  
  Agrega un nuevo control de tracción. Requiere permisos de staff.

- **Editar control de tracción**:  
  `PUT /traction_controls/edit/<int:traction_control_id>/`  
  Edita los detalles de un control de tracción específico. Requiere permisos de staff.

- **Eliminar control de tracción**:  
  `DELETE /traction_controls/delete/<int:traction_control_id>/`  
  Elimina un control de tracción específico. Requiere permisos de staff.

### Tipos de Carrocería de Vehículos

- **Listar tipos de carrocería**:  
  `GET /vehicle_body_types/`  
  Devuelve una lista de todos los tipos de carrocería de vehículos. Requiere permisos de staff.

- **Agregar tipo de carrocería**:  
  `POST /vehicle_body_types/add/`  
  Agrega un nuevo tipo de carrocería. Requiere permisos de staff.

- **Editar tipo de carrocería**:  
  `PUT /vehicle_body_types/edit/<int:vehicle_body_type_id>/`  
  Edita los detalles de un tipo de carrocería específico. Requiere permisos de staff.

- **Eliminar tipo de carrocería**:  
  `DELETE /vehicle_body_types/delete/<int:vehicle_body_type_id>/`  
  Elimina un tipo de carrocería específico. Requiere permisos de staff.

### Dirección

- **Listar direcciones**:  
  `GET /steerings/`  
  Devuelve una lista de todas las direcciones. Requiere permisos de staff.

- **Agregar dirección**:  
  `POST /steerings/add/`  
  Agrega una nueva dirección. Requiere permisos de staff.

- **Editar dirección**:  
  `PUT /steerings/edit/<int:steering_id>/`  
  Edita los detalles de una dirección específica. Requiere permisos de staff.

- **Eliminar dirección**:  
  `DELETE /steerings/delete/<int:steering_id>/`  
  Elimina una dirección específica. Requiere permisos de staff.

### Categorías

- **Listar categorías**:  
  `GET /categories/`  
  Devuelve una lista de todas las categorías. Requiere permisos de staff.

- **Agregar categoría**:  
  `POST /categories/add/`  
  Agrega una nueva categoría. Requiere permisos de staff.

- **Editar categoría**:  
  `PUT /categories/edit/<int:category_id>/`  
  Edita los detalles de una categoría específica. Requiere permisos de staff.

- **Eliminar categoría**:  
  `DELETE /categories/delete/<int:category_id>/`  
  Elimina una categoría específica. Requiere permisos de staff.

### Comentarios

- **Agregar comentario**:  
  `POST /add_commentary/`  
  Agrega un nuevo comentario sobre un vehículo.

- **Editar comentario**:  
  `PUT /edit_commentary/<int:commentary_id>/`  
  Edita un comentario específico. Requiere que el usuario sea el propietario del comentario.

- **Eliminar comentario**:  
  `DELETE /delete_commentary/<int:commentary_id>/`  
  Elimina un comentario específico. Requiere que el usuario sea el propietario o miembro del personal.

- **Obtener comentarios via API**:  
  `GET /api/comments/<int:vehicle_id>/`  
  Obtener comentarios sobre un vehículo.
