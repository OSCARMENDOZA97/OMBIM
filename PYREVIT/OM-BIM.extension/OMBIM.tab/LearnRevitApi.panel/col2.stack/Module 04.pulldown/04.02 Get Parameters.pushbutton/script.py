# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "04.02 Get Parameters",
    "en_gb": "04.02 Get Parameters",
    "es_es": "04.02 Get Parameters"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Code from lesson 04.02 - Get Parameters 
Obtain Parameters with revit api

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

def read_param(p):
    print ("Nombre: {}".format(p.Definition.Name))
    print ("BuiltInParameter:{}".format(p.Definition.BuiltInParameter))
    print ("ParameterGroup:{}".format(p.Definition.ParameterGroup))
    print ("IsRealOnly:    {}".format(p.IsReadOnly))
    print ("HasValue:      {}".format(p.HasValue))
    print ("IsShared:      {}".format(p.IsShared))
    print ("Value: {}".format(get_parameter(p)))
    print ("AsValueString: {}".format(p.AsValueString()))
    print ("***************************************")

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================

pick_object_ = selection.PickObject(ObjectType.Element, "Selecciona los elementos")
pick_object  = doc.GetElement(pick_object_)

# 1️⃣ Get Built-In Parameters (LockUp- Parameters)

comments    = pick_object.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
mark        = pick_object.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
level       = pick_object.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM)
el_type     = pick_object.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM)
area        = pick_object.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED)
heigth_sill = pick_object.get_Parameter(BuiltInParameter.INSTANCE_SILL_HEIGHT_PARAM)

# Metodo LockUpParameter
p_text = pick_object.LookupParameter("OMBIM")
p_text2 = pick_object.LookupParameter("Altura de extremo")


# Read parameters
read_param(comments)
read_param(mark)
read_param(level)
read_param(el_type)
read_param(area)
read_param(heigth_sill)