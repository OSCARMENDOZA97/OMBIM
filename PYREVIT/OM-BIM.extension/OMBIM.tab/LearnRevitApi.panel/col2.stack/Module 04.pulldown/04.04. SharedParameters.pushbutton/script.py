# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "04.04 Shared Parameters",
    "en_gb": "04.04 Shared Parameters",
    "es_es": "04.04 Shared Parameters"
}  # Nombre de del boton mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 21.10.2024
____________________________________________
Descripción
Learn how to work with shared parameters
How to check if they are loaded in the project
How load more shared parameters
How to modify existing Shared Parameters
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

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
app   = __revit__.Application


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================


def check_loaded_parameters(list_p_names):
    """
    Check if any parameters from provided list are missing in the project
    :param list_p_names:
    :return:
    """
    # Nota si borrras el texto te apaece
    # 1. Lista de parametros -> ParametersBindings -> bindingmap Class
    bm = doc.ParameterBindings
    itor = bm.ForwardIterator()


    # Reset to the beginning
    itor.Reset()
    loaded_parameters = []

    # Iterate over the map
    while itor.MoveNext():
        try:
            d = itor.Key # Definition that is the current focus of the iterator
            loaded_parameters.append(d.Name)
        except:
            pass

    missing_params = [p_name for p_name in req_parameters if p_name not in loaded_parameters]
    return missing_params

req_parameters = [listadoparametros]
missing_params = check_loaded_parameters(req_parameters)

# for x in missing_params:
#     print x

"""Ejercicio 2"""

# BrindingMapClass -> insert method
# Access shared parameter file
spfile = app.OpenSharedParameterFile()


# Find definition to missin parameter name
missing_def = []
if spfile:
    for group in spfile.Groups:
        print("\n Group Name {}".format(group.Name))
        for p_def in group.Definitions:
            if p_def.Name in missing_params:
                missing_def.append(p_def)

            #print("Parameter name: {}".format(p_def.Name))
            #print(p_def) # Te va a salir un external definition

"""
Internal definition -> Autodesk revit model loaded
External definition -> Written in shared parameter file 
1. Open SharedParameterFile
2. Read Sheared ParameterFile
3. Crate Binding with Categories
4. Add Definition to Revit Project

"""

"""
Notas:
 No Podemos traer ni modificar los projects parameters
 Pero si se puede modifcar y traerlo los parametros compartidos
 
Definition -> Es lo que define a los parametros 
Parametros -> Son unicos para cada elemento invdividual 

** FORMA DE TRABAJO **
Por alguna razón no funciona bien con el bucle for

Obtienes el iterador -> definition1
move next method -> definition2
move next method -> definition3

* Como añadir parametros *
1. Select shared Parameters (Select Group)
2. Type / Instance
3. Parameter Group
4. Category set
5. Varies by group

"""
