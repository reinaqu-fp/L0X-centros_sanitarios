# -*- coding: utf-8 -*-

import folium

def crea_mapa(latitud, longitud, zoom=9):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    @param latitud: latitud del centro del mapa en pantalla
    @type latitud: float
    @param longitud: longitud del centro del mapa en pantalla
    @type longitud: float
    @param zoom: nivel del zoom con el que se muestra el mapa 
    @type zoom:int
    @return: objeto mapa creado
    @rtype: folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa

def crea_marcador (latitud, longitud, etiqueta):
    '''
    Función que crea un marcador rojo con un icono de tipo señal de información.
    El marcador se mostrará en el punto del mapa dado por la latitud y longitud
    y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    @param latitud: latitud del marcador 
    @type latitud: float
    @param longitud: longitud del marcador
    @type longitud: float
    @param etiqueta: texto de la etiqueta que se asociará al marcador 
    @type etiqueta: str
    @return: objeto marcador creado 
    @rtype: folium.Marker
    '''
    marcador = folium.Marker([latitud,longitud], 
                   popup=etiqueta, 
                   icon=folium.Icon(color='red', icon='info-sign')) 
    return marcador
