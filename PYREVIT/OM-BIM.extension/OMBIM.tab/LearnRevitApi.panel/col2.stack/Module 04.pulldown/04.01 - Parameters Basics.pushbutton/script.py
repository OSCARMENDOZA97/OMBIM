# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "04.01 - Parameters Overview",
    "en_gb": "04.01 - Parameters Overview",
    "es_es": "04.01 - Parameters Overview"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Code from lesson 04.01 - Parameters Overview
Overview of elements parameters with revit api

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
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *
from Snippets.Converts import  *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
selection = uidoc.Selection

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
# ==================================================
def get_parameter(param):
    "Get value from a parameter based on its Storage Type"
    if param.StorageType == StorageType.Double:
        value_ft = param.AsDouble()
        if param.Definition.Name == 'Área':
            value_ = convert_internal_units(value_ft,get_internal=False, units='m2')
            value = round(value_,2)
        elif param.Definition.Name == 'Volumen' or param.Definition.Name == 'Volume'  :
            value_ = convert_internal_units(value_ft, get_internal=False, units='m3')
            value = round(value_, 2)
        else:
            value_ = convert_internal_units(value_ft, get_internal=False, units='m')
            value = round(value_, 2)
    elif param.StorageType == StorageType.ElementId:
        value = param.AsElementId()
    elif param.StorageType == StorageType.Integer:
        value = param.AsInteger()
    elif param.StorageType == StorageType.String:
        value = param.AsString()
    return value


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

pick_object = selection.PickObject(ObjectType.Element, "Selecciona los elementos")
e_2         = doc.GetElement(pick_object)
parameters  = e_2.Parameters

for p in parameters:
    print ("Nombre: {}".format(p.Definition.Name))
    print ("BuiltInParameter:{}".format(p.Definition.BuiltInParameter))
    print ("ParameterGroup:{}".format(p.Definition.ParameterGroup))
    print ("IsRealOnly:    {}".format(p.IsReadOnly))
    print ("HasValue:      {}".format(p.HasValue))
    print ("IsShared:      {}".format(p.IsShared))
    print ("Value: {}".format(get_parameter(p)))
    print ("AsValueString: {}".format(p.AsValueString()))
    print ("***************************************")



