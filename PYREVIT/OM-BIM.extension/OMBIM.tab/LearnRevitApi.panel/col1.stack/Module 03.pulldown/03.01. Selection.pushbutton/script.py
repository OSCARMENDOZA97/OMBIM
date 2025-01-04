# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.01 - Selection",
    "en_gb": "03.01 - Selection",
    "es_es": "03.01 - Selection"
}  # Nombre de del botón mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 30.06.2024
____________________________________________
Descripción
ID Selection  - Type Name Element 
____________________________________________
Author Oscar Mendoza 
"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.UI.Selection import *

# .NET Importaciones
import clr

clr.AddReference('System')
from System.Collections.Generic import List


# Units Meters Revit API
def mf(meters):
    return meters * 3.28084


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
app = __revit__.Application  # Application class
selection = uidoc.Selection  # type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

#  1.Get Select elements

# select_elements_Ids = uidoc.Selection.GetElementIds()
#
# for e_id in select_elements_Ids:
#     e = doc.GetElement(e_id)
#     print(e, e_id)
#     if type(e) == Room:
#         print("It's a room")
#     elif type(e) == Wall:
#         print("It's a wall")
#     elif type(e) == Floor:
#         print("It's a floor")
#     elif type(e) == FamilyInstance:
#         print("It's a familyInstance")


#  2. Pick Elements by rectangle

# select_elements = selection.PickElementsByRectangle("Selecciona los elementos Osquitar")
# # print(select_elements)  # Todo_junto
# for elem in select_elements:
#     print(elem)

#  3. Pick object

# pick_object = selection.PickObject(ObjectType.Element, "Selecciona los elementos linkeados OWMB")
# e_2 = doc.GetElement(pick_object)
# print(e_2)

#  4. Pick Objects

# ref_pick_objects = selection.PickObjects(ObjectType.Element, "Selecciona los elementos OSCAR")
# picked_objects = [doc.GetElement(ref) for ref in ref_pick_objects]
#
# for el in picked_objects:
#     print(el)

# ALTERNATIVA
# picked_objects = []
# for ref in ref_pick_objects:
#     e = doc.Getelement(ref)
#     picked_objects.append(e)


#  5. Pick Points

# picked_point = selection.PickPoint("Selecciona el punto Oscar")
# print(picked_point, type(picked_point))


#  6.PickBox


#  7. Set Selection
new_selection = List[ElementId]()

new_selection.Add(ElementId(25055))
new_selection.Add(ElementId(25098))
new_selection.Add(ElementId(25260))

selection.SetElementIds(new_selection)

# with Transaction(doc, "Create a Floor") as t:
#     t.Start()
#     new_floor = CreateFloorAtElevation(doc, 1.50)
#     t.Commit()
