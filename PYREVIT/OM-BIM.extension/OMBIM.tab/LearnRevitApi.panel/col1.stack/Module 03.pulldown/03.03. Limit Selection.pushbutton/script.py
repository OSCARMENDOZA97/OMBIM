# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.03 Limit Selection",
    "en_gb": "03.03 Limit Selection",
    "es_es": "03.03 Limit Selection"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Example IselectionFilter limit Selection Element
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

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

clr.AddReference('System')

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument

selection = uidoc.Selection  # type:Selection


# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝

# Get Selected  elements

# selected_elements_ids = selection.GetElementIds()
#
# for e_id in selected_element_ids:
#   e = doc.GetElement(e_id)
#   print(e_id,e)
#
# if type(e) == Room
#   print("It's a room!")
# elif wall type(e) == Wall
#   print(it's a room)"


#  --- FILTER CLASSES OR ONE CLASS ---

# filtered_classes = IselectionFilterClasses([Floor, FamilyInstance])
# ref_picked_objets = selection.PickElementsByRectangle(filtered_classes,
#                                                    "Seleciona los suelos osquitar")
# for elem in select_elements:
#    print(elem)


#  --- FILTER CATEGORIES OR ONE CATEGORIES ---

filtered_categories = ISelectionFilter_Categories([BuiltInCategory.OST_StructuralColumns,
                                                   BuiltInCategory.OST_Rooms])
select_elements = selection.PickObjects(ObjectType.Element,
                                        filtered_categories,
                                        "Selecciona los elementos OWMB")

el = [doc.GetElement(elem) for elem in select_elements]
# print(el)


# --- BONUS WALL EXCERCISE I  ---

class WallSelectionFilter(ISelectionFilter):
    def AllowElement(self, element):
        if type(element) == Wall:
            # Get Type Name
            type_name = element.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM).AsValueString()
            # Get Height
            height_ft = element.get_Parameter(BuiltInParameter.WALL_USER_HEIGHT_PARAM).AsDouble()
            heigth_m = convert_internal_units(height_ft, get_internal=False, unit='m')

            # Check height and type name
            if 1 <= heigth_m <= 5 and 'MURO1' in type_name:
                return True


# ref_wall = uidoc.Selection.PickObjects(ObjectType.Element,
#                                       WallSelectionFilter(),
#                                       "Seleccionar el muro")
# el = [doc.GetElement(elem) for elem in ref_wall]
# for elem in el:
#    print(elem)


# -- BONUS ROOM AREA EXCERCISE I ---
class RoomSelectionFilter(ISelectionFilter):
    def AllowElement(self, element):
        if element.Category.BuiltInCategory == BuiltInCategory.OST_Rooms:
            # Get Height
            area_ft2 = element.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble()
            area_m2 = convert_internal_units(area_ft2, get_internal=False, unit='m2')
            # Check area
            if area_m2 > 15:
                return True


#ref_rooms = uidoc.Selection.PickObjects(ObjectType.Element,
#                                        RoomSelectionFilter(),
#                                        "Seleccionar el room")
# Obtain elements
#el = [doc.GetElement(elem) for elem in ref_rooms]

# Obtain Names
#habitaciones = [elem.get_Parameter(BuiltInParameter.ROOM_NAME).AsValueString() for elem in el]

# Obtains area
#areaft2 = [elem.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble() for elem in el]
#area_m2 = [str(convert_internal_units(area, get_internal=False, unit='m2')) for area in areaft2]  # List

# Print names and area
#print("-- Names: Areas -- \n -- Filter for rooms larger than 15 m2-")
#for habitacion, area in zip(habitaciones, area_m2):
#    print("{}: {:.2f} m2".format(habitacion, area))  # 2 decimals

print("hola mundo{}".format(el))