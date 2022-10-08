# L0X-Centros Sanitarios

AUTORA: Toñi Reina

REVISOR: Mariano González

En este proyecto trabajaremos con datos proporcionados por la diputación de Cádiz de centros sanitarios de los municipios con población inferior a 50.000 habitantes de dicha provincia. Los datos los representaremos con mediante listas de tuplas. Implementaremos una serie de funciones que nos permitirán mostrar gráficas de evolución de la población, así como comparar la población en distintos países.

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **centros.py**: Contiene funciones para explotar los datos de los centros sanitarios.
    * **centros_test.py**: Contiene funciones de test para probar las funciones del módulo `centros.py`. En este módulo está el main.
    * **coordenadas.py**: Contiene funciones para trabajar con el tipo Coordenada.
    * **coordenadas_test.py**: Contiene funciones de test para probar las funciones del módulo `coordenadas.py`.
    * **mapas.py**: Contiene funciones para crear un mapa y representar puntos en él. Requiere tener instalada la librería folium.
* **/data**: Contiene el dataset o datasets del proyecto
    * **centrosSanitarios.csv**: Archivo con los datos de población de diversos paises o agrupaciones de paises en distintos años.
* **/doc**: Contiene archivos con documentación acerca del proyecto.
    * **Enunciado.pdf**: Archivo con el enunciado del laboratorio.

## Dependencias
En este ejercicio vamos a trabajar con mapas, para lo que usaremos la librería folium . Para instalar la librería folium abra una ventana de comandos de Anaconda (Anaconda Prompt) y ejecute el siguiente comando:
```
conda install –c conda-forge folium
```

## Funciones a implementar:
Lee el enunciado del proyecto situado en la carpeta doc para tener más detalles de los requisitos que deben cumplir las funciones a implementar.

### Módulo coordenadas

* **calcular_distancia**: recibe dos coordenadas de tipo Coordenada(float, float) y devuelve un float que representa la distancia euclídea entre esas dos coordenadas.
* **calcular_media_coordenadas**: recibe una lista de Coordenada(float, float) y devuelve una Coordenada(float, float) cuya latitud es la media de las latitudes de la lista y cuya longitud es la media de las longitudes de la lista.

### Módulo centros

*	**leer_centros**: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo CentroSanitario(str, str, Coordenada(float, float), str, int, bool, bool) conteniendo todos los datos almacenados en el fichero. 
*	**calcular_total_camas_centros_accesibles**: recibe una lista de tuplas de tipo CentroSanitario y produce como salida un entero correspondiente al número total de camas de los centros sanitarios accesibles para discapacitados.
* **obtener_centros_con_uci_cercanos_a**: recibe una lista de tuplas de tipo CentroSanitario; una tupla de tipo Coordenada, que representa un punto; y un float, que representa un umbral de distancia. Produce como salida una lista de tuplas (str, str, Coordenada(float, float)) con el nombre, del centro, la localidad y la coordenada de los centros situados a una distancia de la coordenada dada como parámetro menor o igual que el umbral dado. Observe la Figura 3 para entender mejor el resultado de la función.
* **generar_mapa**: recibe una lista de tuplas (str, str, Coordenada(float, float)) con el nombre, del centro, la localidad y la coordenada de centros; y un una cadena, que representa la ruta de un fichero html, que se generará con los centros geolocalizados. 
