CyberSecurity
=============

Para ejecutar el proyecto debemos tener instalado Docker:

```bash
# Clonar repositorio
git clone https://github.com/palpico/CyberSecurity.git
# Bring server up
docker-compose.exe -f local.yml up
#Create login user
docker-compose.exe -f local.yml run --rm django python manage.py makemigrations
#Create login user
docker-compose.exe -f local.yml run --rm django python manage.py migrate
#Create login user
docker-compose.exe -f local.yml run --rm django python manage.py createsuperuser
```
Una vez inicializado se puede ingresar al navegador a: http://localhost:8000/

##Tema 1 - Estadísticas de Twitter 

Se creo un notebook: [Notebook](https://github.com/palpico/CyberSecurity/blob/master/notebooks/EstadisticasTwitter.ipynb)

##Tema 2 - SQL 

Se crearon los procesos almacenado para Postgres: [SQL](https://github.com/palpico/CyberSecurity/blob/master/sql/StoredProcedures.sql) 

*en caso de querer informacion de prueba se puede encontrar inserts en: 

##Tema 3 - API REST 

###•	Asumir que la mayoría de la información es sensible.
Solo usuarios verificados pueden acceder
###•	Se espera que los endpoints del API estén bajo protección.
Solo usuarios verificados pueden acceder
###•	El servidor debería ser resistente a ataques informáticos como DOS.
Solo usuarios verificados pueden acceder, se establece un contador para bloquear al usuario temporalmente.
###•	El despliegue será remoto, factor que deberás tener en cuenta al instaurar un proceso que garantice la seguridad en el momento de acceso.
Para un facil despliegue remoto se usa tegnologia de contenedores.

#### A continuacion la descripcion del rest:
El codigo para el rest esta en: [API](https://github.com/palpico/CyberSecurity/tree/master/cybersecurity/tema3/api)

| Resource          | GET                                   | POST | PUT | DELETE |
| ----------------- | ------------------------------------- | ---- | --- | ------ |
| /day/{'pet'}      | returns string (day) for specific pet | X    | X   | X      |
| /day/             | returns string (day) for all pets     | X    | X   | X      |
| /positive/{'pet'} | returns count for specific pet        | X    | X   | X      |
| /positive/        | returns count for all pets            | X    | X   | X      |
| /negative/{'pet'} | returns count for specific pet        | X    | X   | X      |
| /negative/        | returns count for all pets            | X    | X   | X      |
| /neutral/{'pet'}  | returns count for specific pet        | X    | X   | X      |
| /neutral/         | returns count for all pets            | X    | X   | X      |
| /hashtags/{'pet'} | return list with specific pet         | X    | X   | X      |
| /hashtags/        | return list for all pet               | X    | X   | X      |

##Tema 4 - Arquitecturas de Seguridad 

###- Tema 1

| Sugerencia | Problema             | solucion                                                                        |
| ---------- | -------------------- | ------------------------------------------------------------------------------- |
| 1          | Acceso no autorizado | Limitar el tipo de acceso, usar solo acceso de lectura en casos de mineria, etc |
| 2          | Filtracion           | Almacenar informacion sensitiva encriptada                                      |
| 3          | DDOS                 | Limitar la cantidad de respuestas, CDN                                          |

###- Tema 2

| Sugerencia | Problema                            | solucion                                            |
| ---------- | ----------------------------------- | --------------------------------------------------- |
| 1          | Inyeccion SQL                       | Parametrizar de argumentos de procesos almacenados. |
| 2          | Acceso indebido                     | DCL, limitar el uso de sql en el codigo, usar ORM   |
| 3          | Modificaciones no autorizadas al DB | DCL, limitar el uso de sql en el codigo, usar ORM   |

###- Tema 3

| Sugerencia | Problema                                            | solucion                                                                              |
| ---------- | --------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1          | Filtracion de credenciales en repositorio de codigo | Usar variables de entorno o archivos de configuracion que no esten en el repositorio. |
| 2          | Acceso no autoriado                                 | Sistema de autenticacion.                                                             |
| 3          | Filtrado informacion del sistema                    | Mostrar mensajes de error genericos. Manejo de errores.                               |

