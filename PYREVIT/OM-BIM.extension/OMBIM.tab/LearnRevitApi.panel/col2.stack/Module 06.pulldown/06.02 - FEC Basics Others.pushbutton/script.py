# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "06.02 FEC basics Others",
    "en_gb": "06.02 FEC basics Others",
    "es_es": "06.02 FEC basics Others"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Lesson 6.2
____________________________________________
Description 
Explore Documentation and learn how to use additional methods in Revit API documentation with real examples
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

### EXTRA: Tú puedes borrar esto
__helpurl__ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
__min_revit_ver__ = 2021
__max_revit_ver__ = 2025

### EXTRAS
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
import os, sys, datetime
from copy_reg import constructor
from logging import Filter
from zipfile import compressor_names

import System

from System.Collections.Generic import List
from Autodesk.Revit.DB import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
active_view = doc.ActiveView

# ╔═╗╔═╗╔╗╔╔═╗╔╦╗╦═╗╦ ╦╔═╗╔╦╗╔═╗╦═╗
# ║  ║ ║║║║╚═╗ ║ ╠╦╝║ ║║   ║ ║ ║╠╦╝
# ╚═╝╚═╝╝╚╝╚═╝ ╩ ╩╚═╚═╝╚═╝ ╩ ╚═╝╩╚═
# ==================================================
# 1. Get visible elements in view

furniture = FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Furniture).WhereElementIsNotElementType().ToElements()

# print('The are {} Furniture Elements in Active view'.format(len(furniture)))

# 2. FilteredElementCollector with a set of elements

selected_elements = uidoc.Selection.GetElementIds()

if selected_elements:
    el_colector = FilteredElementCollector(doc,selected_elements).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#    print('The are {} Walls in Active view'.format(len(el_colector)))

# ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
# ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
# ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
# ==================================================
#---------------------------------------------------------------------------------------------------------------------------------
# 1. Excluding
selected_elements = uidoc.Selection.GetElementIds()

if selected_elements:
    excl_collector = FilteredElementCollector(doc, active_view.Id).Excluding(selected_elements)\
        .WhereElementIsNotElementType().ToElements()
#else:
#    excl_collector = FilteredElementCollector(doc, active_view.Id)\
#        .WhereElementIsNotElementType().ToElements()

#print('There are {} Elements Excluding currect selection in the active View'.format(len(excl_collector)))
#---------------------------------------------------------------------------------------------------------------------------------
# 2. First Element /Element Id

random_wall         = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().FirstElement()
random_wall_type_id = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().FirstElementId()


#print('The wall random is {} \n The random wall type id is {}'.format(random_wall,random_wall_type_id))
#---------------------------------------------------------------------------------------------------------------------------------
# 3. Of Category / Of class

walls       = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements() # este elemento
walls_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElements()

walls_       = FilteredElementCollector(doc).OfClass(Wall).ToElements()
walls_types_ = FilteredElementCollector(doc).OfClass(WallType).ToElements() # ese utilizo para tipos

#print('Cantidad de muros {} \n Cantidad de tipos {}'.format(len(walls),len(walls_types)))
#print('Cantidad de muros 2 {} \n Cantidad de tipos 2 {}'.format(len(walls_),len(walls_types_)))

# 4. OwnedByView: View Specific Elements (Annotations Dimensions, details lines, tags, annotations )

owned_view_collector = FilteredElementCollector(doc).OwnedByView(active_view.Id).ToElements()
#print('Owned by view Elements: {}'.format(len(owned_view_collector)))

#for i in owned_view_collector:
#    print i
#---------------------------------------------------------------------------------------------------------------------------------

# 5. To elements /To elements Ids
floors       = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements() # este elemento
floor_ids = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElementIds()


#6. Union With (Alternative)

walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
floors2 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()

elements = list(walls) + list(floors2)

#6.1 Union With (Alternative2) - Union FilteredELementCollector - Class

# Get Elements
rooms_ = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)
doors  = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)
# Do not use .To elements if you whant to use UnionWith

# Combine
elements = rooms_.UnionWith(doors)
instances = elements.WhereElementIsNotElementType()

# 7 WhereElementsIsCurveDriven (

curve_driven_elements = FilteredElementCollector(doc).WhereElementIsCurveDriven().ToElements()

unique = []

# for el in curve_driven_elements:
#     if type(el) not in unique:
#         unique.append(type(el))
#         print(type(el))


# 8. WhereElementIsViewIndependent (Opposite OwnedByView)

view_independent_elements = FilteredElementCollector(doc).WhereElementIsViewIndependent().ToElements()
unique =[]

# 9 WherePasesMethod (Filter elements)

cats = [BuiltInCategory.OST_Walls,
        BuiltInCategory.OST_Floors,
        BuiltInCategory.OST_Roofs,
        BuiltInCategory.OST_Ceilings]
#ICollection
list_ = List[BuiltInCategory](cats)

#Create filter
multi_cat_filter = ElementMulticategoryFilter(list_)

#ApplyFilter To FEC
combine_collector = FilteredElementCollector(doc).WherePasses(multi_cat_filter).WhereElementIsNotElementType().ToElements()
sorted            = sorted(combine_collector, key=lambda x: str(x))

for i in sorted:
    print(i)


