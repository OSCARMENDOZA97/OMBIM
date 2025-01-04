# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "FEC Wall Collect",
    "en_gb": "FEC Wall Collect",
    "es_es": "FEC Wall Collect"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Esto es un archivo de plantilla para Pyrevit Scripts
____________________________________________
Acciones:
- Revisar que la versión sea en 2021
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================

import clr
from Snippets.Converts import *

clr.AddReference('System')
from System.Collections.Generic import List

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document

cl = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)  # Hasta acá hemos creado una instancia

# for el in cl: # Iteramos
#    print(el)

"""
1. Pero si te das cuenta hasta ahi hemos imprento como 20 tipos
Nota : Siempre probar todos los element collector por que siempre se debe ver los elementos que se obtiene

2. Para solucionarlo buscamos en los metodos para excluir los tipos (Oh WhereElementIsNotType) entonces eso lo agregamos 
a nuestra intancia
"""

# Collecionar elementos
wall_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).\
    WhereElementIsNotElementType().\
    ToElements()
vol_m3 = 0
count = 0
for i in wall_collector:
    param_volume = i.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)
    if param_volume and param_volume.AsDouble():
        count +=1
        volume = param_volume.AsDouble()
        volume_m3 = convert_internal_units(volume, get_internal=False, units='m3')
        rounded_area = round(volume_m3, 2)
        print(rounded_area)
        vol_m3 += rounded_area

print("El volumen total es {}".format(vol_m3))
# print i.LookupParameter('Volume')  # esto te devuelve el elemento propiedad
# print(p.Definition.Name)  # Saca el nombre del parametro


# En caso no se tenga to elements:
# for i in wall_collector:
#    print(i)
# Ok es lo que queria esta imprimiendose solo los muros solicitados

print("La cantidad de muros en el modelo es {}".format(count))


