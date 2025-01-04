# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.04 Sum Rooms",
    "en_gb": "03.04 Sum Rooms",
    "es_es": "03.04 Sum Rooms"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 05.09.2024
____________________________________________
Descripción
Tool to Sun Selected Rooms
if not rooms you will asked to select them 
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

"""
Obtains Summary rooms
1. Get Rooms
2. Get Name y Area
3. Display Results
"""
# .NET Importaciones
import sys
import clr
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from select import select
from Snippets.Selection import *
from Snippets.Converts import *
from Autodesk.Revit.DB.Architecture import Room
from collections import defaultdict

clr.AddReference('System')

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument

selection = uidoc.Selection  # type:Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ================================================

# Select elements
selected_elements = [doc.GetElement(e_id) for e_id in selection.GetElementIds()]
selected_rooms = [elem for elem in selected_elements if type(elem) == Room]

# Not select elements
if not selected_rooms:
    filtered_classes = ISelectionFilter_Classes([Room])
    selected_rooms_ref = selection.PickObjects(ObjectType.Element,
                                               filtered_classes,
                                               "Select the elements OWMB")
    selected_rooms = [doc.GetElement(elem) for elem in selected_rooms_ref]

# Not select nothing
if not selected_rooms:
    print("There were no Rooms selected. Please try Again")
    sys.exit()

counts = defaultdict(int)

for room in selected_rooms:
    level = doc.GetElement(room.LevelId)  # Devuelve un objeto Element Id
    room_level_Name = level.Name
    counts[room_level_Name] += 1  # Dictionary

for k, v in counts.items():
    print('Level "{}" has {} Rooms'.format(k, v))
