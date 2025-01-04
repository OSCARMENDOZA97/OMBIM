# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.02- Read Properties",
    "en_gb": "03.02- Read Properties",
    "es_es": "03.02- Read Properties"
}  # Nombre de del botón mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 30.06.2024
____________________________________________
Descripción
Examples of Python - Read properties elements
____________________________________________
Author Oscar Mendoza 
"""
# .NET Importaciones
import clr
import sys

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================

from Autodesk.Revit.DB.Architecture import Room
from Snippets.Selection import *
from Snippets.Converts import *

clr.AddReference('System')
from System.Collections.Generic import List

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
selection = uidoc.Selection  # type: Selection
# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

pick_object = selection.PickObject(ObjectType.Element, "Selecciona los elementos Osquitar")
elem = doc.GetElement(pick_object)

# Check
if type(elem) != Room:
    print("Esto no es una habitación. Intenta de nuevo")
    sys.exit()
print(elem)

# Room Variables
level_id = elem.LevelId
level = doc.GetElement(level_id).Name
group = "None" if elem.GroupId == ElementId(-1) else elem.GroupId

# Print statement
print('### Element Properties ## ')
print('ElementId: {}'.format(elem.Id))
print(type(elem.GroupId))
print('GroupId:{}'.format(group))
print('Document:{}.rvt'.format(doc.Title))  # Titulo Documento
print("Category:{}/n Category Name:{}".format(elem.Category, elem.Category.Name))
print("BuiltInCategory: {}".format(elem.Category.BuiltInCategory))
print('El nombre de nivel del room es: {}'.format(level))
print("Nombre:{}".format(Element.Name.GetValue(elem)))  # Name no valido en tipos rooms
print('Unique Id:{}')
print('### SpatialElements Properties REVIT API UNITS Feets ###')  # Revit API uses feet as internal units
print("X:{}, Y:{}, Z:{}".format(elem.Location.Point.X, elem.Location.Point.Y, elem.Location.Point.Z))
print("Area:{}".format(elem.Area))
print("Number:{}".format(elem.Number))
print("Perimeter:{}".format(elem.Perimeter))


# x = convert_internal_units() # control +q

print('### SpatialElements Properties REVIT API UNITS meters ###')
perimeter_m = convert_internal_units(elem.Perimeter, get_internal=False)
area_m = convert_internal_units(elem.Area, get_internal=False, unit='m2')
print('El perimetro es:{}'.format(perimeter_m))
print('El area es: {}'.format(area_m))
