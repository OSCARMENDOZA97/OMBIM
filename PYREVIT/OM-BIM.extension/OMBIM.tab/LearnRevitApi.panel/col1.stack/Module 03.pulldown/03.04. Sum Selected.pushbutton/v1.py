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
selected_rooms = [element for element in selected_elements if type(element) == Room]

# Not select elements
if not selected_rooms:
    filtered_classes = ISelectionFilter_Classes([Room])
    ref_picked_rooms = selection.PickObjects(ObjectType.Element,
                                             filtered_classes,
                                             "Seleciona los rooms osquitar")
    selected_rooms = [doc.GetElement(ref) for ref in ref_picked_rooms]

if not selected_rooms:
    print("There were no Rooms selected. Please try Again")
    sys.exit()

# GET VALUES
area_m2 = [convert_internal_units(elem.Area, get_internal=False, unit='m2') for elem in selected_rooms]
names = [elem.get_Parameter(BuiltInParameter.ROOM_NAME).AsValueString() for elem in selected_rooms]
sum_area = sum(area_m2)
print("--Names: Areas---")
for name, area in zip(names, area_m2):
    print("{}: {:.2f} m2".format(name, float(area)))
print("La suma de las areas de los rooms seleccionados: {:.2f} m2".format(float(sum_area)))