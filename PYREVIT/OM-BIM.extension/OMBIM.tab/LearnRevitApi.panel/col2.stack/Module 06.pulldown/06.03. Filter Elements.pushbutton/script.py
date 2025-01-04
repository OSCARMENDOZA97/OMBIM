# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "06.03 FilterElements",
    "en_gb": "06.03 FilterElements",
    "es_es": "06.03 FilterElements"
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

### EXTRA: Tu puedes borrar esto
__helpurl__ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
__min_revit_ver__ = 2021
__max_revit_ver__ = 2025

### EXTRAS
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
import os, sys, datetime
from logging import Filter
from operator import truediv

import System

from System.Collections.Generic import List
from Autodesk.Revit.DB import *
from Snippets.Converts import *
# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
active_view = doc.ActiveView


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

# 1️⃣ Filter out unbounded Rooms
all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
all_rooms_bounded = [r for r in all_rooms if r.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble()]
all_rooms_unbounded = [r for r in all_rooms if not r.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble()]

# print('Total rooms : {}'.format(len(all_rooms)))
# print('Total rooms bounded: {}'.format(len(all_rooms_bounded)))
# print('Total rooms unbounded: {}'.format(len(all_rooms_unbounded)))

#--------------------------------------------------------------------------------------------
# 2️⃣ Get walls with 'Tabique' in type name and height of less than 1 meter

#📦 Variables
keyword = "Tabique"
max_height_m = 1
max_height_ft = convert_internal_units(max_height_m, get_internal=True, units = 'm')

# Functions
def check_wall (wall, keyword, max_heigth_ft):
    #type: (Wall, str, float) -> bool
    """ Check if wall's Type Name contains keyword and it's lower than max_height_ft"""
    wall_type_name = wall.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM).AsValueString()
    wall_height_ft = wall.get_Parameter(BuiltInParameter.WALL_USER_HEIGHT_PARAM).AsDouble()
    if keyword in wall_type_name and wall_height_ft < max_heigth_ft:
        return True



# 🎯Main
all_walls_ = FilteredElementCollector(doc).OfClass(Wall).ToElements()
filtered_walls_ = [w for w in all_walls_ if check_wall(w, keyword, max_height_ft)]

# 📄Reports
#print("Total Walls: {}".format(len(all_walls)))
#print('There are {} Walls with "{}" keyword and height lower than {}m'.format(len(filtered_walls),
#                                                                          keyword,
#                                                                          max_height_m ))
#print([e.Id.IntegerValue for e in filtered_walls])

#--------------------------------------------------------------------------------------------

# 3️⃣ Get elements with certain Material used in compound structure [Walls, Floor, Roofs Ceiling]

#📦 Variables
mat_name = "OMBIM"

# 🧬Function
def check_mat(el, mat_name):
    #type (Element, str) -> bool
    """Function to check if given element has a Material in Structure that matches given material name"""
    # Get Type
    el_type_id = el.GetTypeId()
    el_type = doc.GetElement(el_type_id)
    if type(el_type) not in [WallType, FloorType, CeilingType, RoofType]:
        return False
    # Structure
    structure = el_type.GetCompoundStructure()
    if structure:
        # Get & Iterate through layers
        for layers in structure.GetLayers():
            mat_id = layers.MaterialId
            # Ensure material is assigned! ElementId(-1) means no material
            if mat_id != ElementId(-1):
                mat = doc.GetElement(mat_id)
                # Check material Name
                if mat_name.lower() in mat.Name.lower():
                    return True


#🎯Main
# Como se quiere hacer un reporte individual conviene tener los elementos separados

all_walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()
all_floors = FilteredElementCollector(doc).OfClass(Floor).ToElements()
all_ceilings = FilteredElementCollector(doc).OfClass(Ceiling).ToElements()
all_roofs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Roofs)\
                .WhereElementIsNotElementType().ToElements()

all_roofs = [roof for roof in all_roofs if type(roof) != FamilyInstance]

filtered_walls = [el for el in all_walls        if check_mat (el, mat_name)]
filtered_floors = [el for el in all_floors      if check_mat (el, mat_name) ]
filtered_ceilings = [el for el in all_ceilings  if check_mat (el, mat_name) ]
filtered_roofs = [el for el in all_roofs        if check_mat (el, mat_name) ]

# 📄 Report
print('Total {}/{} Walls    found with material Name "{}" in Compound Structure'.format(len(filtered_walls), len(all_walls), mat_name))
print('Total {}/{} Floors   found with material Name "{}" in Compound Structure'.format(len(filtered_floors), len(all_floors), mat_name))
print('Total {}/{} Ceilings found with material Name "{}" in Compound Structure'.format(len(filtered_ceilings), len(all_ceilings), mat_name))
print('Total {}/{} Roofs    found with material Name "{}" in Compound Structure'.format(len(filtered_roofs), len(all_roofs), mat_name))

filtro1 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

print("Hay en total rooms {} en el proyecto".format(len(filtro1)))
print([e.Id.IntegerValue for e in filtro1])


"""
Atajos : 
    Control + D= repetir ultimo texto
    Selección multiple= selección + alt
    Control + J = Seleccionar parecidos
Comentarios:
    1. Para hallar el tipo tiene que hacerse con el metodo GetTypeId si no se tendria que buscar por cada tipo 
    y sería más engorroso
    2. GetCompoundStucture (Wall, roof o Ceiling)
    Realiza una copia de la CompoundStructure pero no modifcia 
"""


