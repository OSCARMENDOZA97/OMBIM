# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.04.01 Filter doors",
    "en_gb": "03.04.01 Filter doors",
    "es_es": "03.04.01 Filter doors"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 05.09.2024
____________________________________________
Descripción
Tool to Sun Selected Rooms
if not rooms you will asked to select them 
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

# .NET Importaciones
import sys
import clr
clr.AddReference('System')
from System.Collections.Generic import List
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

# Select Doors

filtered_categories = ISelectionFilter_Categories([BuiltInCategory.OST_Doors])
ref_picked_Doors = selection.PickObjects(ObjectType.Element,
                                         filtered_categories,
                                         "Select the wall")
selected_Doors = [doc.GetElement(ref) for ref in ref_picked_Doors]

if not selected_Doors:
    print("There were no Doors selected. Please try Again")
    sys.exit()

new_selection = List[ElementId]()
string_contains = "Tabique"

# Obtain Properties
for door in selected_Doors:
    door_host = door.Host
    host_name = door_host.Name
    host_id = door_host.Id
    door_name = door.Name
    wall_type_name = door_host.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM).AsValueString()
    if string_contains in host_name:
        new_selection.Add(host_id)
    # print('Host: {}'.format(door_host))

# Selection

selection.SetElementIds(new_selection)

