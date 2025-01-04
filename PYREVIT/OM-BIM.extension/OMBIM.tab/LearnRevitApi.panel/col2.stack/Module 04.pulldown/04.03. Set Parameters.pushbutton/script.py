# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "04.03 Set Parameters",
    "en_gb": "04.03 Set Parameters",
    "es_es": "04.03 Set Parameters"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Code from lesson 04.03 - set Parameters 
Set Parameters with revit api

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
__title__ = "OM"

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
top_offset  = pick_object.get_Parameter(BuiltInParameter.WALL_TOP_OFFSET)
b_offset    = pick_object.get_Parameter(BuiltInParameter.WALL_BASE_OFFSET)
# Metodo LockUpParameter
p_text     = pick_object.LookupParameter("OMBIM")
p_text2    = pick_object.LookupParameter("Altura de extremo")
s_material = pick_object.LookupParameter("")
s_area     = pick_object.LookupParameter("om_area")
s_number   = pick_object.LookupParameter("om_number")
s_boolean  = pick_object.LookupParameter("om_boolean")

top_offset_    = convert_internal_units(-3.00,get_internal = True, units='m')
base_offset    = convert_internal_units(0.30, get_internal= True, units='m')
with Transaction(doc, __title__) as t:

    t.Start()
    comments.Set("Random comments..")
    mark.Set(str(pick_object.Id))
    top_offset.Set(top_offset_)
    b_offset.Set(base_offset)
    el_type.Set(ElementId(24200))
    s_area.Set(40.153)
    s_number.Set(13890123)
    s_boolean.Set(1)
    # Recuerda que no cambie parametros
    t.Commit()




